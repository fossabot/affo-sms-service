def test_gateway_changing(sms_factory, phone):
    gateway = sms_factory.get_for_phone(phone=phone)
    assert gateway == sms_factory.get_for_phone(phone=phone)

    sms_factory.send(from_="AFFO", to=phone, body="test")
    assert gateway != sms_factory.get_for_phone(phone=phone, retry=True)
