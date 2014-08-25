ucs_python_tool
===============

A simple UCS configuration tool that uses the UCS Python SDK for UCSM API integration.

It modularizes key functions for the UCS Python SDK, supporting configuration via a JSON structured configuration file for simplified manipulation. 
 
### Important source files
- build_ucs.py - Main file to build UCS environment; auto-generates a time stamped remove script.
- ucs_config<>.json - JSON configuraiton file required for build_ucs.py; Uses JSON format specifying UCSM constructs such as pools policies and templates.
- remove_ucs.py - Takes a previously auto-generated time-stamped removal script to remove all configuration completed by a previous build_ucs.py run.

### Usage
#### To build:
build_ucs.py -i `ip` -u `user` -p `password` -c `json config file`
```bash
$ build_ucs.py -i 192.168.10.10 -u admin -p cisco123 -c ucs_config-2xESX.json 
```
#### To remove:
remove_ucs.py -i `ip` -u `user` -p `password` -r `previous generated remove file`
```bash
$ remove_ucs.py -i 192.168.10.10 -u admin -p cisco123 -r remove_script_with_timestamp
```
