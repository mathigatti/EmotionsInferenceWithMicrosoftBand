#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import sys

ROOT = '/Users/mgatti/Desktop/Physiological_Studies/'

IMG_ROOT = ROOT + 'IMGs/'
DATA_ROOT = ROOT + 'Data/'

def makeFigure(name, df, date):
	plt.cla() # descarto datos

	df[name].plot()
	plt.savefig(IMG_ROOT+ date + '/' +name+'.png')


def main(argv):

	DATE = argv[0]

	fileName1 = DATA_ROOT + DATE + '/Skin_' + DATE +'.csv'
	fileName2 = DATA_ROOT + DATE + '/Atmospheric_'+ DATE + '.csv'
	fileName3 = DATA_ROOT + DATE + '/Heart_'+ DATE +'.csv'

	# Import data from csv
	df1 = pd.read_csv(fileName1, parse_dates = True, index_col = 0, skiprows=[0])
	df1.head()

	df2 = pd.read_csv(fileName2, parse_dates = True, index_col = 0, skiprows=[0])
	df2.head()

	df3 = pd.read_csv(fileName3, parse_dates = True, index_col = 0, skiprows=[0])
	df3.head()

	subprocess.call('mkdir ' + IMG_ROOT + DATE, shell=True)

	makeFigure('Skin Temperature', df1, DATE)

	makeFigure('Resistivity(Kohms)', df1, DATE)

	makeFigure('Brightness(lux)', df2, DATE)

	makeFigure('Air Temperature', df2, DATE)

	makeFigure('Air Pressure(hPa)', df2, DATE)

	makeFigure('Heart Rate(bpm)', df3, DATE)

	makeFigure('RR',df3, DATE)

if __name__ == "__main__":
    main(sys.argv[1:])
