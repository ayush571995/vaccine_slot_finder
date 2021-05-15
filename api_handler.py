import requests

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

def extract_session_info(session_json_info, date):
    new_dict = {}
    for i in session_json_info:
        if i['date'] == date:
            new_dict['available_capacity'] = i['available_capacity']
            new_dict['vaccine'] = i['vaccine']
            new_dict['slots'] = i['slots']
            new_dict['min_age_limit'] = i['min_age_limit']
            return new_dict
    return None


def extract_center_info(json_data, date):
    data = dict()
    data['name'] = json_data['name']
    data['fee_type'] = json_data['fee_type']
    vaccine_info = extract_session_info(json_data['sessions'], date)
    if vaccine_info:
        data['vaccine'] = vaccine_info['vaccine']
        data['available_capacity'] = vaccine_info['available_capacity']
        data['slots'] = vaccine_info['slots']
        data['min_age_limit'] = vaccine_info['min_age_limit']
        return data
    return None


def make_api_call(pincode, date):

    querystring = {"pincode": pincode, "date": date}

    headers = {
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        'accept-language': "en-US,en;q=0.9",
        'cache-control': "no-cache",

    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    if response.status_code == 200:
        data = response.json()
        centres = [extract_center_info(i, date) for i in data['centers']]
        clean = [x for x in centres if x != None]
        if len(clean) > 0:
            print(*clean, sep='\n')
        else:
            print('No Slot Available')
    else:
        print('Response status not 200')
