from rest_framework import serializers
from .models import ImageGame, Languages



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields=['id','title']

class ImageGameSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageGame
        fields=['id','language_preference', 'image', 'input_field', 'correct_answer_field' ]