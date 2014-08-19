#!/usr/bin/python

import sys
import getopt
from UcsSdk import *
from modules.utilities import login

ifile = ''
ofile = ''
ts = time.time()
timestamp_str = \
    datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
myopts, args = getopt.getopt(sys.argv[1:], "r:i:u:p:", ["remove_file=","ip=","user=","pw="])

for o, a in myopts:
    if o in ("-i", "--ip"):
        ucsm_ip = a
    elif o in ("-u", "--user"):
        ucsm_user = a
    elif o in ("-p", "--pw"):
        ucsm_pass = a
    elif o in ("-r", "--remove_file"):
        remove_file = a
    else:
        print("Usage: %s --ip <ip> --user <user_name> --pw <password> --remove_file <remove_file>" % sys.argv[0])

# Login to UCS
handle = login.ucs_login(ucsm_ip, ucsm_user, ucsm_pass)

f = open(remove_file, 'r')

handle.StartTransaction()

for rem_obj in f.readlines():
    print rem_obj
    eval(rem_obj)

handle.CompleteTransaction()
handle.Logout()

t_now = time.time()
print ""
print("Completed in %.2f seconds" % round((t_now-ts), 2))
