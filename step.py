#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygwizo

if __name__ == "__main__":
    val = pygwizo.Ingest("troubled")
    # Stem only with Step_1b
    print(val.step_1b())

    val.word = "vietnamization"
    # Stem only with Step_2
    print(val.step_2())

    val.word = "electriciti"
    # Stem only with Step_3
    print(val.step_3())
