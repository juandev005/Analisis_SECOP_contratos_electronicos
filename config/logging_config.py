from pathlib import Path
import json
import logging
import logging.config
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"

load_dotenv(BASE_DIR / ".env")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

APP_LOGGER = "APP_NAME"


# Clase para formatear los logs en JSON
class JsonFormatter(logging.Formatter):

    def format(self, record):
        data = {
            "ts": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "func": record.funcName,
            "line": record.lineno,
            "msg": record.getMessage(),
        }

        if record.exc_info:
            data["exception"] = self.formatException(record.exc_info)

        return json.dumps(data, ensure_ascii=False, default=str)

# Función para configurar los handlers rotativos de los logs
def _rotativo( name, level, formatter, size=5242880, backups=5):
    return {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": str(LOG_DIR / name),
        "maxBytes": size ,
        "backupCount": backups,
        "encoding": "utf-8",
        "level": level,
        "formatter": formatter,
    }

# Objetos de configuración centralizados de los logs
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "consola": {
            "format": "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            "datefmt": "%H:%M:%S",
        },
        "detallado": {
            "format": "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s",
        },
        "json": {"()": JsonFormatter},
    },

    "handlers": {
        "consola": {
            "class": "logging.StreamHandler",
            "level": LOG_LEVEL,
            "formatter": "consola",
        },
        "archivo": _rotativo("secop.log", "DEBUG", "detallado"),
        "errores": _rotativo("errores.log", "ERROR", "detallado"),
        "json": _rotativo("secop.json", "DEBUG", "json"),
    },

    "loggers": {
        APP_LOGGER: {
            "level": "DEBUG",
            "handlers": ["consola", "archivo", "errores", "json"],
            "propagate": False,
        },
    },

    "root": {
        "level": "WARNING",
        "handlers": ["consola", "errores"],
    },
}

# Variable global para controlar la configuración
_configurado = False

# Función principal para inicilizar la configuración
def setup_logging():
    global _configurado

    if _configurado:
        return

    LOG_DIR.mkdir(exist_ok=True)
    logging.config.dictConfig(LOGGING)
    _configurado = True