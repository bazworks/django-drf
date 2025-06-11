import logging
import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # Log the full exception details
    logger.error(
        "Exception occurred: %s\nContext: %s\nTraceback: %s",
        str(exc),
        context,
        traceback.format_exc(),
    )

    response = exception_handler(exc, context)

    def extract_messages(errors):
        if isinstance(errors, dict):
            messages = []
            for value in errors.values():
                messages.extend(extract_messages(value))
            return messages
        if isinstance(errors, (list, tuple)):
            messages = []
            for item in errors:
                messages.extend(extract_messages(item))
            return messages
        return [str(errors)]

    if response is not None:
        messages = extract_messages(response.data)
        logger.error("DRF handled exception: %s", messages)
        return Response(
            {
                "success": False,
                "message": "An error occurred",
                "errors": messages,
            },
            status=response.status_code,
        )

    messages = extract_messages(exc)
    logger.error("Unhandled exception: %s", messages)
    return Response(
        {
            "success": False,
            "message": "An unexpected error occurred",
            "errors": messages,
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
