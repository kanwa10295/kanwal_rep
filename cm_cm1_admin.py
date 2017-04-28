from django.contrib import admin

# Register your models here.
from .models import user,TempContactPicture, TempContact,TempContactNickName, TempContactPhone,TempContactEmail, TempContactWebsite, TempContactSocialAccount,TempContactOtherAccount,UserJoinedNotification, TempContactPhoneChangeNotification
mymodels =[user,TempContactPicture, TempContact,TempContactNickName, TempContactPhone,TempContactEmail, TempContactWebsite, TempContactSocialAccount,TempContactOtherAccount,UserJoinedNotification, TempContactPhoneChangeNotification]

admin.site.register(mymodels)
