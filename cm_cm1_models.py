import logging
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
#from api.v1.users.models import UserInfo
#from api.v1.enums import *

logger = logging.getLogger(__name__)
# Create your models here.

SOCIAL_MEDIA_OPTIONS = (
    ("", ""),
    ("_Propagated", "_Propagated"),
    ("Facebook", "Facebook"),
    ("GooglePlus", "GooglePlus"),
    ("LinkedIn", "LinkedIn"),
    ("Twitter", "Twitter"),
    ("Instagram", "Instagram"),
    ("Pinterest", "Pinterest"),
    ("Foursquare", "Foursquare"),
)


class user(models.Model):

    username = models.CharField(max_length=200)
    f_link = models.CharField(max_length=200,null=True)
    t_link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.username)+ ' ' + str(self.f_link)+' '+ str(self.t_link) + '\n'


class TempContactPicture(models.Model):
    PICTURE_OPTIONS = (
        (1, "Profile Picture"),
        (2, "Cover Photo")
    )
    picture_title = models.CharField(max_length=500, null=True, blank=True)
    picture_url = models.URLField(max_length=500, null=True, blank=True)
    cdn_key = models.CharField(max_length=500, null=True, blank=True)
    type = models.SmallIntegerField(choices=PICTURE_OPTIONS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%s' % self.picture_url

    class Meta:
        app_label = 'cm1'

    def get_pic_type(self):
        if self.type == 1:
            return 'profile'
        elif self.type == 2:
            return 'cover'


class TempContact(models.Model):

    GENDER_OPTIONS = (
        (1, "Male"),
        (2, "Female"),
    )
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200,null=True,blank=True)
    other_phone = models.IntegerField(null=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    photo = models.CharField(max_length=500, null=True, blank=True)
    profile_picture = models.OneToOneField(TempContactPicture, related_name="temp_contact_profile_picture", null=True)
    cover_photo = models.CharField(max_length=500, null=True, blank=True)
    cover_picture = models.OneToOneField(TempContactPicture, related_name="temp_contact_cover_picture", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.SmallIntegerField(choices=GENDER_OPTIONS, null=True, blank=True)
    dob = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.f_name) + ' ' + ' '+ str(self.l_name) + ' '+ ' ' +str(self.other_phone)+' '+str(self.city)+' '+str(self.photo)+' '+str(self.profile_picture)+' '+str(self.cover_photo)+' '+str(self.cover_picture)+' '+str(self.dob)+' '+str(self.gender) +'\n'

    class Meta:
        verbose_name_plural = 'Temporary Contacts'
        app_label = 'cm1'
        ordering = ('-updated_at',)

    def type(self):
        return "temp_contact"


class Contact(models.Model):
    CONTACT_STATUS_OPTIONS = (
        (0, "Followed"),
        (1, "Pending"),
        (2, "Connected"),
        (3, "Declined"),
        (4, "Blocked"),
    )
    user = models.ForeignKey(User, db_column="user_id", db_index=True, related_name="user_contacts",
                             on_delete=models.CASCADE)
    user_id1 = models.CharField(max_length=12)
    contact = models.ForeignKey(User, db_column="contact_id", db_index=True, related_name="user__contacts",
                                on_delete=models.CASCADE)
    contact_id1 = models.CharField(max_length=12)
    status = models.IntegerField(choices=CONTACT_STATUS_OPTIONS, default=0)
    mute_notification = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%d-%s-%d-%s-%d' % (
            self.user.id, self.user__id, self.contact.id, self.contact__id, self.status)

    class Meta:
        unique_together = ('user', 'contact',)


class TempContactNickName(models.Model):
    temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_nicknames",
                                     on_delete=models.CASCADE)
    nick_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_media_source = models.CharField(choices=SOCIAL_MEDIA_OPTIONS, max_length=50, default="")
    is_add_attr = models.BooleanField(default=False)
    temp_id = models.CharField(max_length=12)

    def __str__(self):
        return '%s' % self.nick_name

    class Meta:
        verbose_name_plural = 'Contacts NickName'
        app_label = 'cm1'

