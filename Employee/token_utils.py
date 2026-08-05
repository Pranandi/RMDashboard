from typing import Any, Dict
from django.core import signing  # type: ignore

# Salt constant to namespace these tokens
_TOKEN_SALT = "employee-session-token"
# Default TTL in seconds (5 minutes)
DEFAULT_TTL = 300


def generate_token(payload: Dict[str, Any], ttl: int = DEFAULT_TTL) -> str:
    """Generate a signed token embedding the payload.

    The token itself does not store the ttl internally (Django signing handles
    timestamp via TimestampSigner embedded in dumps). Validation requires
    specifying the same ttl in `verify_token`.
    """
    return signing.dumps(payload, salt=_TOKEN_SALT)


def verify_token(token: str, ttl: int = DEFAULT_TTL) -> Dict[str, Any]:
    """Verify a token and return its payload.

    Raises signing.BadSignature or signing.SignatureExpired on failure.
    Caller should catch these exceptions.
    """
    return signing.loads(token, max_age=ttl, salt=_TOKEN_SALT)  # type: ignore
