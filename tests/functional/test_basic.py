from hamcrest import *

from pytest_toolbelt import matchers


def test_send(client, phone):
    response = client.post("/api/v1.0/sms/", json={"user_id": "0", "from": "AFFO", "phone": phone, "message": "test"})
    assert_that(response, matchers.has_status(201))


def test_send_retry(client, phone):
    response = client.post(
        "/api/v1.0/sms/", json={"user_id": "0", "from": "AFFO", "phone": phone, "message": "test", "retry": True}
    )
    assert_that(response, matchers.has_status(201))
