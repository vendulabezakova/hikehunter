from django.forms import ModelForm, ValidationError, CharField
from hikehunter.models import Hike
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, ButtonHolder, Submit
from ckeditor.widgets import CKEditorWidget

class HikeForm(ModelForm):
    description = CharField(widget=CKEditorWidget())

    class Meta:
        model = Hike
        fields = ("name", "region", "difficulty", "length", "peak", "terrain", "lowestpoint", "description", "header_image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div("name", css_class="col-6"),
                Div("region", css_class="col-6"),
                Div("difficulty", css_class="col-4"),
                Div("length", css_class="col-4"),
                Div("peak", css_class="col-4"),
                Div("terrain", css_class="col-4"),
                Div("lowestpoint", css_class="col-4"),
                Div("header_image", css_class="col-4"),
                Div("description", css_class="col-12"),
                css_class="row"
            ),
            ButtonHolder(
                Submit("submit", "Submit", css_class="button")
            )
        )

class RegisterUserForm(UserCreationForm):
    username = CharField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

