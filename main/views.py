from django.views.generic import CreateView
from .models import Contact
from textblock.models import TextBlock

class IndexView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    template_name = 'index.html'
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context