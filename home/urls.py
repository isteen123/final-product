from django.urls import path

from . import views


urlpatterns = [
    path('', views.index,name='index'),
   
    
    path('add_clint/', views.add_clint,name='add_clint'),
    path('add_agent/', views.add_agent,name='add_agent'),
    path('add_agent/delete_agent/<int:id>', views.delete_agent, name='delete_agent'),
    path('tableview/', views.tableview,name='tableview'),
    path('tableview/took/<int:id>',views.took,name='took'),
    path('tableview/revok/<int:id>',views.revok,name='revok'),
    path('tableview/done/<int:id>',views.done,name='done'),
    path('tableview/delete/<int:id>', views.delete, name='delete'),
    path('donetable/delete_done/<int:id>', views.delete_done, name='delete_done'),
    path('donetable/', views.donetable,name='donetable'),
    path('tableview/editepage/<int:id>',views.editepage,name='editepage'),
    path('tableview/editepage/edite_table/<int:id>',views.edite_table,name='edite_table'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('emp_table', views.emp_table, name='emp_table'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
    path('tableview/add_exid/<int:id>',views.add_exid,name='add_exid'),

]
