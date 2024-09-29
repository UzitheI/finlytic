from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, DetailView
# Create your views here
from frontend.models import ContactModel, ChatModel
from .forms import ContactForm, ChatInput
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
class IndexView(CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = 'frontend/index.html'
    success_url = reverse_lazy('frontend:index')

    def form_valid(self, form):
        form.save()  # Save the form data
        return super().form_valid(form)  # Call the parent's form_valid method

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # No need to add the form again; it's already part of the context
        return context

class ChatTemplate(LoginRequiredMixin,CreateView):
    model= ChatModel
    form_class= ChatInput
    template_name='frontend/chatbot.html'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        try:
            print('a')
            self.object.save()

            success_message = "Your input has been received."

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                print('b')
                return JsonResponse({'success': True, 'message': success_message})
            else:
                print('c')
                messages.success(request, success_message)
                return redirect(self.success_url)

        except Exception as e:
            print('d')
            error_message = f"An error occurred: {str(e)}"

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                print('e')
                return JsonResponse({'success': False, 'error': error_message})
            else:
                print('f')
                messages.error(request, error_message)
                return redirect(reverse_lazy('frontend:chatbot'))
    