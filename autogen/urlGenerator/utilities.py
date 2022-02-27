""" urlGenerator utilities.py : Utilities for url code generator """

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Development"


import os

from constants import common
from constants import views
from constants import urls
from snippets import url_snippets


def addContentToFile(appName, content):
    """
    Append import statements to a specific app's url file
    """
    urlFileName = os.path.join(appName, common.DJANGO_URL_FILE)
    with open(urlFileName, 'a+') as urlFileObj:
        urlFileObj.write(content)
        urlFileObj.write(common.NEW_LINE)


def generateImports(appName):
    """
    Generate imports for url file
    """
    statementsList = []
    statementsList.append(url_snippets.PATH_IMPORT)
    statementsList.append(url_snippets.VIEWS_IMPORT)
    statementsList.append(url_snippets.APP_NAME_TEMPLATE.format(appName=appName))
    return common.NEW_LINE.join(statementsList)


VIEW_NAME_MAP = {
    views.GEN_FILE_VIEWS_CREATE: views.CREATE_VIEW,
    views.GEN_FILE_VIEWS_UPDATE: views.UPDATE_VIEW,
    views.GEN_FILE_VIEWS_DETAIL: views.DETAIL_VIEW,
    views.GEN_FILE_VIEWS_DELETE: views.DELETE_VIEW,
    views.GEN_FILE_VIEWS_LIST: views.LIST_VIEW
}


def generateUrlSnippet(modelName, view):
    """
    Based on the type of view, returns a single url pattern code snippet
    """
    viewName = modelName + VIEW_NAME_MAP[view]
    pathName = modelName.lower() + common.PATH_NAME_SEPARATOR + view
    path = modelName.lower() + common.ROUTE_SEPARATOR
    if view == views.GEN_FILE_VIEWS_CREATE:
        path += ( urls.CREATE_PATH + common.ROUTE_SEPARATOR )
    elif view == views.GEN_FILE_VIEWS_UPDATE:
        path += ( urls.DETAIL_PATH + common.ROUTE_SEPARATOR + urls.UPDATE_PATH + common.ROUTE_SEPARATOR )
    elif view == views.GEN_FILE_VIEWS_DELETE:
        path += ( urls.DETAIL_PATH + common.ROUTE_SEPARATOR + urls.DELETE_PATH + common.ROUTE_SEPARATOR )
    elif view == views.GEN_FILE_VIEWS_DETAIL:
        path += ( urls.DETAIL_PATH + common.ROUTE_SEPARATOR )
    return url_snippets.PATH_CB_TEMPLATE.format(path=path, viewName=viewName, pathName=pathName)


def generateUrlPatterns(viewsInfo):
    """
    Generate the url patterns for the django url file
    """
    urlPatterns = []
    for modelName, viewsList in viewsInfo.items():
        for view in viewsList:
            urlPatterns.append( generateUrlSnippet(modelName, view) )
    pathList = common.NEXT_LINE_WITH_INDENT.join( urlPatterns )
    return url_snippets.URL_PATTERNS_TEMPLATE.format(pathList=pathList)

