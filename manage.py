#!/usr/bin/env python
import os
import sys
import envvars

if __name__ == "__main__":
    envvars_file = os.path.join('env')
    if os.path.exists(envvars_file):
        envvars.load(envvars_file)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
