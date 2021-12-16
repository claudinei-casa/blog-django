# Generated by Django 3.2.9 on 2021-12-15 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0002_auto_20211215_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='make',
            new_name='brand',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='slug',
        ),
        migrations.AddField(
            model_name='cars',
            name='title',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='usr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cars',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.IntegerField(choices=[(2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007)]),
        ),
    ]