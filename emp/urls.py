from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from emp import views as emp_views

urlpatterns = [
    path('', emp_views.list_employee, name='list_employee'),  # ✅ เพิ่ม comma ที่ลืม
    

    path('add/', emp_views.add_employee, name='add_employee'),
    path('edit/<int:emp_id>/', emp_views.edit_employee, name='edit_employee'),
    path('delete/<int:emp_id>/', emp_views.delete_employee, name='delete_employee'),
    path('dashboard/', emp_views.dashboard, name='dashboard'),
    path('export/', emp_views.export_employees_csv, name='export_employees_csv'),

    # Auth
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='emp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', emp_views.register, name='register'),

    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='emp/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='emp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='emp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='emp/password_reset_complete.html'), name='password_reset_complete'),
]
