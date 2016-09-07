#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygwizo

if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    # vowcon
    print("{0} has Pattern {1}".format(val.word, val.vowcon))

    # Measure value [v]vc{m}[c]
    print("{0} has Measure value {1}".format(val.word, val.measure))
