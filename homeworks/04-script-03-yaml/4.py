#!/bin/python
import socket
import json
import os.path
import yaml
import time


def get_sites(sites):
        for site in sites.keys():
                sites[site] = socket.getaddrinfo(site, 443)[0][4][0]
                print(f'{site}  {sites[site]}')
        print('---')
        return sites


def write_files(sites):
        with open('old_ip.json', 'w') as jfile:
                json.dump(sites, jfile)
        with open('old_ip.yaml', 'w') as yfile:
                yaml.dump(sites, yfile)


sites = {'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
mismatch = False

while not mismatch:
        sites = get_sites(sites)

        if os.path.exists('old_ip.json'):
                with open('old_ip.json') as file:
                        old_sites = json.load(file)
        else:
                sites = get_sites(sites)
                old_sites = sites
                write_files(sites)


        for site in sites.keys():
                if sites[site] != old_sites[site]:
                        print(f'[ERROR] {site} IP mismatch: {old_sites[site]} {sites[site]}')
                        print('---')
                        write_files(sites)
        time.sleep(1)
