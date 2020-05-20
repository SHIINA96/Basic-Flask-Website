# Basic Flask Website
* 一个简单的Flask网页模版, 包含了用户注册，登录，登出以及密码找回功能
* 其他语言版本: [简体中文](README.zh-cn.md), [English](README.md)


## 开始
* 使用Python3.7建立，在根目录下添加.env文件来存储数据库链接以及密码
* 本地数据库使用MySQL

## 前期准备
给本地MySQL建立可外部访问的非root用户
   ```
   Use FlaskTest;
   Create User '***'@'localhost' identified by '***';
   grant all privileges on FlaskTest.* to '***'@'%';
   ```
表的结构
```
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| username | varchar(120) | NO   | UNI | NULL    |                |
| password | varchar(120) | NO   |     | NULL    |                |
| email    | varchar(120) | NO   | UNI | NULL    |                |
| cTime    | datetime     | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

## 安装与部署
```
virtualenv venv
pip3 install -r requirements.txt
run app.py
```
## 参考
* [Yufan Zheng](https://github.com/alphafan/flask-user-auth-example/blob/master/app/main/routes.py)  --  flask user auth example