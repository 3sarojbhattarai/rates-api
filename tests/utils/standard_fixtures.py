
# All the standard fixtures are put here

import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })

    yield app


@pytest.fixture()
def session_client(app):
    return app.test_client()


@pytest.fixture()
def session_runner(app):
    return app.test_cli_runner()
