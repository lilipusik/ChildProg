import ast
import json
import sys
import subprocess
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from school.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def all_reviews(request):
    reviews = Reviews.objects.select_related('user').all()
    return render(request, 'InfinitySchool/all_reviews.html', {'reviews': reviews})

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@csrf_exempt
def code_checker(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            language = data.get('language')
            code = data.get('code')
            result_message = ""

            task_id = request.GET.get('task_id')
            task = get_object_or_404(PracticeTasks, id=task_id)
            expected_answer = task.answer.strip()

            if language == 'python':
                try:
                    # Check if code is syntactically correct
                    ast.parse(code)
                    process = subprocess.Popen(
                        [sys.executable, '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                    stdout, stderr = process.communicate()
                    output = stdout.decode('utf-8').strip()
                    error_output = stderr.decode('utf-8').strip()

                    if error_output:
                        result_message = f'Error in execution: {error_output}'
                    elif output == expected_answer:
                        result_message = f'Ваш ответ: {output}\nЗадача решена! Поздравляем! 🎉'
                    else:
                        result_message = f'Ваш ответ: {output}\nК сожалению, это неправильно.\nНе отчаивайтесь! Попробуйте еще раз.'
                except SyntaxError as e:
                    result_message = f"Ошибка синтаксиса Python: {str(e)}"
                except Exception as e:
                    result_message = f"Error during code execution: {str(e)}"

            response_data = {
                'message': result_message
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)

    # Handling GET requests
    course_id = request.GET.get('course_id')
    task_id = request.GET.get('task_id')
    course = get_object_or_404(Courses, id=course_id)
    task = get_object_or_404(PracticeTasks, id=task_id)

    return render(request, 'InfinitySchool/task.html', {'course': course, 'task': task})


def index(request):
    context = {
        'title': 'InfinityCode',
        'courses': Courses.objects.all()[:3],
        'reviews': Reviews.objects.order_by('-rating')[:2]
    }
    return render(request, 'InfinitySchool/main_page.html', context)


def catalog(request):
    courses = Courses.objects.all()
    liked_courses = []
    if request.user.is_authenticated:
        liked_courses = Like.objects.filter(user=request.user).values_list('course_id', flat=True)
    
    context = {
        'courses': courses,
        'liked_courses': liked_courses,
    }
    return render(request, 'InfinitySchool/catalog.html', context)

@login_required
def toggle_like(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    like, created = Like.objects.get_or_create(user=request.user, course=course)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked})

def course_detail(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    theories = course.theories.all()
    if course.name != "Полный курс изучения Python":
        return render(request, 'InfinitySchool/course_in_development.html')

    theories = course.theories.all()
    return render(request, 'InfinitySchool/course_detail.html', {'course': course, 'theories': theories})




def execute_code(code):
    try:
        exec_locals = {}
        exec(code, globals(), exec_locals)
        res = exec_locals.get("result")

    except Exception as e:
        return str(e)
    
#def send_review(request):
#   return render(request, 'InfinitySchool/send_review.html')

@login_required
def send_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')
        user = request.user

        # Создание нового отзыва
        Reviews.objects.create(user=user, rating=rating, review=review_text)

    return render(request, 'InfinitySchool/send_review.html')
