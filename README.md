在python2.7.10 和 3.5.0上测试通过

# 目录结构
待处理的数据目录放在与data-process同级目录下, 待处理数据的目录结构必须为以下结构：

* 总目录 -- 该目录名在config_default.py -> folder项中进行配置
    * annotations
        * xml
    * image
    
xml和image文件名为 xxx_xxx_xxx 或 xxx_xxx 的数字形式

# 使用方法
* makeLable.py : 检测xml和image下文件的文件名是否完全一致，如果一致则在anotations目录下生成标签文件，包括trainval.txt、 list.txt、 test.txt
* splitFiles.py : 把符合规则的xml和image文件摘取出来，并生成新的目录

# 配置文件
将config_default.example.py 复制为config_default.py, 更改config_default.py中的配置
* folder : 待处理的数据目录
* target_folder : 摘取出的文件存放到的新目录
* files : 待摘取文件的名字匹配规则, 比如101:* , 表示摘取出文件名前缀为101的文件，102:'01, 02' 表示摘取出文件名前缀为102_01 和  102_02的文件
