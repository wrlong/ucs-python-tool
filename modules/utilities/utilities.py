#!/usr/bin/python


def get_remove_dn_string(Dn, class_string):
    return 'handle.RemoveManagedObject(handle.GetManagedObject(None, ' +\
           class_string + '.ClassId(), {' + class_string + \
           '.DN:"' + Dn + '"}))\n'

def pad_zeros(int_as_string, num_digits):
    return int_as_string.zfill(num_digits)

def int_to_string(int_to_convert):
    return str(int_to_convert)
