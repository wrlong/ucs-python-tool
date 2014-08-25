#!/usr/bin/python

from UcsSdk import *

def ucs_login(ucsm_ip, user, password):

    try:
        handle = UcsHandle()
        handle.Login(ucsm_ip, user, password)
        return handle
    except LoginError:
        print("Error: Unable to login to UCSM " + ucsm_ip)
