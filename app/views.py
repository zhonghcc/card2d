from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.models import Card
from random import randint
import qrcode
import os

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the poll index.")
    template =loader.get_template('app/index.html')
    data = ''
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        qq = request.POST.get('qq')
        site = request.POST.get('site')
        company = request.POST.get('company')
        position = request.POST.get('position')

        card = Card(username = username,email = email, tel = tel, qq = qq, site= site, company = company, position= position)
        card.save()
        data += 'BEGIN:VCARD'
        if username:
            data+='\nN:'+username
        if email:
            data+='\nEMAIL:'+email
        if tel:
            data+='\nTEL:'+tel
        if site:
            data+='\nURL:'+site
        data += '\nEND:VCARD'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    filepath = 'app/uploads/'+str(52535782)+'.jpg'
    if data:
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image()
        filename = str(randint(10000000,99999999))
        baseDir = os.path.dirname(os.path.abspath(__file__))
        img.save(baseDir+'/static/app/uploads/'+filename+'.jpg')
        filepath = 'app/uploads/'+filename+'.jpg'

    context = RequestContext(request,{
            'fileName': filepath
        })
    return HttpResponse(template.render(context))


def list(request):
	lastest_cards = Card.objects.all()
	context = {'lastest_cards':lastest_cards}
	return render(request,'app/index.html',context)

def detail(request, card_id):
	return HttpResponse('nihao2')