class TempContactPhone(models.Model):
    temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_phones",
                                     on_delete=models.CASCADE)
    country_code = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    phone_number = models.CharField(max_length=100, db_index=True)
    display_number = models.CharField(max_length=150)
    international_number = models.CharField(max_length=150)
    phone_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_media_source = models.CharField(choices=SOCIAL_MEDIA_OPTIONS, max_length=50, default="")
    temp_id = models.CharField(max_length=12)
    is_edit_notif_rejected = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.phone_number

    class Meta:
        unique_together = ('temp_contact', 'country_code', 'phone_number',)
        verbose_name_plural = 'Temporary Contact Phones'
        app_label = 'cm1'

class TempContactEmail(models.Model):
    temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_emails",
                                     on_delete=models.CASCADE)
    email_address = models.CharField(max_length=200, db_index=True)
    email_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_media_source = models.CharField(choices=SOCIAL_MEDIA_OPTIONS, max_length=50, default="")
    temp_id = models.CharField(max_length=12)
    is_edit_notif_rejected = models.BooleanField(default=False)
    is_merge_notif_rejected = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.email_address

    class Meta:
        unique_together = ('temp_contact', 'email_address',)
        verbose_name_plural = 'Temporary Contact Emails'
        app_label = 'cm1'


class TempContactWebsite(models.Model):
    temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_websites",
                                     on_delete=models.CASCADE)
    url = models.URLField()
    url_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_media_source = models.CharField(choices=SOCIAL_MEDIA_OPTIONS, max_length=50, default="")
    temp_id = models.CharField(max_length=12)

    def __str__(self):
        return '%s' % self.url

    class Meta:
        verbose_name_plural = 'Temporary Contact Websites'
        app_label = 'cm1'


class TempContactSocialAccount(models.Model):
    temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_social_accounts",
                                     on_delete=models.CASCADE)
    social_media = models.CharField(max_length=50)
    social_account = models.CharField(max_length=500)
    social_name = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verification_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_media_source = models.CharField(choices=SOCIAL_MEDIA_OPTIONS, max_length=50, default="")
    temp_id = models.CharField(max_length=12)

    def __str__(self):
        return '%s' % self.social_account

    class Meta:
        verbose_name_plural = 'Temporary Contact Social Accounts'
        app_label = 'cm1'

class TempContactOtherAccount(models.Model):
    temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_other_accounts",
                                     on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)
    other_account = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    social_media_source = models.CharField(choices=SOCIAL_MEDIA_OPTIONS, max_length=50, default="")
    temp_id = models.CharField(max_length=12)

    def __str__(self):
        return '%s' % self.other_account

    class Meta:
        verbose_name_plural = 'Temporary Contact Other Accounts'
        app_label = 'cm1'

# user joined
class UserJoinedNotification(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name="user_joining_notifications", on_delete=models.CASCADE)
    joining_user = models.ForeignKey(User, db_index=True, related_name="contact_joining_notifications",
                                     on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d-%d-%s' % (self.user.id, self.joining_user.id, self.message)

    class Meta:
        verbose_name_plural = 'User Joined Notifications'


class TempContactPhoneChangeNotification(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name="tct_phone_change_notification", on_delete=models.CASCADE)
   # temp_contact = models.ForeignKey(TempContact, db_index=True, related_name="temp_contact_phone_change_notif",
    #                                 on_delete=models.CASCADE)
    old_country_code = models.CharField(max_length=50, null=True, blank=True)
    old_phone_num = models.CharField(max_length=100)
    old_display_num = models.CharField(max_length=150)
    new_country_code = models.CharField(max_length=50, null=True, blank=True)
    new_phone_num = models.CharField(max_length=100)
    new_display_num = models.CharField(max_length=150)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d-%s' % (self.user.id, self.message)

    class Meta:
        verbose_name_plural = 'Temp Contact Phone Num Change Notifications'
