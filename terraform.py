#!/usr/bin/env python3

from requests import get
import sysgenerics as sg
from sys import argv, stderr

# print('Executing script: ', argv[0])

if len(argv) != 2:
    stderr.write('Usage: python3 terraform.py <version>\nExample: python3 terraform.py 0.12.9\n'.format(argv[0]))
    exit(1)
else:
    print('Executing script: ', argv[0])


# print('\nOS type is: ' + sg.os_type())
# print('OS version is: ' + sg.os_version())
# print('Processor type is: ' + sg.processor_name())
# print('Machine network name is: ' + sg.machine_network_name())
# print('Machine type is: ' + sg.machine_type())
# print('Machine Platform type is: ' + sg.machine_platform())


app_name = 'terraform'
ver = argv[1]
darwin_url = 'https://releases.hashicorp.com/{}/{}/{}_{}_{}_amd64.zip'
linux_386_url = 'https://releases.hashicorp.com/{}/{}/{}_{}_{}_386.zip'
linux_amd64_url = 'https://releases.hashicorp.com/{}/{}/{}_{}_{}_{}.zip'
linux_arm_url = 'https://releases.hashicorp.com/{}/{}/{}_{}_{}_arm.zip'


def terraform_url_setter():
    if sg.os_type() == 'Darwin':
        terraform_url = darwin_url.format(app_name, ver, app_name, ver, sg.os_type().lower())
    elif sg.os_type() == 'Linux' & sg.processor_name() == 'i386':
        terraform_url = linux_386_url.format(app_name, ver, app_name, ver, sg.os_type().lower())
    elif sg.os_type() == 'Linux' & sg.processor_name() == 'amd64':
        terraform_url = linux_amd64_url.format(app_name, ver, app_name, ver, sg.os_type().lower(), sg.machine_type())
    elif sg.os_type() == 'Linux' & sg.processor_name() == 'arm':
        terraform_url = linux_arm_url.format(app_name, ver, app_name, ver, sg.os_type().lower())
    else:
        print('Other OS yet to be supported. TODO')
    return terraform_url


print('\nFetched URL: ' + terraform_url_setter())


def terraform_downloader():
    download_getter = get(terraform_url_setter(), allow_redirects=True)
    open('terraform.zip', 'wb').write(download_getter.content)


# terraform_downloader()

# flake8 --ignore E501 .
