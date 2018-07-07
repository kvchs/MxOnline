from django.urls import path
# from users.views import user_login
from users.views import LoginView, RegisterView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),

]
