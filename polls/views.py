from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Folk


def index(request):
    folks_list = Folk.objects.order_by('-updated_at')
    context = {'folks_list': folks_list}
    return render(request, 'folks/index.html', context)

def detail(request,folk_id):
	folk=get_object_or_404(Folk,pk=folk_id)
	context = {'folk' : folk}
	return render(request,'folks/detail.html',context)
