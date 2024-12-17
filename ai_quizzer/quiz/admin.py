from django.contrib import admin
from .models import Quiz, QuizHistory, Question, Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade_level', 'created_at', 'updated_at')
    search_fields = ('grade_level',)

class QuizHistoryAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student_name', 'score', 'completed_at')
    search_fields = ('student_name',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question_text', 'correct_answer')
    search_fields = ('question_text',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'is_correct')
    search_fields = ('answer_text',)

# Register your models with custom admin
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizHistory, QuizHistoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)