from asyncio.windows_events import NULL
from urllib import request
import requests

USERNAME="liza.voros@hotmail.com"
PASSWORD="liza123"

host="https://raven-api-eu.clobotics.com"


def validate_response(response):
    response_data = response.json()
    assert response.ok
    assert not response_data["error"]
    return response_data

login_data = validate_response(
    requests.post(host + "/api/v1/auth/signin/", data={
        'email': USERNAME,
        'password': PASSWORD
    })
)

#print(login_data)

token = "Token " + login_data["token"]

print(token)

turbine_data = validate_response(
    requests.get(host + "/api/v1/campaign/{campaign_id}/turbines/", data={
        "Authorization": token
    })
)

print(turbine_data)





