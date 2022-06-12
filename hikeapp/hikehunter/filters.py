import django_filters
from .models import Hike
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, ButtonHolder, Submit

class HikeFilter(django_filters.FilterSet):
    length_gte = django_filters.NumberFilter(field_name='length', lookup_expr='gte')
    length_lte = django_filters.NumberFilter(field_name='length', lookup_expr='lte')
    peak_gte = django_filters.NumberFilter(field_name='peak', lookup_expr='gte')
    peak_lte = django_filters.NumberFilter(field_name='peak', lookup_expr='lte')

    class Meta:
        model = Hike
        fields = (
            'name',
            'region',
            'difficulty',
            'terrain',
            'length_gte',
            'length_lte',
            'peak_gte',
            'peak_lte',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-4"),
                Div("region", css_class="col-4"),
                Div("difficulty", css_class="col-4"),
                Div("length", css_class="col-3"),
                Div("peak", css_class="col-3"),
                Div("terrain", css_class="col-3"),
                Div("lowestpoint", css_class="col-3"),
                Div("description", css_class="col-6"),
                Div("header_image", css_class="col-2"),
                css_class="row"
            ),
            ButtonHolder(
                Submit("submit", "Submit", css_class="button")
            )
        )
