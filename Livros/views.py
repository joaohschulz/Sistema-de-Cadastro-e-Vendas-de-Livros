from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic import CreateView , ListView
from django.urls import reverse_lazy
from .forms import InsereLivroForms
from .models import Livro
from django.contrib.auth.mixins import LoginRequiredMixin



class BaseView(ListView):
    template_name = 'LivrosBase.html'
    model = Livro
    context_object_name = 'livros'
class InsereLivrosView(CreateView):
    model = Livro
    form_class = InsereLivroForms
    template_name = 'Livro.html'
    success_url = reverse_lazy('livrocadastrado')
    
    # validacao de formulario valido
    def form_valid(self, form):
        response = super().form_valid(form) # salva o livro cadastrado
        self.request.session['livrocadastrado'] = True # libera a pagina que vai dar sucesso
        return response
 
class LivroCadastradoView(LoginRequiredMixin, TemplateView):
    template_name = 'LivroCadastrado.html'

    def dispatch(self, request, *args, **kwargs):
        # pop le uma vez só, nao permitindo que acesse se nao tiver feito cadastro
        if not request.session.pop('livrocadastrado', False):
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)