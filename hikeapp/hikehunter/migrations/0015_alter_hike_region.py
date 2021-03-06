# Generated by Django 4.0.5 on 2022-06-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikehunter', '0014_alter_hike_header_image_alter_hike_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='region',
            field=models.CharField(choices=[('HLP', 'Hlavní město Praha'), ('STK', 'Středočeský kraj'), ('JHK', 'Jihočeský kraj'), ('PLK', 'Plzeňský kraj'), ('KRK', 'Karlovarský kraj'), ('USK', 'Ústecký kraj'), ('LBK', 'Liberecký kraj'), ('KHK', 'Královéhradecký kraj'), ('PRK', 'Pardubický kraj'), ('KRV', 'Kraj Vysočina'), ('Jihomoravský kraj', 'Jihomoravský kraj'), ('ZLK', 'Zlínský kraj'), ('OLK', 'Olomoucký kraj'), ('MSK', 'Moravskoslezský kraj')], max_length=50, verbose_name='Region'),
        ),
    ]
