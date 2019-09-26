from platform import system, release, processor, node, machine
from sys import platform


def os_type():
    return system()


def os_version():
    return release()


def processor_name():
    return processor()


def machine_network_name():
    return node()


def machine_type():
    return machine()


def machine_platform():
    return platform
