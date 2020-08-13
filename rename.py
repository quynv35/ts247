#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

list_file = os.listdir()

for file in list_file:
	if ".pdf" in file:
		cmd = "mkdir '{0}'".format(file[:-4])
		os.system(cmd)
		cmd = "mv '{0}' '{1}'".format(file,file[:-4])
		os.system(cmd)

print("Done!")