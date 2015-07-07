from django.contrib import admin

# Register your models here.
from productapp.models import login_info,user_info,category,product,comment

admin.site.register(login_info)
admin.site.register(user_info)
admin.site.register(category)
admin.site.register(product)
admin.site.register(comment)