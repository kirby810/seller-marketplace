# Generated by Django 5.0.6 on 2024-06-24 17:29

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일 주소')),
                ('nickname', models.CharField(blank=True, max_length=150, verbose_name='닉네임')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('profile_picture', models.ImageField(blank=True, default='profile_images/default/profile_picture.png', null=True, upload_to='profile_images/%Y/%m/%d/', verbose_name='프로필 사진')),
                ('is_agree_terms', models.BooleanField(default=False, verbose_name='이용 약관 동의')),
                ('is_agree_privacy_policy', models.BooleanField(default=False, verbose_name='개인정보 처리방침 동의')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성 상태')),
                ('is_staff', models.BooleanField(default=False, verbose_name='스태프 여부')),
                ('role', models.CharField(choices=[('buyer', '구매자'), ('seller', '판매자'), ('admin', '운영자')], default='buyer', max_length=10, verbose_name='역할')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
