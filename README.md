#                     Note
1. 安装MySQL驱动： pip install mysqlclient
2. Ctrl + 鼠标左键查看函数定义，Alt + 左箭头 返回原代码
3. 怎样在setting中设置 apps的搜索路径？(*)

   import os

   import sys

   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

   sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

   sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))
4. template guide(模板标签)
https://docs.djangoproject.com/en/2.0/ref/templates/builtins/

====================================================

5. 项目概要
(1) users - 用户管理
(2) course - 课程管理
(3) organization - 机构和教师管理
(4) operation - 用户操作管理

6. users.UserProfile.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
   Fixed by: Get Pillow at https://pypi.org/project/Pillow/ or run command "pip install Pillow".
7. Add or change a related_name argument to the definition for 'UserProfile.user_permissions' or 'User.user_permissions'.

      Fixed by:(只能在首次进行数据迁移前进行设置) Warning You cannot change the AUTH_USER_MODEL setting during the lifetime of a project (i.e. once you have made and migrated models that depend on it) without serious effort. It is intended to be set at the project start, and the model it refers to must be available in the first migration of the app that it lives in. See Substituting a custom User model for more details.
      https://docs.djangoproject.com/en/2.0/ref/settings/
6. django.db.utils.DataError: (1406, "Data too long for column 'gender' at row 1")
   Fixed by: https://blog.csdn.net/qingche456/article/details/58106629
7.  UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 3444: illegal multibyte sequence
  Fixed by:https://blog.csdn.net/qingche456/article/details/58279692  (直接下载源文件安装)
8. ModuleNotFoundError: No module named 'django.core.urlresolvers'

    Fixed by: https://blog.csdn.net/Cand6oy/article/details/79243166  (xadmin2 才能兼容django2.0和以上版本)pip install xadmin-django2.zip
9. https://github.com/mbi/django-simple-captcha Django框架的验证码设置
   如果安装失败，改变_imaging.cp36-win_amd64.pyd 文件的权限，获取所有权限
   http://django-simple-captcha.readthedocs.io/en/latest/usage.html

10. https://github.com/jamespacileo/django-pure-pagination django分页模块

