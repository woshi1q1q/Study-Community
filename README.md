# Study-Community
基于Flask编写的类似于forum的学习交流网站

--------------------2018-8-23首次上传-----------------------

#基础登录注册

#发表文章

#评论

#个人信息页面

#动态信息

*后续慢慢完善功能

--------------------2018-8-27更新-----------------------

1.增加admin后台:可后台管理账号文章以及评论，当前用户为admin时才能进行后台管理，否则无效

2.优化内容的显示 enter即可换行

3.增加个人页面的权限操作功能：新增删除文章和修改文章的功能

--------------------2019-3-30更新-----------------------
1.优化部分页面内容显示

2.增加Markdown语法，文章以及评论均可使用。新建以及修改文章部分整体修改，使用Markdown编辑器

3.增加上传图片功能，上传图片至staic/uploads文件下

4.增加数据库迁移，首次执行请输入
'''
Python manage.py db init
python manage.py db migrate
python manage.py db upgrade
'''
后续更新数据库只需要执行后两条。
