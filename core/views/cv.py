import os
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView


class CvPageView(TemplateView):
    template_name = 'cv.html'


def download_file(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'pdf', 'resume.pdf')
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read())
        response['content_type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename=resume.pdf'
        return response
