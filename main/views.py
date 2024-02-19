from django.views.generic import TemplateView
from .templatetags.main_tags import draw_menu

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = draw_menu({'request': self.request}, 'main_menu')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request):
        pass