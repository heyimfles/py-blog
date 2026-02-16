from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentaryForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=True,
        label="Leave a Comment!"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
