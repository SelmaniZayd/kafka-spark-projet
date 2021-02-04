#!/usr/bin/python3
# -*-coding:utf-8 -*
"""mapper.py"""

import sys

data = sys.stdin

for vente in data.readlines():
    res = vente.split('\t')[2] + "\t" + vente.split('\t')[4]
    print(res)