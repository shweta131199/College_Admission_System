from django.urls import path
from . import views
from .views import UpdatePostView, notice, online_admission, index, hostel_status


urlpatterns = [
    path("", views.index, name="index"),
    path("online_admission/", views.online_admission, name="online_admission"),
    path('home/', views.home, name="home"),
    # path('products/', views.products, name='products'),
    path('notice/', views.notice, name="notice"),
    # path('admission_form/', views.admission_form, name="admission_form"),
    path('merit_list/', views.merit_list, name="merit_list"),
    path('hostel/', views.hostel, name="hostel"),
    path('help_support/', views.help_support, name="help_support"),
    path("college/", views.college, name="college"),
    path("new_notice/", views.new_notice, name="new_notice"),

    path("notice/<int:myid>/", views.notice, name="notice"),
    path("application_form/", views.application_form, name="application_form"),
    path("hostel_form/", views.hostel_form, name="hostel_form"),
    path("edit_application/", views.edit_application, name="edit_application"),
    path("hostel_edit_application/", views.hostel_edit_application, name="hostel_edit_application"),
    path("status/", views.status, name="status"),
    path("hostel_status/", views.hostel_status, name="hostel_status"),
   

    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.loggedout, name="logout"),

    path("handle_admin/", views.handle_admin, name="handle_admin"),
    path("users/", views.users, name="users"),
    path("student_application/<int:myid>/", views.student_application, name="student_application"),
    path("application_status/<int:pk>/", UpdatePostView.as_view(), name="application_status"),
    path("approved_applications/", views.approved_applications, name="approved_applications"),
    path("pending_applications/", views.pending_applications, name="pending_applications"),
    path("rejected_applications/", views.rejected_applications, name="rejected_applications"),
    path("hostel_application/<int:myid>/", views.hostel_application, name="hostel_application"),

    path("hostel_approved_application/", views.hostel_approved_application, name="hostel_approved_application"),
    path("hostel_pending_application/", views.hostel_pending_application, name="hostel_pending_application"),
    path("hostel_application_status/<int:pk>/", views.hostel_application_status, name="hostel_application_status"),



]