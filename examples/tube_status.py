#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tflclient import tflclient


tube_status = tflclient.get_status('tube')
print('Tube status:')
for line in tube_status:
    statuses = [st.statusSeverityDescription for st in line.lineStatuses]
    print(line.id, ':', "/".join(statuses))
