from exceptions.base_exceptions import AnalysisError

class EnvironmentVariableError(AnalysisError): # Base class for errors related to missing environment variable
    pass

class MissingEnvironmentVariableError(EnvironmentVariableError): # Error raised when an environment variable is missing
    pass

class InvalidEnvironmentVariableError(EnvironmentVariableError): # Error raised when an environment variable has an invalid value
    pass

class NotExistEnvironmentVariableError(EnvironmentVariableError): # Error raised when an environment variable does not exist
    pass

class NotSetRequiredEnvironmentVariableError(EnvironmentVariableError): # Error raised when an environment variable is not set
    pass