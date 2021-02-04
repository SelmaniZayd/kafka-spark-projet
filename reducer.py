#!/usr/bin/python3
# -*-coding:utf-8 -*
"""reducer.py"""

import sys
from functools import reduce

def set_shops(shops, element):
    print(element)
    shop = element.split("\t")[0]
    bill = float(element.split("\t")[1])

    if shop not in shops:
        shops[shop] = bill
    else:
        shops[shop] += bill
    return shops


data = sys.stdin
cout_par_magasin = reduce(set_shops, data.readlines(), {})

print(cout_par_magasin)