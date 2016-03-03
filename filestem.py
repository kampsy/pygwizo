#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygwizo

array = open("input.txt").read().splitlines()
for word in array:
    val = pygwizo.Ingest(word)
    deep = val.deep_stem()
    with open("stem.txt", "a") as file:
        stem = deep + "\n"
        file.writelines(stem)
        print(word, " ---> ", deep)
