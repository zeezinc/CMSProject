from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import model_form_upload, loginPage, registerPage, logoutUser, home_view, item_list, \
    item_delete, search_contents, show_content, item_form

app_name = 'AuthorCourses'

urlpatterns = [
    path('', home_view, name='home'),
    path('upload/', model_form_upload, name='upload'),
    path('upload/', model_form_upload, name='upload'),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('insert/', item_form, name='item_insert'),  # get and post req. for insert operation
    path('<int:id>/', item_form, name='item_update'),  # get and post req. for update operation
    path('delete/<int:id>/', item_delete, name='item_delete'),  # get req. for update operation
    path('list/', item_list, name='item_list'),  # get and post req. for display operation

    path('show_content/<content_id>', show_content, name='show_content'),
    path('search_contents/', search_contents, name='search_contents'),
]

if settings.DEBUG:  # To allow us to view the documents
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
