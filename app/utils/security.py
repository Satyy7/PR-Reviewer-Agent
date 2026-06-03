import hashlib
import hmac

from app.core.config import settings


def verify_github_signature(
    payload_body: bytes,
    signature_header: str
) -> bool:

    if not signature_header:
        return False

    expected_signature = (
        "sha256="
        + hmac.new(
            settings.github_webhook_secret.encode(),
            payload_body,
            hashlib.sha256
        ).hexdigest()
    )

    return hmac.compare_digest(
        expected_signature,
        signature_header
    )