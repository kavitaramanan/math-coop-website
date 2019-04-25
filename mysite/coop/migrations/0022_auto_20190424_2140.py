# Generated by Django 2.2 on 2019-04-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0021_auto_20181204_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreach',
            name='date',
            field=models.DateField(blank=True, default='', null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='location',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='people',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='outreach', to='coop.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='author',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='level',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='summary',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='topics',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='pres', to='coop.Topic'),
        ),
    ]
