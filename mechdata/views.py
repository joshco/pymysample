
# Create your views here.
from .models import Folk
from .forms import *
from .stats import *
from .datamover import Osdi
from django.conf import settings
import logging
from django.contrib.auth import logout as auth_logout

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render(request,'main.html', {})

logger=logging.getLogger('django')

from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    print "looking4 ", dictionary, " with ", key
    return dictionary.get(key)


def index(request):
    folks_list = Folk.objects.order_by('-updated_at')
    context = {'folks_list': folks_list}
    return render(request, 'folks/index.html', context)

def detail(request,folk_id):
	folk=get_object_or_404(Folk,pk=folk_id)
	context = {'folk' : folk}
	return render(request,'folks/detail.html',context)
	
def sentiment(request):
	context={}
	context['form']= SentimentForm()
	logger.debug("view/sentiment")

	if request.method =='POST':
		form=SentimentForm(request.POST)
		if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
                        
			sample=form.cleaned_data['sample']
			
			sentiment=Sentiment()
			prediction=sentiment.compute(sample)
			context['prediction']=prediction
			context['sample']= sample[0:50] + '...'
			logger.debug("Manual Sentiment: %s result: %s" % (sample,prediction))
		

	return render(request,'sentiment.html',context)

def main(request):
	return render(request,'main.html')

def sync(request):
	return render(request,'sync.html')

def syncresults(request):
	token=settings.OSDI_TOKEN
	aep=settings.OSDI_AEP
	osdi=Osdi(aep,token)
	results=osdi.sync()
	logger.debug("OSDI sync got {} results".format(len(results)))
	classifier=Sentiment()

	converted_results=[]
	for person in results:
		sample= person.get('custom_fields').get('sentence')
		try:
			sentiment=classifier.compute(sample)

		except:
			sentiment='n/a non-ascii'

		c={
		  'name' : person.get('given_name') + " " + person.get('family_name'),
		  'sample' : sample,
		  'mobile' : person.get('mobile'),
		  'sentiment' : sentiment
		}
		converted_results.append(c)
	context = { 'results': converted_results}
	return render(request,'syncresults.html',context)
