from exceptions.base_exceptions import AnalysisError

class SecopError(AnalysisError):
    """Base de todos los errores relacionados con el SECOP."""

class SecopNotRespondingError(SecopError):
    """La url base de la api no responde."""

class SecopDataBaseNotRespondingError(SecopError):
    """La url base de la api no responde."""

class SecopTokenNotValidError(SecopError):
    """La url base de la api no responde."""