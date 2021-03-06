# Basic Flask Website
* A simple Flask website, including user register, login, logout and password reset function
* Other language version: [简体中文](README.zh-cn.md), [English](README.md)

## Get Started
* Using Python 3.7, create a .env file to storge database link and password
* MySQL as local database

## Prerequisites
Create a MySQL non-root user which can access database with localhost
   ```
   Use FlaskTest;
   Create User '***'@'localhost' identified by '***';
   grant all privileges on FlaskTest.* to '***'@'%';
   ```
Table Structure
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

## Installing and Deployment
```
virtualenv venv
pip3 install -r requirements.txt
run app.py
```
## Reference
* [Yufan Zheng](https://github.com/alphafan/flask-user-auth-example/blob/master/app/main/routes.py)  --  flask user auth example