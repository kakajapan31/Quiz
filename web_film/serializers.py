from rest_framework import serializers
from .models import Question, Choice

class Question_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text')

class Choice_serializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text')
