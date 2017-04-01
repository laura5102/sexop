from django.template import Template, Context
from django.http import HttpResponse

def analysis_file(request):
    fp = open('F:/PycharmProjects/dnsmanage/templates/server_manage.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'user': 'John Smith',
                             'worker_processes': 'Super Lawn Mower',
                             'error_log': 'Outdoor Equipment',
                             'pid': 'pid',
                             'events': 'eventslog',
                             'http': 'http'}))
    return HttpResponse(html)
