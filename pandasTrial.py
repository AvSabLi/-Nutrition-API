import requests, json, sys, time
from pprint import pprint
import pandas as pd
import xlsxwriter
import xlrd
import openpyxl


# print empty excel called compareSearches
def intro3():
    # writer = pandas.ExcelWriter("compareSearches.xlsx", engine="xlsxwriter")
    writer = pd.ExcelWriter(  # https://github.com/PyCQA/pylint/issues/3060 pylint: disable=abstract-class-instantiated
        "demo.xlsx", engine="xlsxwriter"
    )
    writer.save()


intro3()