""" modelGenerator utilities.py : Utilities for model code generation """

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Development"


import os


from snippets import model_snippets
from constants import common


def generateModelField(fieldName, fieldValue):
    """
    Generate a field for model using field name and description
    E.g.
        title = models.CharField(max_length=500)

        Here, fieldName is 'title' and fieldValue is 'CharField(max_length=500)'
    """
    return model_snippets.MODEL_FIELD_TEMPLATE.format(fieldName=fieldName, fieldValue=fieldValue)


def generateModelFields(modelFieldValueMap):
    """
    Generate all the model fields mentioned in the model field map.
    
    Parameters
    ----------
    modelFieldValueMap : dict
        dictionary containing field names along with description
        E.g. "title": "CharField(max_length=500)"
    """
    return "".join([ model_snippets.MODEL_FIELD_TEMPLATE.format(fieldName=key, fieldValue=value) for key, value in modelFieldValueMap.items() ])


def generateModel(modelName, modelFields):
    """
    Generate a model structure using fields and model name.

    Parameters
    ----------
    modelName : str
        name of the django model
    
    modelFields : str
        code for model fields to be appended to model
    """
    return model_snippets.MODEL_TEMPLATE.format(modelName=modelName, modelFields=modelFields)


def addModelToFile(appName, generatedModel):
    """
    Append a generated model to Django app's model file.

    Parameters
    ----------
    appName : str
        name of the django app
    
    generatedModel : str
        string containing model code, to be appended in the app's model file
    """
    modelFileName = os.path.join(appName, common.DJANGO_MODEL_FILE)
    with open(modelFileName, 'a') as modelFileObj:
        modelFileObj.write(generatedModel)


def addModelToAdmin(appName, modelName):
    """
    Appends a model to Django's admin file
    """
    adminFileName = os.path.join(appName, common.DJANGO_ADMIN_FILE)
    with open(adminFileName, 'a') as adminFileObj:
        adminFileObj.write(model_snippets.ADMIN_SITE_REGISTER_TEMPLATE.format(modelName=modelName))
        adminFileObj.write(common.NEW_LINE)


def addImportsToAdmin(appName):
    """
    Append imports to an app's admin file
    """
    adminFileName = os.path.join(appName, common.DJANGO_ADMIN_FILE)
    with open(adminFileName, 'a') as adminFileObj:
        adminFileObj.write(model_snippets.MODELS_IMPORT)
        adminFileObj.write(common.NEW_LINE)