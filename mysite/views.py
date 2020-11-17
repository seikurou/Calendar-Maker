from django.http import HttpResponse, JsonResponse, FileResponse
from wsgiref.util import FileWrapper
import json
from .cal_maker.main import make_calendar, OUTPUT_DIR
import time, os


class Arg:
    def __init__(self, params):
        self.template = params['template']
        self.year = params['year']
        self.month = params['month']
        self.day = params['day']
        self.cnt = params['cnt']
        self.start_day = params['start_day']
        self.filename = 'calendar' + (str)((int)(time.time()*1000)) + '.docx'
        

def make_calendar_view(request):
    try:
        params = json.loads(request.body)
        args = Arg(params)
        make_calendar(args)
    except Exception:
        return HttpResponse("Invalid arguments.", status=406)
    return JsonResponse({"link":args.filename})

def get_file(request, file_name):
    # return HttpResponse("File.")
    fpath = OUTPUT_DIR + file_name
    # file = open(fpath, 'r') 
    f = open(fpath, 'rb')
    response = FileResponse(f)
    response['Content-Disposition'] = "attachment; filename=%s" %file_name
    response['Content-Length'] = os.path.getsize(fpath)
    return response

 
# def download_file(request):
#     # fill these variables with real values
#     fl_path = ‘/file/path'
#     filename = ‘downloaded_file_name.extension’

#     fl = open(fl_path, 'r’)
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#         return response

