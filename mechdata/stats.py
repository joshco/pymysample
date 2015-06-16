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

class Sentiment():

	def __init__(self):
		self.clf=joblib.load('stats/review-classifier.pkl')
		self.vect=joblib.load('stats/review-vect.pkl')

	def compute(self,sample):
				
			sample_xform= self.vect.transform([sample])
			prediction_raw = self.clf.predict(sample_xform)[0]
			prediction = "Happy" if prediction_raw == 1 else "Sad"

			return prediction

