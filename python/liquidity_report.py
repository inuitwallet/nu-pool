#! /usr/bin/env python
"""
The MIT License (MIT)
Copyright (c) 2015 creon (creon.nu@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""


import time
import os

liquidity = {'ask': {}, 'bid': {}}


for logs_file in os.listdir('logs'):
    if not logs_file.endswith('credits'):
        continue
    with open('logs/%s' % logs_file) as credits_file:
        last_time = None
        side = None
        for i, line in enumerate(credits_file):
            line = line.strip().split()
            log_time = line[0]
            if log_time != last_time:
                for side in ['ask', 'bid']:
                    for exchange in liquidity[side]:
                        for key in liquidity[side][exchange][last_time]:
                            total = 0
                            for value in liquidity[side][exchange][last_time][key]:
                                total += float(value)
                            liquidity[side][exchange][last_time][key] = total
                        grand_total = 0
                        for key in liquidity[side][exchange][last_time]:
                            grand_total += float(liquidity[side][exchange][last_time][key])
                        liquidity[side][exchange][last_time] = grand_total

                print str(liquidity) + "\n"
                time.sleep(5)
                last_time = log_time

            side = line[5]
            key = line[3]
            amount = line[4]
            exchange = line[6]

            if exchange not in liquidity[side]:
                liquidity[side][exchange] = {}

            if log_time not in liquidity[side][exchange]:
                liquidity[side][exchange][log_time] = {}

            if key not in liquidity[side][exchange][log_time]:
                liquidity[side][exchange][log_time][key] = []

            if amount not in liquidity[side][exchange][log_time][key]:
                liquidity[side][exchange][log_time][key].append(amount)