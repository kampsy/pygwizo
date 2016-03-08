#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygwizo
import time

if __name__ == "__main__":
    array = open("input.txt").read().splitlines()
    start_time = time.time()
    for word in array:
        val = pygwizo.Ingest(word)
        deep = val.deep_stem()
        with open("stem.txt", "a") as file:
            stem = deep + "\n"
            file.writelines(stem)
            print(word, " ---> ", deep)

    print("============================")
    print("Done After: %ss" % (time.time() - start_time))
    print("============================")
