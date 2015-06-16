from django import forms

class SentimentForm(forms.Form):
	sample=forms.CharField(widget=forms.Textarea( attrs={'class' :"form-control"}))
	
