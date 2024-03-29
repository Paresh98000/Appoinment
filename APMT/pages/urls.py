from django.urls import path, re_path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('homepage',views.home,name='home'),
	path('about',views.about,name='about'),
	path('contact',views.contact,name='contact'),
	path('client/signup',views.clientSignup,name='clientSignup'),
	path('client/signin',views.signin,name='signin'),
	path('sp/signup',views.SPSignup,name='spsignup'),
	path('sp/login',views.SPLogin,name='splogin'),
	path('homepage/logout',views.logout,name='lot'),
	path('client/dashboard',views.clientdashboard,name='clientdbd'),
	path('client/profile',views.cpf,name='clientprf'),
	path('sp/dashboard',views.spdashboard,name='spdbd'),
	path('sp/profile',views.spprofile,name='spprf'),
	path('client/appointment',views.appointments,name='appointment'),
	path('sp/appointment',views.manageappointment_sp,name='appointment_sp'),
	path('client/appointment/edit/<int:appid>',views.editappointment,name="editapp"),
	path('client/appointment/delete/<int:appid>',views.deleteappointment,name="delapp"),
	path('client/notification',views.notification,name='notification'),
	path('sp/newservice',views.newservice,name='newservice'),
	path('sp/manageservice',views.manageservice,name='manageservice'),
	path('sp/editservice',views.editservice,name='editservice'),
	path('sp/deleteservice',views.deleteservice,name='deleteservice'),
	path('service/view',views.view_service,name='view_service'),
	path('client/manageappointment',views.manageappointment,name='manageappointment'),
	path('sp/appointment/approve',views.appapprove,name='approve'),
	path('sp/appointment/reject',views.appreject,name='reject'),
	path('service/search',views.search,name='search'),
	path('order/',views.order,name='order'),
	path("handlerequest/", views.handlerequest, name="HandleRequest"),
	path("paytm/", views.paytm, name="paytm"),
	path("aboutus/", views.aboutus, name="aboutus"),
	path("contactus/", views.contactus, name="contactus"),
]
