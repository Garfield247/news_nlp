# 说明书册

## 项目结构说明

```shell
├── Pr_Task
│   ├── app 
│   │   ├── config.py #项目配置文件
│   │   ├── extensions.py # 项目初始化脚本
│   │   ├── __init__.py
│   │   ├── models #数据库模型包
│   │   │   ├── __init__.py
│   │   │   ├── tbl_phone_brand_count.py
│   │   │   ├── tbl_phone_color_count.py
│   │   │   └── tbl_phone_size_count.py
│   │   ├── static #静态文件目录
│   │   │   ├── css
│   │   │   ├── favicon.ico
│   │   │   ├── img
│   │   │   │   └── bg.jpg
│   │   │   └── js
│   │   │       ├── echarts.min.js
│   │   │       └── jquery.min.js
│   │   ├── templates # 模板目录
│   │   │   ├── errors
│   │   │   │   └── 404.html
│   │   │   └── main
│   │   │       ├── index.html
│   │   │       └── test.html
│   │   └── views #视图函数目录
│   │       ├── __init__.py
│   │       └── main.py
│   ├── manage.py # 项目管理文件
│   ├── migrations # 数据迁移文件夹
│   └── requirements.txt # 依赖包list
└── README.md # 本文件，项目说明

```



## 数据库迁移（初次运行项目要先进行数据库迁移）

以上三步完成mondel定义的表结构向数据库的迁移。并且会在项目下生成migrations/目录，保存数据库每次变更的内容。

1. 创建数据库表

   ```shell
   python manage.py db init
   ```

2. 提交修改

   ```
   python manage.py db migrate
   ```

3. 执行修改

   ```
   python manage.py db upgrage
   ```

**注：**若变更数据库则删除migrations目录，重新进行迁移

## 启动

```shell
# 在manage.py的目录下
python managr.py runserver 
```

