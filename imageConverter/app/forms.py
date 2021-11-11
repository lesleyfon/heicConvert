from django import forms


IMAGE_TYPES_CHOICES = [
    ('jpeg', 'jpeg'),
    ('png', 'png'),
    ('svg', 'svg'),
    ('gif', 'gif'),
]


# class UploadFileForm(forms.Form):
#     file = forms.FileField()

class UploadFileForm(forms.Form):
    image_file = forms.FileField(required=True)


class ImageFileType(forms.Form):
    image_type = forms.ChoiceField(
        widget=forms.Select, choices=IMAGE_TYPES_CHOICES)
