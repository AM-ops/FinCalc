from django.views.generic import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'
#    def __init__(self, arg):
#        super(HomePage, self).__init__()
#        self.arg = arg

class TestPage(TemplateView):
    # """docstring for TestPage."""
    #
    # def __init__(self, arg):
    #     super(TestPage, self).__init__()
    #     self.arg = arg
    template_name = 'test.html'

class ThanksPage(TemplateView):
    # """docstring for ThanksPage."""
    #
    # def __init__(self, arg):
    #     super(ThanksPage, self).__init__()
    #     self.arg = arg
    template_name = 'thanks.html'

class ContactPage(TemplateView):
    # """docstring for ThanksPage."""
    #
    # def __init__(self, arg):
    #     super(ThanksPage, self).__init__()
    #     self.arg = arg
    template_name = 'contact.html'

def handler404(request, exception):
       return render(request, '404.html')
