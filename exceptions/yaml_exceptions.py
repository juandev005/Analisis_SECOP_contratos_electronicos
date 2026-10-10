from .base_exceptions import AnalysisError

class YamlError(AnalysisError):
    pass

class YamlFileError(YamlError):
    pass

class YamlBadFormatError(YamlError):
    pass

class YamlKeyError(YamlError):
    pass

