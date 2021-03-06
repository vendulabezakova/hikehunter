# Generated by Django 4.0.5 on 2022-06-06 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hikehunter', '0002_terrain_alter_hike_difficulty_alter_hike_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hike',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='hike',
            name='difficulty',
            field=models.ForeignKey(blank=True, choices=[('E', 'Easy'), ('M', 'Moderate'), ('MS', 'Moderately Strenuous'), ('S', 'Strenuous'), ('VS', 'Very Strenuous')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='hikehunter.difficulty'),
        ),
        migrations.AlterField(
            model_name='hike',
            name='region',
            field=models.ForeignKey(blank=True, choices=[('HLP', 'Hlavní město Praha'), ('STK', 'Středočeský kraj'), ('JHK', 'Jihočeský kraj'), ('PLK', 'Plzeňský kraj'), ('KRK', 'Karlovarský kraj'), ('USK', 'Ústecký kraj'), ('LBK', 'Liberecký kraj'), ('KHK', 'Královéhradecký kraj'), ('PRK', 'Pardubický kraj'), ('KRV', 'Kraj Vysočina'), ('JMK', 'Jihomoravský kraj'), ('ZLK', 'Zlínský kraj'), ('OLK', 'Olomoucký kraj'), ('MSK', 'Moravskoslezský kraj')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='hikehunter.region'),
        ),
        migrations.AlterField(
            model_name='hike',
            name='terrain',
            field=models.ForeignKey(blank=True, choices=[('FO', 'Forest'), ('FI', 'Fields'), ('RO', 'Rocks'), ('ME', 'Meadows'), ('MI', 'Mixed')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='hikehunter.terrain'),
        ),
    ]
