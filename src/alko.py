import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patche as mpatches

df = pd.read_csv("alkosales.csv")

#Assing all columns to a variable for easy access
month = df['Month']
vodka_spirit = df['VodkaAndSpirit']
other_spirit = df['OtherSpirit']
fortified_wine = df['FortifiedWine']
red_wine = df['RedWine']
white_wine = df['WhiteWine']
sparkling_wine = df['SparklingWine']
rose_wine = df['RoseWine']
other_wine = df['OtherWine']
cider = df['Cider']
long_drink = df['LongDrink']
beer = df['Beer']
non_alcoholic_beverage = df['NonAlcoholicBeverage']
total = df['Total']
pure_alcohol_total = df['PureAlcoholTotal']

