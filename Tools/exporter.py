import tkinter as tk
from tkinter import filedialog
import pandas as pd
global df
################ Excel #################
def export_to_excel(data,columns_table):
    df = pd.DataFrame(data, columns=columns_table)

    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
    canvas1.pack()


    def exportExcel():
        export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
        df.to_excel(export_file_path, index=False, header=True)


    saveAsButtonExcel = tk.Button(text='Export Excel', command=exportExcel, bg='green', fg='white',
                                font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=saveAsButtonExcel)

    root.mainloop()
'''
#excel xslx to dta convertor
def xlsx_to_dta(filename):
    pd.read_excel('Data/'filename + '.xlsx', index_col=0).to_stata('Data/'filename + '.dta')

#csv to dta convertor
def csv_to_dta(filename):
    pd.read_csv('Data/'filename + '.csv').to_stata('Data/'filename + '.dta')


def csv_merger():
    fout=open("d:/Files/Google Drive (gabryu@gmail.com)/Projects/PycharmProjects/coinmetrics/out.csv","a")
    # first file:
    for line in open("d:/Files/Google Drive (gabryu@gmail.com)/Projects/PycharmProjects/coinmetrics/sh1.csv"):
        fout.write(line)
    # now the rest:
    for num in range(2,5):
        f = open("d:/Files/Google Drive (gabryu@gmail.com)/Projects/PycharmProjects/coinmetrics/sh"+str(num)+".csv")
        next(f) # skip the header
        for line in f:
            fout.write(line)
        f.close() # not really needed
    fout.close()
'''