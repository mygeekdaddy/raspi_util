#!/usr/bin/python
# -*- coding: utf-8 -*-

#-----------------------------------------------------#
# Basic python script to display CPU temp in deg F
# Created by: Jason Verly
# Date: 2014-12-04
# The MIT License (MIT)
# Copyright (c) 2014 Jason Verly
# See http://opensource.org/licenses/MIT for details
#-----------------------------------------------------#

import os
import time
 
cpu_temp = os.popen('vcgencmd measure_temp').readline()
 
temp_c = eval(cpu_temp[5:9])
 
temp_f = (9 * temp_c)/5 + 32
 
 
print 'RPi CPU temp is: %.1f °F' % temp_f