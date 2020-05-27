from datetime import datetime

from requests.auth import HTTPBasicAuth
import requests

from access_token import generate_access_token
from  encode import generate_password
from utils import get_timestamp
import keys

formated_time=get_timestamp()

decoded_password=generate_password(formated_time)

def lipa_na_mpesa():
    
        access_token = generate_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
            "BusinessShortCode": keys.business_shortCode,
            "Password": decoded_password,
            "Timestamp": formated_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",
            "PartyA": keys.phone_number,
            "PartyB": keys.business_shortCode,
            "PhoneNumber": keys.phone_number,
            "CallBackURL": "https://fullstack.com",
            "AccountReference": "12345678",
            "TransactionDesc": "Paying school fees"
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        
        print (response.text)
        
lipa_na_mpesa()