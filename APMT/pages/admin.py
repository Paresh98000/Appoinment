from .models import appointment,orders,sp,client,admin_local,service
from django.contrib import admin
# Register your models here.
#from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'city', 'email', 'gender','password']
     list_filter = ['id', 'name', 'city', 'email', 'gender']
     list_editable = []

class Admin_LocalAdmin(admin.ModelAdmin):
     list_display = ['id','username','password']
     list_filter = ['id','username','password']
     list_editable = []

class SpAdmin(admin.ModelAdmin):
    list_display = ['id','name','password','phone_no','email','city','status']
    list_filter = ['id','name','password','phone_no','email','city','status']
    list_editable = []

class ServiceAdmin(admin.ModelAdmin):
     list_display = ['id','providerid','title','time_start_h','time_start_m','time_end_h','time_end_m','city','location','day','description','image','status','stype','phone_no','cost']
     list_filter = ['id','providerid','title','time_start_h','time_start_m','time_end_h','time_end_m','city','location','day','description','image','status','stype','phone_no','cost']
     list_editable = []

class AppointmentAdmin(admin.ModelAdmin):
     list_display = ['id','description','date','time','status','payment_status']
     list_filter = ['id','description','date','time','status','payment_status']
     list_editable = []

class OrdersAppoitment(admin.ModelAdmin):
    list_display = ['id','appointmentid','date_and_time','status','amount']
    list_filter = ['id','appointmentid','date_and_time','status','amount']
    list_editable = []

admin.site.register(appointment,AppointmentAdmin)
admin.site.register(admin_local,Admin_LocalAdmin)
admin.site.register(service,ServiceAdmin)
admin.site.register(client,ClientAdmin)
admin.site.register(orders,OrdersAppoitment)
admin.site.register(sp,SpAdmin)
