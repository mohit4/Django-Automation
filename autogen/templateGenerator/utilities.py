""" templateGenerator utilities.py : utilities to generate template snippet files """

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Development"


import os
from constants import common
from constants import views
from snippets import template_snippets


def generateTemplateDir():
    """ Generate the template directory in project """
    if not os.path.isdir(common.TEMPLATES_DIR_NAME):
        os.mkdir(common.TEMPLATES_DIR_NAME)


def generateTemplateFileNameAndContent(modelName, viewName):
    """ based on the model and view name, generated the name and content for template file """
    templateNamePrefix = modelName.lower()
    if viewName == views.GEN_FILE_VIEWS_CREATE or viewName == views.GEN_FILE_VIEWS_UPDATE:
        return (f"{templateNamePrefix}_form.html", template_snippets.FORM_SNIPPET.format(modelName=modelName))
    elif viewName == views.GEN_FILE_VIEWS_DETAIL or viewName == views.GEN_FILE_VIEWS_DELETE:
        return (f"{templateNamePrefix}_detail.html", template_snippets.DETAIL_SNIPPET.format(modelName=modelName))
    elif viewName == views.GEN_FILE_VIEWS_LIST:
        return (f"{templateNamePrefix}_list.html", template_snippets.LIST_SNIPPET.format(modelName=modelName))


def generateTemplateFiles(appName, modelName, viewsList):
    """ based on the model and views information, return a list of file """
    appTemplateDirPath = os.path.join(common.TEMPLATES_DIR_NAME, appName)
    templateFileName = None
    templateFileContent = None
    for view in viewsList:
        templateFileName, templateFileContent = generateTemplateFileNameAndContent(modelName, view)
        absoluteFileName = os.path.join(appTemplateDirPath, templateFileName)
        if not os.path.exists(absoluteFileName):
            with open(absoluteFileName, 'w') as fobj:
                fobj.write(templateFileContent)


def generateTemplateForViews(appName, viewsInfo):
    """ For the views, generate templates """
    generateTemplateDir()
    appTemplateDirPath = os.path.join(common.TEMPLATES_DIR_NAME, appName)
    if not os.path.isdir(appTemplateDirPath):
        os.mkdir(appTemplateDirPath)
    for modelName in viewsInfo:
        generateTemplateFiles(appName, modelName, viewsInfo[modelName])
