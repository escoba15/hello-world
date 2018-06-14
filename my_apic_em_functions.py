import requests
import json
from tabulate import *
from my_apic_em_functions import *


def get_ticket():
    requests.packages.urllib3.disable_warnings()  #Disable SSL warnings
    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"}
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"}
    resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
    status = resp.status_code
    #print("Ticket request status: ", status)

    response_json = resp.json()

    service_ticket = response_json['response']['serviceTicket']

    #print("The service ticket number is: ", service_ticket)
    #optional
    return service_ticket

def print_hosts():
    api_url = "https://sandboxapicem.cisco.com/api/v1/host"
    ticket = get_ticket()
    # Hard Code ticket
    # ticket = "ST-3490-ULLpHxvkKX2tro0L710T-cas"

    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    # print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    host_list = []
    i = 0
    for item in response_json["response"]:
        i += 1
        host = [i, item["hostType"], item["hostIp"]]
        host_list.append(host)

    table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))

def print_devices():
    api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    # Hard Code ticket
    # ticket = "ST-3490-ULLpHxvkKX2tro0L710T-cas"

    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Status of /host request: ", resp.status_code)

    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)

    response_json = resp.json()

    host_list = []
    i = 0
    for item in response_json["response"]:
        i += 1
        host = [i, item["type"], item["managementIpAddress"]]
        host_list.append(host)

    table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))

"""def main():
    
    Lab n. Description

    Conditions:
    
    get_ticket()
    print_hosts()
    print_devices()


if __name__ == '__main__':
    main()"""

