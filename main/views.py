from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from itertools import chain
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from accounts.models import CustomUser
from .models import Room

def index(request):

    return render(request, 'html/index.html')

def rules(request):

    return render(request, 'html/rules.html')

def MyRooms(request):
    rooms = Room.objects.all()
    return render(request, 'html/User_room.html', {'rooms': rooms})

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ["title", "adres",  "usphone",  "discript", ]
    template_name = "html/room_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Room
    template_name = "room_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        return self.get_object().author == self.request.user


class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Room
    template_name = "room_delete.html"
    success_url = reverse_lazy("main")

    def test_func(self):
        return self.get_object().author == self.request.user


class PostView(DetailView):
    model = Room

    template_name = "html/room_details.html"



class SearchView(View):
    template_name = 'html/map.html'

    def get(self, request, *args, **kwargs):
        context = {}

        q = request.GET.get('q')
        if q:
            query_sets = []  # Общий QuerySet

            # Ищем по всем моделям
            query_sets.append(Room.objects.search(query=q))


            # и объединяем выдачу
            final_set = list(chain(*query_sets))

            context['last_question'] = '?q=%s' % query_sets

            paginator = Paginator(final_set, 2)

            page = request.GET.get('page')

            try:
                context['object_list'] = paginator.page(page)
            except PageNotAnInteger:
                context['object_list'] = paginator.page(1)
            except EmptyPage:
                context['object_list'] = paginator.page(paginator.num_pages)
        return render(request=request, template_name=self.template_name, context=context)


