
from .models import Languages, ImageGame
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
import random
from django.http import Http404


class LanguagesAPIView(TemplateView):
    template_name = 'languages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        languages = Languages.objects.all()
        context['languages'] = languages 
        return context


def images_detail_view(request, pk):
    try:
        language = Languages.objects.get(pk=pk)
        images = ImageGame.objects.filter(language_preference=language)
        if images.exists():
            random_image = random.choice(images)
            language_id = language.language_id
            correct_answer = random_image.correct_answer_field
            return render(request, 'image.html', {'image_data': random_image, 'language_id': language_id, 'correct_answer':correct_answer})
        else:
            raise Http404("No images found for this language.")
    except Languages.DoesNotExist:
        raise Http404("Language does not exist.")

def get_next_image(request, pk):
    try:
        language = Languages.objects.get(pk=pk)
        images = ImageGame.objects.filter(language_preference=language)
        if images.exists():
            random_image = random.choice(images)
            return JsonResponse({'image_url': random_image.image.url})
        else:
            return JsonResponse({'error': 'No images found for this language'}, status=404)
    except Languages.DoesNotExist:
        return JsonResponse({'error': 'Language does not exist'}, status=404)