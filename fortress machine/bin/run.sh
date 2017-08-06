#!/bin/bash

python3 run.py syncdb
python3 run.py create_hosts -f ../share/examples/new_hosts.yml
python3 run.py create_remoteusers -f ../share/examples/new_remoteusers.yml
python3 run.py create_groups -f ../share/examples/new_groups.yml
python3 run.py create_bindhosts -f ../share/examples/new_bindhosts.yml
python3 run.py create_fortressusers -f ../share/examples/new_fortressusers.yml
python3 run.py start_session 
