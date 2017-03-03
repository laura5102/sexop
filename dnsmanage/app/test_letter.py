from django.template import Template, Context
from django.http import HttpResponse
import datetime

def re_letter(request):
    now = datetime.datetime.now()
    # Simple way of using templates from the filesystem.
    # This doesn't account for missing files!
    #fp = open('F:/PycharmProjects/dnsmanage/templates/letter.html')
    fp = open('F:/PycharmProjects/dnsmanage/templates/letter.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'person_name': 'John Smith',
                             'product': 'Super Lawn Mower',
                             'company': 'Outdoor Equipment',
                             #'ship_date': datetime.date(2009, 4, 2),
                             'ship_date': datetime.datetime.now(),
                             'ordered_warranty': True}))
    return HttpResponse(html)
