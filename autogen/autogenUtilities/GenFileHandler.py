""" GenFileHandler.py : Contains Gen file class to manipulate input request file """

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Development"


import yaml


GEN_FILE_PROJECT = "project"
GEN_FILE_APPS = "apps"
GEN_FILE_MODELS = "models"
GEN_FILE_VIEWS = "views"


class GenFile():
    """
    GenFile : A class to efficiently deal with input Gen File
    """
    _inputFileName = None
    _inputYamlFileObj = None

    def __init__(self, inputFileName):
        self._inputFileName = inputFileName
        with open(self._inputFileName, 'r') as _inputFileObj:
            self._inputYamlFileObj = yaml.safe_load(_inputFileObj)
    
    def getInputFileName(self):
        """Returns the input file name of the gen file"""
        return self._inputFileName
    
    def getProjectName(self):
        """Returns a string containing project name"""
        return self._inputYamlFileObj[GEN_FILE_PROJECT]
    
    def getAppList(self):
        """Returns a list of strings containing app names"""
        return self._inputYamlFileObj[GEN_FILE_APPS]
    
    def _contains(self, appName):
        """if appName is present in apps and definitions -> true, else -> false"""
        return appName in self._inputYamlFileObj and appName in self._inputYamlFileObj[GEN_FILE_APPS]

    def getModels(self, appName):
        """Returns a map containing models if app is defined"""
        if self._contains(appName):
            return self._inputYamlFileObj[appName][GEN_FILE_MODELS]

    def getViews(self, appName):
        """Returns a map containing model views if app is defined"""
        if self._contains(appName):
            return self._inputYamlFileObj[appName][GEN_FILE_VIEWS]
