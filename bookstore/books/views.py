from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
     model = Book
     context_object_name ="book"
     template_name = "books/book_detail.html"
     permission_required = 'books.special_status' #

class SearchResultsListView(ListView):
     model = Book
     context_object_name = 'book_list'
     template_name = 'books/search_result.html'

     def get_queryset(self):
          q = self.request.GET.get('q')
          return Book.objects.filter(
          Q(title__icontains=q) | Q(author__icontains=q)
          )
      
     
     