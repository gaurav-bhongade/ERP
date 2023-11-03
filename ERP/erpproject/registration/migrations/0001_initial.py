# Generated by Django 3.2.20 on 2023-11-03 13:43

from django.db import migrations, models
import django.utils.timezone


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
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('contact', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('aadhaar', models.CharField(max_length=12)),
                ('marital_status', models.CharField(max_length=20)),
                ('spouse_name', models.CharField(blank=True, max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('dpt_manager', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('grade_pay', models.FloatField(blank=True, null=True)),
                ('basic_pay', models.FloatField(blank=True, null=True)),
                ('taxation', models.FloatField(blank=True, null=True)),
                ('project', models.CharField(max_length=50)),
                ('security_question', models.CharField(blank=True, max_length=255, null=True)),
                ('security_answer', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, related_name='registration_users', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='registration_users_permissions', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
