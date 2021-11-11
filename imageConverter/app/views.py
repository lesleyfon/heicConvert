
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from .models import Model
from .forms import ImageFileType, UploadFileForm


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

    def post(self, request, **kwargs):
        if request.method == "POST":

            image_file = UploadFileForm(data=request.POST, files=request.FILES)
            image_type = ImageFileType(request.POST)

            # If
            if image_file.is_valid() and image_type.is_valid():
                image_file = request.FILES['image_file']
                image_type = request.POST['image_type']
                image_filename = image_file.name[:-4] + image_type
                converted_image = Model.convertImageTo(image_file, image_type)
                return render(request, 'index.html', {
                    "filename": image_filename})
                print(converted_image, image_filename)

        return render(request, 'index.html')
