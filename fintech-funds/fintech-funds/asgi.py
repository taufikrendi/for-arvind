"""
ASGI config for fintech-funds project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os, daemon

from django.core.asgi import get_asgi_application
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
apps.populate(settings.INSTALLED_APPS)

application = get_asgi_application()

from deposits.routers import deposit_router
from loan.routers import loan_router


def get_application() -> FastAPI:
    app = FastAPI(title=settings, debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app = FastAPI(docs_url='/documentations', redoc_url=None)
    app.include_router(deposit_router, tags=["deposit"], prefix="/api/v1/deposit")
    app.include_router(loan_router, tags=["loan"], prefix="/api/v1/loan")
    app.mount("/", WSGIMiddleware(get_wsgi_application()))

    return app


app = get_application()