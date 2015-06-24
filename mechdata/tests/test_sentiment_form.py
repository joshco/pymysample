from django_webtest import WebTest
import logging
logger=logging.getLogger('test')

class SentimentFormTestCase(WebTest):
    def testForm(self):
        page=self.app.get('/sentiment')
        form=page.form

        page.mustcontain('Enter Sample')
        sample = 'This is a great app!'
        form['sample']= sample

        response=form.submit()
        logger.debug("SentimentFormTestCase sample: %s result: %s" % (sample,response.context['prediction']))
        self.assertEqual(response.context['prediction'], "Happy")

