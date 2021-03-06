# Generated by Django 4.0.5 on 2022-06-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikehunter', '0003_alter_hike_description_alter_hike_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='region',
            field=models.CharField(choices=[('HLP', 'Hlavní město Praha'), ('STK', 'Středočeský kraj'), ('JHK', 'Jihočeský kraj'), ('PLK', 'Plzeňský kraj'), ('KRK', 'Karlovarský kraj'), ('USK', 'Ústecký kraj'), ('LBK', 'Liberecký kraj'), ('KHK', 'Královéhradecký kraj'), ('PRK', 'Pardubický kraj'), ('KRV', 'Kraj Vysočina'), ('JMK', 'Jihomoravský kraj'), ('ZLK', 'Zlínský kraj'), ('OLK', 'Olomoucký kraj'), ('MSK', 'Moravskoslezský kraj')], default='HLP', max_length=50, verbose_name='Region'),
        ),
    ]
