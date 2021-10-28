from django.urls import path,include
#from employee_register import views
from . import views
from django.contrib import admin
#from views import register_request, login_request,logout_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_employee/', views.employee_form,name='employee_insert'),
    path('<int:id>/', views.employee_form,name='employee_update'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('',views.employee_list,name='employee_list'),
    path('second_task',views.num_to_word,name='num_to_word'),

]