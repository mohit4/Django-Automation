""" url_snippets.py : contains code snippets for django url file """

PATH_IMPORT = "from django.urls import path"
VIEWS_IMPORT = "from .views import *"

APP_NAME_TEMPLATE = """
app_name = '{appName}'
"""

PATH_CB_TEMPLATE = "path('{path}', {viewName}.as_view(), name='{pathName}'),"

URL_PATTERNS_TEMPLATE = """
urlpatterns = [
    {pathList}
]
"""