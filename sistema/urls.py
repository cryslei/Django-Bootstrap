from django.urls import path
from sistema.views import RelatorioList
from . import views

urlpatterns = [
    path('',views.redirect),
    path('home/',views.home,name='pagina inicial'),
    path('pesquisa/', RelatorioList.as_view(), name='pesquisa'),
    path('home/relatorio/',views.relatorio_geral,name='relatorio_geral'),
    path('home/relatorio/<int:relatorio_id>/', views.relatorio,name='pdf')
]

   