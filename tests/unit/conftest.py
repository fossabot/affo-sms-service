import pytest

from affo_sms_service.sms.sms_factory import SMSFactory


@pytest.fixture(scope='session')
def sms_factory(request):
    return SMSFactory()


@pytest.fixture(scope='session', params=('twilio', 'clickatell', ))
def sms_gateway(request, sms_factory):
    return sms_factory.get(request.param)
