#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tflclient import tflclient


tube_status = tflclient.get_status('tube')
print('Tube status:')
[print(line.id, ':', line.lineStatuses[0].statusSeverityDescription) for line in tube_status]
