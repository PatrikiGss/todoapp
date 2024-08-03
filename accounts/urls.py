from django.urls import path # type: ignore
from . import api_views

app_name = 'accounts'

urlpatterns = [
    # URLs para usuários
    path('api/novo-usuario/', api_views.AddUserAPIView.as_view(), name='api_add_user'),
    path('api/login/', api_views.UserLoginAPIView.as_view(), name='api_user_login'),
    path('api/sair/', api_views.UserLogoutAPIView.as_view(), name='api_user_logout'),
    path('api/alterar-senha/', api_views.UserChangePasswordAPIView.as_view(), name='api_user_change_password'),

    # URLs para perfis de usuário
    path('api/meu-perfil/', api_views.ListUserProfileAPIView.as_view(), name='api_list_user_profile'),
    path('api/novo-perfil/', api_views.AddUserProfileAPIView.as_view(), name='api_add_user_profile'),
    path('api/alterar-perfil/<str:username>/', api_views.ChangeUserProfileAPIView.as_view(), name='api_change_user_profile'),

    # URL para alterar informações do usuário
    path('api/editar-usuario/<str:username>/', api_views.ChangeUserInformationAPIView.as_view(), name='api_change_user_information'),
    ]

