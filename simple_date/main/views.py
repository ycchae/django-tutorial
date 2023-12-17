import os

from django.http import FileResponse, Http404
from django.shortcuts import render

from .forms import DateTimeForm


def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404


def index(request):
    if request.method == 'POST':
        form = DateTimeForm(request.POST)
        if form.is_valid():
            start_datetime = form.cleaned_data['start_datetime']
            end_datetime = form.cleaned_data['end_datetime']
            # 여기에서 선택한 날짜로 원하는 작업을 수행할 수 있습니다.
            return render(request, 'main/index.html', {'start_datetime': start_datetime, 'end_datetime': end_datetime})
    else:
        form = DateTimeForm()

    return render(request, 'main/index.html', {'form': form})