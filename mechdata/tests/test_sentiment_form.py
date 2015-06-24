from django_webtest import WebTest

class SentimentFormTestCase(WebTest):
    def testForm(self):
        page=self.app.get('/sentiment')
        form=page.form

        page.mustcontain('Enter Sample')
        form['sample']='This is a great app!'
        response=form.submit()
        self.assertEqual(response.context['prediction'], "Happy")

