# 实验结果分析写在这里!
Creating model: ('PP-OCRv5_server_det', None)
Model files already exist. Using cached files. To redownload, please delete the directory manually: `/root/.paddlex/official_models/PP-OCRv5_server_det`.
Creating model: ('PP-OCRv5_server_rec', None)
Model files already exist. Using cached files. To redownload, please delete the directory manually: `/root/.paddlex/official_models/PP-OCRv5_server_rec`.

DEBUG:llama_index.core.node_parser.node_utils:> Adding chunk: 童年趣事你仔细看过蚊子吗？那苗条的身材配上细长的大腿和悠闲的飞行姿态，还有那嗡嗡的
DEBUG:llama_index.core.node_parser.node_utils:> Adding chunk: 的飞行姿态，还有那嗡嗡的“歌声，”是不是让你很有“战斗”的冲动？
DEBUG:llama_index.core.node_parser.node_utils:> Adding chunk: 是不是让你很有“战斗”的冲动？在我童年的夏天，有工段快乐的记忆就与它有关。

INFO:root:Chunk 1 (完整内容):
童年趣事你仔细看过蚊子吗？那苗条的身材配上细长的大腿和悠闲的飞行姿态，还有那嗡嗡的
--------------------------------------------------
INFO:root:Chunk 2 (完整内容):
的飞行姿态，还有那嗡嗡的“歌声，”是不是让你很有“战斗”的冲动？
--------------------------------------------------
INFO:root:Chunk 3 (完整内容):
是不是让你很有“战斗”的冲动？在我童年的夏天，有工段快乐的记忆就与它有关。


文章按照句子被分割，且每个chunk保留了一些overlap的字符

最后结果
query:蚊子有啥特点？
an:蚊子有苗条的身材，长着细长的大腿，飞行姿态悠闲，还会发出嗡嗡的“歌声”。