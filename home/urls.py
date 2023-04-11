from django.urls import path
from home.views import init_home, register_user, login_user

urlpatterns = [
    # path('sarasa/<str:nombre>/<str:apellido>/',vista_prueba),
    # path('template-params', pasar_info_a_template),
    path('', init_home ,name='inicio'),
    path('registro', register_user,name='registro'),
    path('iniciar-sesion', login_user, name='iniciar sesion')
]