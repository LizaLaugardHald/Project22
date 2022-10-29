from asyncio.windows_events import NULL
from urllib import request
import requests

USERNAME="liza.voros@hotmail.com"
PASSWORD="liza123"

host="https://raven-api-eu.clobotics.com"


def validate_response(response):
    print(response)
    response_data = response.json()
    assert response.ok
    assert not response_data["error"]
    return response_data

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

login_data = validate_response(
    requests.post(host + "/api/v1/auth/signin/", data={
        'email': USERNAME,
        'password': PASSWORD
    })
)

#print(login_data)

token = login_data["token"]

campaign_id = json_extract(login_data, 'id')
campaign_id = campaign_id[1] # Dårlig løsning. Find på noget bedre. Det skal være dynamisk. Modificer måske json_extract
#print(token)
#print(campaign_id)

#print(host + "/api/v1/campaign/" + campaign_id + "/turbines/")

headers_turbine = {'Authorization': 'Token ' + token}
#print(headers_turbine)

turbine_data = validate_response(
    requests.get(host + "/api/v1/campaign/" + campaign_id + "/turbines/", headers=headers_turbine)
)
#print(turbine_data)

turbine_id = json_extract(turbine_data, 'id')
turbine_id = turbine_id[0]
#print(turbine_id)

headers_defect = {'Authorization': 'Token ' + token}

defect_details_data = validate_response(
    requests.get(host + "/api/v1/turbine/" + turbine_id + "/defects/detailed/", headers=headers_turbine)
)

print(defect_details_data)

