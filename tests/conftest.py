import pytest

from affo_sms_service.application import create_app
from affo_sms_service.extensions import db as db_

TEST_DATABASE_URI = f'sqlite://'


def pytest_addoption(parser):
    parser.addoption(
        '--phone',
        action='store',
        help='A phone which receives test messages'
    )


@pytest.fixture
def phone(request):
    return request.config.getoption('--phone')


@pytest.fixture(scope='session', autouse=True)
def app(request):
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }
    app = create_app(settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session', autouse=True)
def db(app, request):
    db_.app = app
    db_.create_all()

    return db_


@pytest.fixture(scope='function')
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='session')
def client(app, db):
    return app.test_client()
