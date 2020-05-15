from django.shortcuts import render
# Create your views here.
from purchase.models import Learnbook, Tutor, Category
from django.views import generic
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_learnbooks = Learnbook.objects.all().count()

    # The 'all()' is implied by default.
    num_tutors = Tutor.objects.count()

    num_categories = Category.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_learnbooks': num_learnbooks,
        'num_tutors': num_tutors,
        'num_categories': num_categories,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class LearnbookListView(generic.ListView):
    model = Learnbook
    paginate_by = 10


class LearnbookDetailView(generic.DetailView):
    model = Learnbook


class TutorListView(generic.ListView):
    model = Tutor
    paginate_by = 10


class TutorDetailView(generic.DetailView):
    model = Tutor
