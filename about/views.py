from django.views.generic import TemplateView

from .models import About

class AboutView(TemplateView):
    model = About
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()[0]

        return context
