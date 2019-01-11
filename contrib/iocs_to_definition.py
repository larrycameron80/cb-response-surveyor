#!/usr/bin/env python

"""
To use me:

1) Make a file full of indicators, one per line, call it indicators.txt.

NOTE: This was written to handle IP addresses. Change line 40 from ipaddr to md5 if passing hashes.

2) python iocs_to_definition.py indicators.txt

3) Run Surveyor using the output definition file indicators.json
"""

import json
import sys


if __name__ == '__main__':

  input_file = sys.argv[1]

  with open(input_file, 'rb') as indicators:

    indicator_list = []

    for indicator in indicators.readlines():
      indicator_list.append(indicator.strip())

  output_file = 'indicators.json'

  with open(output_file, 'wb') as output_file:
    output_file.write('{\n\t"FOO": {\n')

    list_len = len(indicator_list)
    counter = 0

    for indicator in indicator_list:
      counter += 1
      output_file.write('\t\t\t"ipaddr": ["{0}"]'.format(indicator))

      if counter != list_len:
        output_file.write(',')

      output_file.write('\n')

      if counter == list_len:
        output_file.write('\t}\n}\n')
