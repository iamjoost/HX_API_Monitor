import requests
import json
import os
import urllib3

class HX_API(object):

    def __init__(self,hxip, hxuser, hxpasswd, hxtoken):
        urllib3.disable_warnings()
        self.hxip = hxip
        self.hxuser = hxuser
        self.hxpasswd = hxpasswd
        self.hxtoken = hxtoken

    # Generate HyperFlex API Token.
    def get_hxtoken(self):
        # payload = {'username': hxuser, 'password': hxpasswd, 'client_id': 'HxGuiClient', 'client_secret': 'Sunnyvale',
        #           'redirect_uri': 'http://localhost:8080/aaa/redirect/'}
        payload = {'username': self.hxuser, 'password': self.hxpasswd}

        headers = {
            "Content-type": "application/json",
            "Accept": "application/json"}

        url = 'https://' + self.hxip + '/aaa/v1/auth?grant_type=password'

        hxauth = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        if hxauth.status_code == 201:
            self.hxtoken = hxauth.json()['access_token']
            #return (self.hxtoken)
        else:
            print("There was an error getting the Token. Please try again in 15 minutes.")
            print("You should be on HXDP 4.0 or Higher to run this script correctly. ")
            print("HTTP Error Code: ", self.hxauth.status_code)
            print("Message: ", self.hxauth.text)
            os._exit(1)

    # Get HyperFlex UUID of the Cluster
    def get_cuuid(self):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.hxtoken}

        url = 'https://' + self.hxip + '/coreapi/v1/clusters'
        response = requests.get(url, headers=headers, verify=False)
        cuuid = response.json()[0]['uuid']
        return cuuid