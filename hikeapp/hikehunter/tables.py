import django_tables2 as tables
from hikehunter.models import Hike

class HikeTable(tables.Table):
    class Meta:
        model = Hike
        fields = ("region", "difficulty", "terrain", "peak")