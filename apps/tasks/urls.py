from django.urls import path# type: ignore
from . import api_views

app_name = 'tasks'

urlpatterns = [
    # URLs para categorias
    path('api/adicionar-categoria/', api_views.AddCategoryAPIView.as_view(), name='api_add_category'),
    path('api/listar-categorias/', api_views.ListCategoriesAPIView.as_view(), name='api_list_categories'),
    path('api/editar-categoria/<int:id_category>/', api_views.EditCategoryAPIView.as_view(), name='api_edit_category'),
    path('api/excluir-categoria/<int:id_category>/', api_views.DeleteCategoryAPIView.as_view(), name='api_delete_category'),

    # URLs para tarefas
    path('api/adicionar-tarefa/', api_views.AddTaskAPIView.as_view(), name='api_add_task'),
    path('api/listar-tarefas/', api_views.ListTasksAPIView.as_view(), name='api_list_tasks'),
    path('api/editar-tarefa/<int:id_task>/', api_views.EditTaskAPIView.as_view(), name='api_edit_task'),
    path('api/excluir-tarefa/<int:id_task>/', api_views.DeleteTaskAPIView.as_view(), name='api_delete_task'), 
    ]

