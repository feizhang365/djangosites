"""
views
"""
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
# from django.template import loader
from .models import Choice, Question


# def index(request):
#     """
#     index page.
#     """
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     """
#      detail page view
#     """
#     # return HttpResponse("You're looking at question %s. detail" % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     """
#     result page view
#     """
#     response = "You're looking at the results of question %s. result"
#     return HttpResponse(response % question_id)

### define index and view
class IndexView(generic.ListView):
    """
    index view
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    """
    detail view
    """
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    """
    result view
    """
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    """
    vote page view
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
