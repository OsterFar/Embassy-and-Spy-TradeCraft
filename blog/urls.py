from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('19Q2o85a51GPsEtrx/', views.terminal, name='terminal'),
    path('19Q2o85a51GPsEtrx/5p23xqs/', views.spycraft, name='spycraft'),
    path('19Q2o85a51GPsEtrx/5p23xqs/spies', views.spies, name='spies'),
    path('19Q2o85a51GPsEtrx/5p23xqs/agents', views.agents, name='agents'),
    path('19Q2o85a51GPsEtrx/5p23xqs/assets', views.assets, name='assets'),
    path('19Q2o85a51GPsEtrx/5p23xqs/modify', views.modify, name='modify'),
    path('19Q2o85a51GPsEtrx/5p23xqs/encode', views.encode, name='encode'),
    path('19Q2o85a51GPsEtrx/5p23xqs/decode', views.decode, name='decode'),
    path('19Q2o85a51GPsEtrx/5p23xqs/dasset', views.del_asset, name='dasset'),
    path('19Q2o85a51GPsEtrx/5p23xqs/iasset', views.iasset, name='iasset'),
    path('19Q2o85a51GPsEtrx/5p23xqs/dagent', views.del_agent, name='dagent'),
    path('19Q2o85a51GPsEtrx/5p23xqs/iagent', views.iagent, name='iagent'),
    path('19Q2o85a51GPsEtrx/5p23xqs/dspy', views.del_spy, name='dspy'),
    path('19Q2o85a51GPsEtrx/5p23xqs/ispy', views.ispy, name='ispy'),
    path('19Q2o85a51GPsEtrx/5p23xqs/dspy/<spy_id>/', views.delete_spy, name='delete_spy'),
    path('19Q2o85a51GPsEtrx/5p23xqs/dagent/<agent_id>/', views.delete_agent, name='delete_agent'),
    path('19Q2o85a51GPsEtrx/5p23xqs/dasset/<asset_id>/', views.delete_asset, name='delete_asset'),
]
