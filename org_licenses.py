#pull back all of the orgs and then query the license date in all of those orgs.

import requests
import cred

base_url = 'https://api.meraki.com/api/v0/'
headers = {'X-Cisco-Meraki-API-Key': (cred.key), 'Content-Type': 'application/json'}


get_orgs_url = base_url + 'organizations'

get_orgs_response = requests.get(get_orgs_url, headers=headers)
get_orgs_json = get_orgs_response.json()

for z in get_orgs_json:
    org_id = z['id']
    get_license_url = base_url + 'organizations/%s/licenseState' % org_id
    get_license_response = requests.get(get_license_url, headers=headers)
    get_license_json = get_license_response.json()
    print('Organization ' + (z['name']) + ' Current Status ' + (get_license_json['status']) + ' Expiration Date ' + (get_license_json['expirationDate']))

