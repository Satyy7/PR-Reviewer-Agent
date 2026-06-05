from celery import Celery

celery_app = Celery(
    "ai_pr_reviewer",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",

    timezone="UTC",
    enable_utc=True,

    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=None,

    worker_prefetch_multiplier=1,
    task_track_started=True,
    task_acks_late=True,

    result_expires=3600
)