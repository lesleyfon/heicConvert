
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

            # if image_file.is_valid and image_type.is_valid():
            #     Model.convertImageTo()

        return render(request, 'index.html')
