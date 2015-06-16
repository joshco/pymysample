from django.shortcuts import render,get_object_or_404
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
import numpy as np 

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
	
def sentiment(request):
	print('Loading model...')
	pipeline = joblib.load('stats/review-classifier.pkl')
	vect = joblib.load('stats/review-vect.pkl')
	print('Model loaded!')
	topic="I don't want to do to netroots nation"
	topic_xform= vect.transform([topic])
	prediction_raw = pipeline.predict(topic_xform)[0]
	context = { 'prediction': prediction_raw, 'sample': topic }
	return render(request,'sentiment.html',context)
