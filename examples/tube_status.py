#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tflclient import tflclient


tube_status = tflclient.get_status('tube')
print('Tube status:')
for line in tube_status:
    statuses = [st.statusSeverityDescription for st in line.lineStatuses]
    disruption_details = {'detail': st.reason for st in line.lineStatuses
                          if st.statusSeverity != 10}  # 10 is Good Service
    print('\n', line.id, ':', "/".join(statuses))
    if disruption_details:
        [print(v) for v in disruption_details.values()]
