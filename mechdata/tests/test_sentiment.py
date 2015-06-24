from django.test import TestCase
from mechdata.stats import Sentiment

class SentimentTestCase(TestCase):
    def test_sentiment(self):
        sample="This is a great app"
        clf=Sentiment()
        prediction=clf.compute(sample)
        # should be "Happy"
        self.assertEqual(prediction,"Happy")
