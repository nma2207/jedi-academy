from django.shortcuts import render, get_object_or_404
from .forms import CandidateForm
from django.shortcuts import redirect
from .forms import JediForm
from .models import Jedi
from .models import Candidate
from django.urls import reverse
from .forms import TestTaskForm
from .models import  Test
from .models import Answer
from django.forms.formsets import formset_factory
from django.core.mail import send_mail

def start(request):
    return render(request, 'jedies/start.html', {})
# Create your views here.


def candidate_list(request):
    jedi_id = request.session['jedi_id']
    #print('candidate list')
    jedi = Jedi.objects.get(pk=jedi_id)
    candidates = Candidate.objects.filter(planet=jedi.planet)
    return render(request, 'jedies/candidate_list.html', {'list':candidates})

def jedi_page(request):
    if request.method == 'POST':
        form = JediForm(request.POST)
        if form.is_valid():

            #print(form.data['name'])
            #jedi = Jedi.objects.get(pk = form.data['name'])
            request.session['jedi_id'] = form.data['name']

            #print(jedi.name)
            #candidate = form.save(commit=False)
            #candidate.save()
            #print('redirect to list')
            return redirect('candidate_list')
    else:
        form = JediForm()
    return render(request, 'jedies/jedi.html', {'form':form})

def candidate_page(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():

            candidate = form.save(commit=False)
            candidate.save()
            request.session['candidate_id'] = candidate.pk
            return redirect('test_task')
    else:
        form = CandidateForm()
    return render(request, 'jedies/candidate.html', {'form':form})

def test_task(request):
    #print('PK', request.session['candidate_id'])
    candidate = Candidate.objects.get(pk=request.session['candidate_id'])
    questions = Test.objects.filter(planet=candidate.planet)

    # data = []
    # for question in questions:
    #     data.append({'question':question.question})
    #print(data)
    Formset = formset_factory(TestTaskForm,min_num=len(questions), max_num=len(questions))
    if request.method == 'POST':


        forms = Formset(request.POST)
        if forms.is_valid():

            for i in range(len(questions)):

                #print(form.cleaned_data)
                    #candidate = form.save(commit=False)
                    #candidate.save()
                Answer.objects.create(candidate=candidate, question=questions[i], answer = forms[i].cleaned_data['answer'])
        return redirect('start')
    else:
        forms = Formset()
        for i in range(len(questions)):
            forms[i].fields['answer'].label = questions[i].question
    return render(request, 'jedies/test_task.html', {'form':forms})

def candidate_detail(request, pk):
    print("candidate detail", pk)
    candidate = get_object_or_404(Candidate, pk=pk)
    answers = Answer.objects.filter(candidate=candidate)
    return render(request, 'jedies/candidate_detail.html', {'candidate':candidate, 'answers':answers})

def send_mail_to_padawan(candidate):



    data = candidate.name+""",
    Ты зачислен в падаваны!
    """
    #send_mail('Welcome!', data, "Yasoob",
     #         [candidate.email], fail_silently=False)

def to_padawan(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    send_mail_to_padawan(candidate)
    candidate.delete()
    return redirect('candidate_list')

