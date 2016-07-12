# PythonSkillTree (Python技能树总结)

## 写在最前面
### 1.熟练的定义
+ 当你准备在某项技能的后面加上熟练两个字之前，请考虑下面几点

``` bash
1.对运行过程以及机制了解吗？
2.文档看完了没？不是一个函数一个函数看，是要一个大类一个大类的看，知道要实现什么功能要用到什么！！！
3.源码读过没？某些关键的部分知道别人是怎么实现的么？可以自己修改吗？
4.写过几篇总结paper？研究出了多少技巧？
5.利用这项技能写了多少行代码？实现了什么功能
6.遇到过什么奇葩问题？解决了没有？怎么解决的？
```

### 2.项目须知
+ 项目前 (需求-需求分析-架构设计-功能设计)

``` bash
1.将需求转化成思路以及代码的能力！
2.不切实际的需求一定要坚决拒绝或者协商更改！
3.任务拆分，将一个大的任务拆分细化为多个点，并且排好优先级
4.设计能力，实际上就是一个知识积累沉淀的过程，用的多了思考的多了解决的问题多了，自然而然能力就上来了，多看大厂的paper
5.前期文档的重要性：架构，选型，功能设计文档
6.沟通，反馈与责任
```

+ 项目中 (研发-测试)

``` bash
1.良好的编码习惯，不仅能提高效率，还能在出现bug时，快速定位bug点
2.学会单元测试和单步调试，构建自己的测试样例
3.及时反馈研发进度以及问题记录，你和你的Leader，产品经理会希望看到这个
4.寻求帮助，项目中某个问题卡住你一个小时以上的时间，记得寻求帮助，否则他会浪费你更多的时间，前提是这个问题不是太low
```

+ 项目后 (总结-文档-上线-后期维护)

``` bash
1.上面的进度以及问题记录有作用了，归纳之后就是一篇好的总结文档了
2.不写文档的程序员不是一个好的美工
3.还是那个问题，编码习惯不好，后期维护会浪费你很多的时间
```

### 3.其他的一些必备技能
+ IDE以及编辑器 (Pycharm, VIM.......)
+ Linux 使用 ，《鸟哥的私房菜》
+ 翻墙~~。难道你用百度知道上的代码吗？



## 1.基础
+ Python 入门 [传送门](https://github.com/qiwsir/StarterLearningPython)

### 1.1.Google Python语言规范
+ google python 语言规范    [传送门](http://zh-google-styleguide.readthedocs.org/en/latest/google-python-styleguide/python_style_rules/)
+ google python 风格规范    [传送门](http://zh-google-styleguide.readthedocs.org/en/latest/google-python-styleguide/python_style_rules/)
+ Python是一门优雅的语言，代码一定要写的整洁规范，不然当你要维护你一年以前的代码时，你会后悔的，切记！！！

### 1.2.模块导入Demo
+ 跨目录，以及多级目录之间的相互导入，代码组件化

### 1.3.基础库 (StandardLibrary)
+ 在写代码之前先浏览一下标准库，在能用标准库且这个库适合人类使用的时候，标准库更稳定且不用安装
+ StandardLirary.md
+ 官方标准库说明  [传送门](https://docs.python.org/2.7/library/)

### 1.4.第三方库
+ 在使用第三方库之前，要考虑几点

``` bash
1.文档是否齐全
2.是否有更新，久未更新的项目谨慎使用
3.社区是否活跃，bug是否得到及时的反馈和修复
```


## 2.HTTP
### 2.1.HTTP API
+ HTTP API 设计指南    [传送门](http://www.oschina.net/translate/http-api-design)
+ RESTful API 设计指南    [传送门](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)

## 3.服务端
### 3.1.Tornado
+ Tornado Boilerplate 模板
+ Tornado Github [传送门](https://github.com/tornadoweb/tornado)
+ Tornado 中文教程 [传送门](https://github.com/alioth310/itt2zh)
+ Tornado 官网及文档 [传送门](http://www.tornadoweb.org/en/stable/)

### 3.2.Bottle
+ bottle Boilerplate 模板 
+ Bottle Github [传送门](https://github.com/bottlepy/bottle)
+ Bottle 中文教程(似乎是个半成品) [传送门](https://github.com/TaceyWong/Bottle_Doc_zh)
+ Bottle 官网及文档 [传送门](http://www.bottlepy.org/docs/dev/index.html)

### 3.3.Flask
+ Flask Boilerplate 模板
+ Flask Github [传送门](https://github.com/pallets/flask)
+ Flask 官网及文档 [传送门](http://flask.pocoo.org/docs/0.10/)

### 3.4.Celery 异步处理
+ Celery Boilerplate 模板
+ Celery Github [传送门](https://github.com/celery/celery)
+ Tornado-Celery Github [传送门](https://github.com/mher/tornado-celery)
+ Django-Celery Github [传送门](https://github.com/celery/django-celery)
+ Celery 官网及文档 [传送门](http://www.celeryproject.org/)
+ Celery 中文教程 [传送门](http://docs.jinkan.org/docs/celery/)

### 3.5.Auth 验证处理
+ 使用 JWT + Tornado 的简单验证处理模板

### 3.6.Django
+ Django Github [传送门](https://github.com/django/django)

## 4.存储
### 4.1.关系型数据库
+ Mysql - pymysql [传送门](https://github.com/PyMySQL/PyMySQL)
+ Postgresql - psycopg2 [传送门](https://github.com/psycopg/psycopg2)
+ Sqlite - sqlite3 - 标准库
+ ORM - peewee [传送门](https://github.com/coleifer/peewee)
+ ORM - SQLAlchemy [传送门](https://github.com/zzzeek/sqlalchemy)

### 4.2.NOSQL
+ Redis - redis-py [传送门](https://github.com/andymccurdy/redis-py)
+ MongoDB - pymongo [传送门](https://github.com/mongodb/mongo-python-driver)
+ MEMCached - pymemcache [传送门](https://github.com/pinterest/pymemcache)

### 4.3.大数据存储
+ Hbase (分布式，面向列的数据库)
+ ElasticSearch (分布式全文搜索引擎)
+ HDFS (Hadoop子系统，分布式文件系统)
+ FastDFS (轻量级分布式文件系统)
+ MogileFS (分布式文件系统，文件自动备份组件)

### 4.4.队列服务
+ RabbitMQ - pika [传送门](https://github.com/pika/pika)
+ RabbitMQ - kombu [传送门](https://github.com/celery/kombu)

## 5.分布式
### 5.1.通信与调度
+ Zookeeper - kazoo [传送门](https://github.com/python-zk/kazoo)
+ Etcd - python-etcd [传送门](https://github.com/jplana/python-etcd)
+ Rpyc - rpyc [传送门](https://github.com/tomerfiliba/rpyc)
+ SSH - paramiko [传送门](https://github.com/paramiko/paramiko)
+ xmlrpc 标准库

### 5.2.进程线程
+ 多进程，进程池，以及进程间通信
+ 多线程，线程池

### 5.3.Docker
+ DockerFile

``` bash
1.系统级
2.服务级
3.应用级
4.工具级
```

## 6.前端
+ jQuery
+ AdminLTE
+ Bootstrap
+ AngularJS
+ ECharts
