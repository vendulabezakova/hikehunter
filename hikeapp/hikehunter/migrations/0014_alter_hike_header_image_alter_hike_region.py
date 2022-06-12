# Generated by Django 4.0.5 on 2022-06-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikehunter', '0013_hike_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='header_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='hike',
            name='region',
            field=models.CharField(choices=[('HLP', 'Hlavní město Praha'), ('STK', 'Středočeský kraj'), ('JHK', 'Jihočeský kraj'), ('PLK', 'Plzeňský kraj'), ('KRK', 'Karlovarský kraj'), ('USK', 'Ústecký kraj'), ('LBK', 'Liberecký kraj'), ('KHK', 'Královéhradecký kraj'), ('PRK', 'Pardubický kraj'), ('KRV', 'Kraj Vysočina'), ('Jihomoravský kraj', 'JMK'), ('ZLK', 'Zlínský kraj'), ('OLK', 'Olomoucký kraj'), ('MSK', 'Moravskoslezský kraj')], max_length=50, verbose_name='Region'),
        ),
    ]
