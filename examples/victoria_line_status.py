#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tflclient import tflclient


statuses = tflclient.get_line_status('victoria')[0].lineStatuses
print('Victoria line status:')
for s in statuses:
    if s.statusSeverity == 10:
        print(s.statusSeverityDescription)
    else:
        print(s.statusSeverityDescription, ":", s.reason)
