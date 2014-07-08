#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

In python how to know the number of times is repeated an item of the tuple?

¿Como determinar la cantidad de veces que se repite un item de una tupla en
python?
'''

#create a tuple
tupla = 1, 5, 9, 5, 1, 5, 5, 4
print (tupla)

#return the number of times it appears in the tuple.
count = tupla.count(5)
print (count)

count = tupla.count(1)
print (count)

count = tupla.count(2)
print (count)
