from django.apps import AppConfig


class OperationConfig(AppConfig):
    name = 'operation'
    # app展示名称
    verbose_name = '用户操作'
    # 然后配置__init__.py文件内容*（当前app）
