import pandas as pd
import os.path

xlfile = "sample.xlsx"
if os.path.exists(xlfile):
    xls = pd.ExcelFile(xlfile)
    sheet1 = xls.sheet_names(0)
    df = pd.DataFrame(xls.parse(sheet1))

    print(df.mean())
