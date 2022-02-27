""" view_snippets.py : contains code templates and snippets for views """

EDIT_VIEW_IMPORT = "from django.views.generic.edit import {viewNames}"
LIST_VIEW_IMPORT = "from django.views.generic.list import {viewNames}"
DETAIL_VIEW_IMPORT = "from django.views.generic.detail import {viewNames}"

MESSAGE_MIXIN_IMPORT = "from django.contrib.messages.views import {mixinNames}"
AUTH_MIXIN_IMPORT = "from django.contrib.auth.mixins import {authMixins}"

BASIC_IMPORTS = """
from django.urls.base import reverse_lazy
from django.db.models import Q
from django.contrib import messages
"""

APP_MODEL_IMPORT = "from .models import {modelName}"

CREATE_VIEW_TEMPLATE = """
class {modelName}CreateView({baseClassList}):
    '''
    Creating a new {modelName}
    '''
    template_name = '{appName}/{templatePrefix}_form.html'
    model = {modelName}
    fields = {modelFields}
    success_message = 'New {modelName} added!'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Create new {modelName}'
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
"""

UPDATE_VIEW_TEMPLATE = """
class {modelName}UpdateView({baseClassList}):
    '''
    Updating existing {modelName}
    '''
    template_name = '{appName}/{templatePrefix}_form.html'
    model = {modelName}
    fields = {modelFields}
    success_message = '{modelName} updated!'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Update {modelName}'
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
"""

LIST_VIEW_TEMPLATE = """
class {modelName}ListView({baseClassList}):
    '''
    Listing all the {modelName}s present in database
    '''
    template_name = '{appName}/{templatePrefix}_list.html'
    model = {modelName}
    context_object_name = '{templatePrefix}s'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Listing all {modelName}s'
        return context
"""

DETAIL_VIEW_TEMPLATE = """
class {modelName}DetailView({baseClassList}):
    '''
    Printing details of a single {modelName}
    '''
    template_name = '{appName}/{templatePrefix}_detail.html'
    model = {modelName}
    context_object_name = '{templatePrefix}'

    login_url = '/'
"""

DELETE_VIEW_TEMPLATE = """
class {modelName}DeleteView({baseClassList}):
    '''
    Deleting an existing {modelName}
    '''
    template_name = '{appName}/{templatePrefix}_detail.html'
    model = {modelName}
    context_object_name = {templatePrefix}
    success_url = reverse_lazy('{appName}:{templatePrefix}-list')
    success_message = '{modelName} deleted!'

    login_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super({modelName}DeleteView, self).delete(request, *args, **kwargs)
"""