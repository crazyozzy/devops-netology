#!/bin/python
import socket
import json
import os.path


def get_sites(sites):
        for site in sites.keys():
                sites[site] = socket.getaddrinfo(site, 443)[0][4][0]
                print(f'{site}  {sites[site]}')
        return sites


sites = {'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}


if os.path.exists('old_ip.json'):
        with open('old_ip.json') as file:
                old_sites = json.load(file)
else:
        sites = get_sites(sites)
        with open('old_ip.json', 'w') as file:
                json.dump(sites, file)
        exit(0)


sites = get_sites(sites)
for site in sites.keys():
        if sites[site] != old_sites[site]:
                print(f'[ERROR] {site} IP mismatch: {old_sites[site]} {sites[site]}')