from django.conf import settings
from django.conf.urls import url
from .api import StoreCategoriesView, CategorySubCategoriesView

app_name = "categories"

store_categories_urls = [
    url(r'^$', StoreCategoriesView.as_view(), name='store-categories'),
    
]

categories_urls =[

    url(r'^(?P<id>\d+)/subcategories/',  CategorySubCategoriesView.as_view() ,name="category-subcategories" ),
    

]
