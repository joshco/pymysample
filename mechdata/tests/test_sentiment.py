from django.test import TestCase
from mechdata.stats import Sentiment
import logging
logger=logging.getLogger('test')

class SentimentTestCase(TestCase):
    def test_sentiment(self):
        sample="This is a great app"
        clf=Sentiment()
        prediction=clf.compute(sample)
        # should be "Happy"
        logger.debug("SentimentTestCase sample: %s result: %s" % (sample,prediction))
        self.assertEqual(prediction,"Happy")
