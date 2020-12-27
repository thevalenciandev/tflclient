#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tflclient import tflclient


print('Valid mode names:')
[print(mode.modeName) for mode in tflclient.get_modes()]
