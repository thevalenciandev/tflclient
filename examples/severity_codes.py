#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tflclient import tflclient


modes = {}
for code in tflclient.get_severity_codes():
    if code.modeName not in modes:
        modes[code.modeName] = {}
    modes[code.modeName][code.severityLevel] = code.description

print('Codes for overground:')
[print(code, ':', desc) for code, desc in modes.get('overground').items()]
