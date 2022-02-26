""" model_snippets.py : contains code templates and snippets for models """

MODEL_FIELD_TEMPLATE = "{fieldName} = models.{fieldValue}\n    "

MODEL_TEMPLATE = """
class {modelName}(models.Models):
    '''
    This model is generated by Django-AutoGen 
    '''
    {modelFields}
    def __str__(self):
        return self.pk
"""