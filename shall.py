#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygwizo

if __name__ == "__main__":
    val = pygwizo.Ingest("abilities")
    print(val.shallow_stem())
