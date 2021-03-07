# coding:utf8

import os
import shutil
import pygit2
import networkx as nx
    

USER_NAME = 'AE'
USER_MAIL = 'ae@example.com'


def create_test_repo(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)
    author = pygit2.Signature(USER_NAME, USER_MAIL)
    committer = author
    in_degree_map, g_next, g_previous = read_dot(os.path.join(dest_dir, 'cg.dot'))
    '''
    {
        'commit_name': {
            'branch_name': '',
            'commit_id': ''
        }
    }
    '''
    commit_infos = {}
    sorted_commits = top_sort(g_next, in_degree_map)
    repo = None
    for idx, commit in enumerate(sorted_commits):
        branch_name = None
        commit_msg = commit
        pathspecs = [commit]
        if idx == 0:
            repo = pygit2.init_repository(dest_dir)
            branch_name = commit
            repo.index.add_all(pathspecs)
            repo.index.write()
            tree = repo.index.write_tree()
            repo.create_commit('HEAD', author, committer, commit_msg, tree, [])
        else:
            previous_commits = g_previous.get(commit)
            if len(previous_commits) == 1:
                previous_commit = previous_commits[0]
                previous_branch_name = commit_infos.get(previous_commit)['branch_name']
                branch_name = previous_branch_name
                previous_commit_id = commit_infos.get(previous_commit)['commit_id']
                repo.checkout(repo.lookup_branch(previous_branch_name))
                i = g_next[previous_commit].index(commit)
                if i > 0:
                    # new branch
                    branch_name = commit
                    new_branch = repo.branches.local.create(branch_name, repo[previous_commit_id])
                    repo.checkout(new_branch)
                repo.index.add_all(pathspecs)
                repo.index.write()
                tree = repo.index.write_tree()
                repo.create_commit('HEAD', author, committer, commit_msg, tree, [repo.head.target])
            else:
                # merge commit
                main_branch_commit = previous_commits[0]
                feat_branch_commit = previous_commits[1]
                branch_name = commit_infos.get(main_branch_commit)['branch_name']
                repo.checkout(repo.lookup_branch(branch_name))
                feat_commit_id = commit_infos.get(feat_branch_commit)['commit_id']
                repo.merge(feat_commit_id)
                repo.index.add_all(pathspecs)
                repo.index.write()
                tree = repo.index.write_tree()
                repo.create_commit('HEAD', author, author, commit_msg, tree, [repo.head.target, feat_commit_id])
        commit_infos[commit] = {
            'branch_name': branch_name,
            'commit_id': repo.head.target
        }


def read_dot(dot_file):
    Hin = nx.nx_pydot.read_dot(dot_file)
    in_degree_map = dict(Hin.in_degree())
    out_edges = Hin.out_edges()
    g_next = {}
    g_previous = {}
    for edge in out_edges:
        g_next.setdefault(edge[0], [])
        g_next[edge[0]].append(edge[1])
        g_previous.setdefault(edge[1], [])
        g_previous[edge[1]].append(edge[0])
    return in_degree_map, g_next, g_previous


def top_sort(g, in_degree_map):
    q = [k for k, v in in_degree_map.items() if v == 0]
    res = []
    while q:
        u = q.pop()
        res.append(u)
        for v in g.get(u, []):
            in_degree_map[v] -= 1
            if in_degree_map[v] == 0:
                q.append(v)
    return res


__all__ = ['create_test_repo']

