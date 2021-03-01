## 题目

实现一个python类库, 提供一个接口, 以`data`目录下的子目录作为输入(src_dir), 在目标目录(dest_dir)下创建同名的git代码库. 此题目为开放性题目, 不限时, 并且可以随意检索资料, 但是需要在`investigation_and_implement.md`文件中记录调研实现的思路和过程, 并记录用时.

## data目录结构

1. `data`目录下包含两个子目录`test_repo_1`和`test_repo_2`, 每个目录代表一个git项目, 以下以`test_repo_1`为例.
1. `test_repo_1`包含两部分, `cg.dot`文件记录了git项目的commit graph; 以大写字母开头的文件夹对应每个commit包含的所有文件.
    ```
    $ tree

    .
    ├── README.md
    ├── data
    │   ├── test_repo_1                 
    │   │   ├── A                       # Commit A, "A" 为commit message
    │   │   │   └── CallGraph.java      # 当checkout到这个commit时, 只包含CallGraph.java一个文件
    │   │   ├── B
    │   │   │   └── CallGraph.java
    │   │   ├── C
    │   │   │   └── CallGraph.java
    │   │   ├── D
    │   │   │   ├── CallGraph.java
    │   │   │   └── SecondFile.java
    │   │   ├── G                       # Commit G, "G" 为commit message
    │   │   │   ├── CallGraph.java      # 当checkout到这个commit时, 包含两个文件CallGraph.java和SecondFile.java
    │   │   │   └── SecondFile.java
    │   │   └── cg.dot                  # 该项目的 commit graph
    │   └── test_repo_2
    │       ├── A
    │       │   └── app.go
    │       ├── B
    │       │   └── app.go
    │       ├── C
    │       │   └── app.go
    │       ├── D
    │       │   └── app.go
    │       ├── E
    │       │   └── app.go
    │       ├── F
    │       │   └── app.go
    │       ├── G
    │       │   └── app.go
    │       ├── README.md
    │       └── cg.dot
    └── investigation_and_implement.md  # 记录调研实现的思路和过程, 记录用时
    ```

1. cg.dot文件示例, 以下git commit graph表示:
    - 第1行的`test_repo_1`是git项目的名字
    - 接下来的每一行可以看做是一个分支, 第2行为主干分支, 第3行是feature分支
    - Commit A为初始commit
    - 从Commit B上分出两个分支, 每个各自新增了一个commit, C和G
    - 最后feature分支合并回主干分支, D为merge commit
    ```
    digraph test_repo_1 {
        A -> B -> C -> D ;
            B -> G -> D ;
    }
    ```

## 实现要求

1. 将此目录(`create-git-repository`)转化成一个符合pip包管理的python类库项目, 可以让使用者通过pip install安装使用
1. 对外暴露的接口函数命名为`create_test_repo`
    ```python
    def create_test_repo(src_dir, dest_dir):
        pass
    ```
1. 此题目需要用到git相关的库来进行git操作, 以及graph相关的库来加载和使用`.dot`文件, 推荐使用[pygit2]()和[networkx](), 当然也可以使用其他熟悉的库代替.
1. 每一个commit的author和committer都可以是`AE <ae@example.com>`
1. 所有HEAD commit需要创建一个分支与之对应, 分支名字与HEAD commit message相同
