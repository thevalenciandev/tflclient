#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tflclient import tflclient


tube_lines = tflclient.get_lines_for_modes('tube')
print('All tube lines:')
[print(line.id) for line in tube_lines]
