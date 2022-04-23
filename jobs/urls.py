from django.urls import path
from . import views


urlpatterns = [
    path('jobs/', views.JobsView, name='jobs'),
    path('jobs/encontrar_jobs/', views.Encontrar_Jobs, name='encontrar_jobs'),
    path('jobs/aceitar_job/<int:id>/', views.Aceitar_job, name="aceitar_job"),
    path('jobs/perfil/', views.Perfil, name="perfil"),
    path('jobs/enviar_projeto/', views.Enviar_projeto, name="enviar_projeto")
]
