#!/usr/bin/python

from UcsSdk import *


def ucs_login(ucsm_ip, user, password):

    handle = UcsHandle()
    handle.Login(ucsm_ip, user, password)

    return handle
