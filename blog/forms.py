from django import forms
from django.forms import ModelForm
from blog.models import Spy, Agent, Asset


class SpyForm(ModelForm):
    class Meta:
        model = Spy
        fields = ['first_name', 'last_name', 'code_name', 'spy_id', 'emp_id']


class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'code_name', 'agent_id', 'emp_id']


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['first_name', 'last_name', 'code_name', 'asset_id', 'spy_id']
