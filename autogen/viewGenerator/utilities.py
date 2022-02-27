""" viewGenerator utilities.py : Utilities for view code generation """

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Development"


import os

from snippets import view_snippets
from constants import views
from constants import common


DEFAULT_BASE_CLASSES = [views.LOGIN_REQUIRED_MIXIN, views.SUCCESS_MESSAGE_MIXIN]

def getFields(modelInfo):
    template = "'{fieldName}', "
    result = ""
    for field in modelInfo.keys():
        result += template.format(fieldName=field)
    return "( " + result + " )"


def generateModelCreateView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model CreateView
    """
    baseClasses = DEFAULT_BASE_CLASSES + [ views.CREATE_VIEW ]
    baseClassList = ", ".join(baseClasses)
    modelFields = getFields(modelInfo)
    return view_snippets.CREATE_VIEW_TEMPLATE.format(
        modelName=modelName,
        modelFields=modelFields,
        baseClassList=baseClassList,
        appName=appName,
        templatePrefix=modelName.lower()
    )


def generateModelUpdateView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model UpdateView
    """
    pass


def generateModelDetailView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model DetailView
    """
    pass


def generateModelListView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model ListView
    """
    pass


def generateModelDeleteView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model DeleteView
    """
    pass


def generateModelSearchView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model search
    """
    pass


SWITCHER = {
    views.GEN_FILE_VIEWS_CREATE: generateModelCreateView,
    views.GEN_FILE_VIEWS_UPDATE: generateModelUpdateView,
    views.GEN_FILE_VIEWS_LIST: generateModelListView,
    views.GEN_FILE_VIEWS_DETAIL: generateModelDetailView,
    views.GEN_FILE_VIEWS_DELETE: generateModelDeleteView,
    views.GEN_FILE_VIEWS_SEARCH: generateModelSearchView
}


def generateView(appName, modelName, modelInfo, viewName):
    """
    Generate code for Django views.py against the mentioned model
    """
    return SWITCHER.get(viewName)(appName, modelName, modelInfo)


def generateViewsForModel(appName, modelName, modelInfo, viewsList):
    """
    Iterate over views list and generate code for all of them
    """
    resultCodeSnippet = ""
    for view in viewsList:
        resultCodeSnippet += generateView(appName, modelName, modelInfo, view)
    return resultCodeSnippet


def addViewsToFile(appName, generatedViews):
    """
    Append generate views to Django app's views file
    """
    viewFileName = os.path.join(appName, common.DJANGO_VIEWS_FILE)
    with open(viewFileName, 'a') as viewFileObj:
        viewFileObj.write(generatedViews)


def addImportsToFile(appName, importsList):
    """
    Append import statements to a specific app's views file
    """
    pass
