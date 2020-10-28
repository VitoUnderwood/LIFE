# 新闻评论生成

## 摘要

新闻评论对于传统的seq2seq结构来说长度过长，容易生成不相关，无意义的评论，作者提出graph to seqence模型来解决

## 提出的问题

- 新闻正文太长，影响seq2seq的效果，新闻标题太短，无法提供足够的信息
- 标题存在夸张的成分，无法反映正文
- 一篇文章有不同aspect，用户针对不同aspect可能提出不同评论

## graph-to-sequence model

基于文章的标题和正文组成的图结构来生成评论
实际上就是进行了文本聚类，分成了几个不同主题（主题模型？）

## 整体思路

- 聚类，构建图结构
首先对文档进行关键字提取，tf-idf/textrank均可考虑，可以直接调用结巴库，进行分词和关键字提取，文档的句子根据关键词进行聚类，包含关键词k的句子属于节点k，节点之间的边上的权值用两个节点之间共享的句子的数量来表示
- 对节点进行编码
embedding（ei+pi） + multi-head self-attention
最后使用key所对应的hidden vector来表示整个节点
- 对这个图进行编码
使用GCN + residual connection
- 解码
考虑到title的重要性，title vertex的编码作为decoder的t0输入，或者使用 max pooling or mean pooling.


## new idea

使用ABSA作为提取方式，生成comment
