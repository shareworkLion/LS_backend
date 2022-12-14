# Generated by Django 4.0.4 on 2022-08-10 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('upload_at', models.DateTimeField(auto_now=True)),
                ('comment_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LsApp.comment')),
                ('comment_reply_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
