from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QuizForm

def quiz(request):
    if request.method == 'POST':
        quizform = QuizForm(request.POST)
        if quizform.is_valid():
            ans1 = request.POST.get('question1')
            ans2 = request.POST.get('question2')
            ans3 = request.POST.get('question3')
            ans4 = request.POST.get('question4')
            ans5 = request.POST.get('question5')
            score = 0
            if ans1 == 'All of the above':
                score += 1
            if ans2 == 'No':
                score += 1
            if ans3 == 'https':
                score += 1
            if ans4 == 'Yes':
                score += 1
            if ans5 == 'By checking their FULL email address':
                score += 1
            messages.success(request, f"Your score is {score}/5")
            return redirect('completed')
        else:
            messages.error(request, 'Please answer all the questions.')


    quizform = QuizForm()
    context = {'quizform': quizform}

    return render(request, 'quiz/quiz.html', context)

def completed(request):
    return render(request, 'quiz/completed.html')