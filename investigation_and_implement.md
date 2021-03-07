> 请尽可能详细的记录调研和实现的过程, 包括检索过的资料链接和思考过程等.

总用时8个小时

pygit2仓库：https://github.com/libgit2/pygit2
文档：https://www.pygit2.org/
文档中有很多无效信息，很多还是从代码仓库中test代码中搜索出来的

networkx仓库：https://github.com/networkx/networkx
文档：https://networkx.org/documentation/stable/
通过dir(nx)查找可用的函数

有向无环图知识查找，很多忘了

思路：
cg.dot是一个有向无环图，我的想法如下
1. 找到所有的out_edges、input_degree
2. 排序
3. 按照顺序来commit，第一个需要init，然后对于入度>1的commit做一个merge，对于每个结点的下一邻居结点list中，第一个结点和父结点保持同一分支，其他结点增加新分支


中间饶了很多弯子，没想好怎么处理merge，没有commit排序等
