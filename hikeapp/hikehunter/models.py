from django.db import models
import django_filters
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Difficulty(models.Model):
    difficult_list = (
        ("Easy", "Easy"),
        ("Moderate", "Moderate"),
        ("Moderately Strenuous", "Moderately Strenuous"),
        ("Strenuous", "Strenuous"),
        ("Very Strenuous", "Very Strenuous")
    )

class Region(models.Model):
    region_list = (
        ("Hlavní město Praha", "Hlavní město Praha"),
        ("Středočeský kraj", "Středočeský kraj"),
        ("Jihočeský kraj", "Jihočeský kraj"),
        ("Plzeňský kraj", "Plzeňský kraj"),
        ("Karlovarský kraj", "Karlovarský kraj"),
        ("Ústecký kraj", "Ústecký kraj"),
        ("Liberecký kraj", "Liberecký kraj"),
        ("Královéhradecký kraj", "Královéhradecký kraj"),
        ("Pardubický kraj", "Pardubický kraj"),
        ("Kraj Vysočina", "Kraj Vysočina"),
        ("Jihomoravský kraj", "Jihomoravský kraj"),
        ("Zlínský kraj", "Zlínský kraj"),
        ("Olomoucký kraj", "Olomoucký kraj"),
        ("Moravskoslezský kraj", "Moravskoslezský kraj")
    )

class Terrain(models.Model):
    terrain_list = (
        ("Forest", "Forest"),
        ("Fields", "Fields"),
        ("Rocks", "Rocks"),
        ("Meadows", "Meadows"),
        ("Mixed", "Mixed")
    )

class Hike(models.Model):
    region_list = (
        ("Hlavní město Praha", "Hlavní město Praha"),
        ("Středočeský kraj", "Středočeský kraj"),
        ("Jihočeský kraj", "Jihočeský kraj"),
        ("Plzeňský kraj", "Plzeňský kraj"),
        ("Karlovarský kraj", "Karlovarský kraj"),
        ("Ústecký kraj", "Ústecký kraj"),
        ("Liberecký kraj", "Liberecký kraj"),
        ("Královéhradecký kraj", "Královéhradecký kraj"),
        ("Pardubický kraj", "Pardubický kraj"),
        ("Kraj Vysočina", "Kraj Vysočina"),
        ("Jihomoravský kraj", "Jihomoravský kraj"),
        ("Zlínský kraj", "Zlínský kraj"),
        ("Olomoucký kraj", "Olomoucký kraj"),
        ("Moravskoslezský kraj", "Moravskoslezský kraj")
    )
    difficult_list = (
        ("Easy", "Easy"),
        ("Moderate", "Moderate"),
        ("Moderately Strenuous", "Moderately Strenuous"),
        ("Strenuous", "Strenuous"),
        ("Very Strenuous", "Very Strenuous")
    )

    terrain_list = (
        ("Forest", "Forest"),
        ("Fields", "Fields"),
        ("Rocks", "Rocks"),
        ("Meadows", "Meadows"),
        ("Mixed", "Mixed")
    )

    name = models.CharField(max_length=50)
    header_image = models.FileField(null=True, blank=True,
                             upload_to="")
    description = RichTextField("Description", null=True, blank=True)
    region = models.CharField("Region", max_length=50, choices=region_list)
    difficulty = models.CharField("Difficulty", max_length=50, default="E", choices=difficult_list)
    terrain = models.CharField("Terrain", max_length=50, default="MI", choices=terrain_list)
    length = models.DecimalField(max_digits=4, decimal_places=2)
    peak = models.IntegerField()
    lowestpoint = models.IntegerField()

