# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1koaiqWqGdSjjV_qYcz1znHNwp5NV7t36
"""

import pandas as pd


def printcsv():
    df = pd.read_csv("pima-indians-diabetesdata-pima-indians-diabetesdata.csv")
    return df.tail()
