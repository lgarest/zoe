from django.views.generic import CreateView, TemplateView
from .models import Contact
from textblock.models import TextBlock

class IndexView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    template_name = 'home.html'
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context

class ZOEhubView(TemplateView):

    template_name = "zoehub.html"

    def get_context_data(self, **kwargs):
        context = super(ZOEhubView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context


class ZOEaiView(TemplateView):

    template_name = "zoeai.html"

    def get_context_data(self, **kwargs):
        context = super(ZOEaiView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context


class UsesView(TemplateView):

    template_name = "uses.html"

    def get_context_data(self, **kwargs):
        context = super(UsesView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context