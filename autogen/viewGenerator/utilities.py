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
    baseClasses = DEFAULT_BASE_CLASSES + [ views.UPDATE_VIEW ]
    baseClassList = ", ".join(baseClasses)
    modelFields = getFields(modelInfo)
    return view_snippets.UPDATE_VIEW_TEMPLATE.format(
        modelName=modelName,
        modelFields=modelFields,
        baseClassList=baseClassList,
        appName=appName,
        templatePrefix=modelName.lower()
    )


def generateModelDetailView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model DetailView
    """
    baseClasses = DEFAULT_BASE_CLASSES + [ views.DETAIL_VIEW ]
    baseClassList = ", ".join(baseClasses)
    return view_snippets.DETAIL_VIEW_TEMPLATE.format(
        modelName=modelName,
        baseClassList=baseClassList,
        appName=appName,
        templatePrefix=modelName.lower()
    )


def generateModelListView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model ListView
    """
    baseClasses = DEFAULT_BASE_CLASSES + [ views.LIST_VIEW ]
    baseClassList = ", ".join(baseClasses)
    return view_snippets.LIST_VIEW_TEMPLATE.format(
        modelName=modelName,
        baseClassList=baseClassList,
        appName=appName,
        templatePrefix=modelName.lower()
    )


def generateModelDeleteView(appName, modelName, modelInfo):
    """
    Generate code for Django views.py for Model DeleteView
    """
    baseClasses = DEFAULT_BASE_CLASSES + [ views.DELETE_VIEW ]
    baseClassList = ", ".join(baseClasses)
    return view_snippets.DELETE_VIEW_TEMPLATE.format(
        modelName=modelName,
        baseClassList=baseClassList,
        appName=appName,
        templatePrefix=modelName.lower()
    )


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


def createImportForGenericViews(viewSet):
    """
    Returns a string containing import statement based on the entries present in viewSet
    For : 
    generic.edit - create, update or delete,
    generic.list - list
    generic.detail - detail
    """
    importStatements = []
    genericEditImportClasses = []
    if views.GEN_FILE_VIEWS_CREATE in viewSet:
        genericEditImportClasses.append(views.CREATE_VIEW)
    if views.GEN_FILE_VIEWS_UPDATE in viewSet:
        genericEditImportClasses.append(views.UPDATE_VIEW)
    if views.GEN_FILE_VIEWS_DELETE in viewSet:
        genericEditImportClasses.append(views.DELETE_VIEW)
    if views.GEN_FILE_VIEWS_LIST in viewSet:
        importStatements.append(view_snippets.LIST_VIEW_IMPORT.format(viewNames=views.LIST_VIEW))
    if views.GEN_FILE_VIEWS_DETAIL in viewSet:
        importStatements.append(view_snippets.DETAIL_VIEW_IMPORT.format(viewNames=views.DETAIL_VIEW))
    importStatements.append(view_snippets.EDIT_VIEW_IMPORT.format(viewNames=", ".join(genericEditImportClasses)))
    return common.NEW_LINE.join(importStatements)


def createImportForMixins():
    """
    Return imports with message mixins
    """
    mixinImportList = []
    mixinImportList.append(view_snippets.MESSAGE_MIXIN_IMPORT.format(mixinNames=views.SUCCESS_MESSAGE_MIXIN))
    mixinImportList.append(view_snippets.AUTH_MIXIN_IMPORT.format(mixinNames=views.LOGIN_REQUIRED_MIXIN))
    return common.NEW_LINE.join(mixinImportList)


def generateImports(viewsInfo):
    """
    Analyzes the views for a given app and generate import statements
    """
    resultImportStatements = []
    viewSet = set()
    for modelName in viewsInfo:
        viewSet.update(viewsInfo[modelName])
    resultImportStatements.append(createImportForGenericViews(viewSet))
    resultImportStatements.append(createImportForMixins())
    return common.NEW_LINE.join(resultImportStatements)


def addImportsToFile(appName, importsList):
    """
    Append import statements to a specific app's views file
    """
    viewFileName = os.path.join(appName, common.DJANGO_VIEWS_FILE)
    with open(viewFileName, 'a+') as viewFileObj:
        viewFileObj.write(importsList)
        viewFileObj.write(common.NEW_LINE)


def addAllImportsToFile(appName, viewsInfo):
    """
    Appends basic import statements to app's views file
    """
    addImportsToFile(appName, view_snippets.BASIC_IMPORTS)
    addImportsToFile(appName, view_snippets.MODELS_IMPORT)
    addImportsToFile(appName, generateImports(viewsInfo))
