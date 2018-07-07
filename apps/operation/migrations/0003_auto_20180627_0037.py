# Generated by Django 2.0.6 on 2018-06-27 00:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0002_auto_20180626_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': '用户课程', 'verbose_name_plural': '用户课程'},
        ),
        migrations.AlterModelOptions(
            name='userfavorite',
            options={'verbose_name': '用户收藏', 'verbose_name_plural': '用户收藏'},
        ),
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户消息', 'verbose_name_plural': '用户消息'},
        ),
        migrations.AddField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='fav_id',
            field=models.IntegerField(default=0, verbose_name='数据ID'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '课程'), (2, '课程机构'), (3, '讲师')], default=1),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='has_read',
            field=models.BooleanField(default=False, verbose_name='是否已读'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='message',
            field=models.CharField(default='', max_length=500, verbose_name='消息内容'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='user',
            field=models.IntegerField(default=0, verbose_name='接收用户'),
        ),
    ]