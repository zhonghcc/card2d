from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.models import Card
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the poll index.")
    template =loader.get_template('app/index.html')
    context = RequestContext(request,{
    		'card':'card'
    	})
    return HttpResponse(template.render(context))


def list(request):
	lastest_cards = Card.objects.all()
	context = {'lastest_cards':lastest_cards}
	return render(request,'app/index.html',context)

def detail(request, card_id):
	return HttpResponse('nihao2')