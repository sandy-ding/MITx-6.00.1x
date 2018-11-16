#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:36:37 2018

@author: apple
"""

def genPrimes():
    prime = [2]
    num = 2
    yield 2
    while True:
        isPrime = True
        for i in prime:
            if (num % i) == 0:
                num += 1
                isPrime = False
                break
        if isPrime == True:
            prime.append(num)
            yield num
            num += 1