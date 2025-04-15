import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from pythonjsonlogger.json import JsonFormatter

from src.config import settings


class CustomJsonFormatter(JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            timestamp = datetime.now(ZoneInfo("Europe/Moscow")).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            log_record["timestamp"] = timestamp
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname
        # Remove taskName
        if log_record.get("taskName") is None:
            log_record.pop("taskName", None)


formatter = CustomJsonFormatter(
    "%(timestamp)s %(level)s %(message)s %(module)s %(funcName)s"
)

logger = logging.getLogger()
logHandler = logging.StreamHandler()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(settings.logger.level)
