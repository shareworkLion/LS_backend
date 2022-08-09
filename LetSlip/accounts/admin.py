from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# 사용자 밑에 프로필 보여주기 위함
class ProfileInLine(admin.StackedInline):
    model = Profile
    con_delete = False # 프로필 삭제

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)