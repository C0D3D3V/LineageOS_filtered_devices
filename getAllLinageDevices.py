#!/usr/bin/env python

import os
import yaml

if not os.path.exists('./nooo'):
    os.mkdir('./nooo')
if not os.path.exists('./devices'):
    os.mkdir('./devices')

yaml_files = os.listdir('./devices')

for file_name in yaml_files:
    with open('./devices/' + file_name) as yaml_file:
        dev_infos = yaml.load(yaml_file, Loader=yaml.FullLoader)

    # filter not version 16
    if 16 not in dev_infos['versions']:
        print(dev_infos['versions'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)

    # filter no ac wifi
    if 'ac' not in dev_infos['wifi']:
        print(dev_infos['wifi'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)

    # filter no nfc
    if 'NFC' not in dev_infos['peripherals']:
        print(dev_infos['peripherals'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)
    
    # filter no otg
    if 'USB OTG' not in dev_infos['peripherals']:
        print(dev_infos['peripherals'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)


    # filter no fingerprinter
    if 'Fingerprint reader' not in dev_infos['peripherals']:
        print(dev_infos['peripherals'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)


    # filter sreen
    if '720' in dev_infos['screen_res']:
        print(dev_infos['screen_res'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)


    # filter storage
    storage = dev_infos['storage'].split('/')
    enough = False
    for size in storage:
        realSize = int(''.join(c for c in size if c.isdigit()))
        if realSize >= 64:
            enough = True

    if not enough:
        print(storage)
        os.rename('./devices/' + file_name,'./nooo/' + file_name)

    # filter bad camara
    enough = False
    for camera in dev_infos['cameras']:
        res = camera['info'].split(' ')[0].replace('MP', '')
        try:
            if float(res) >= 16:
                enough = True
                break
    
        except Exception as e:
            e = False
    if not enough:
        print(dev_infos['cameras'])
        os.rename('./devices/' + file_name,'./nooo/' + file_name)



    print("https://wiki.lineageos.org/devices/" + dev_infos['codename'])
    #    print(file_name, dev_infos)


   


