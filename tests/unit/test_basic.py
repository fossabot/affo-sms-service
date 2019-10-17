def test_send(sms_gateway, phone):
    sms_gateway.send(from_="AFFO", to=phone, body="test")
