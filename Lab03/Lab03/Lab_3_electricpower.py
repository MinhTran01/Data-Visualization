# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

############################## Your code for loading and preprocess the data ##

#Đọc file dữ liệu
df = pd.read_csv('household_power_consumption.txt', sep=';', low_memory=False)

#Chuyển kiểu dữ liệu Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst= True)

#Lọc dữ liệu để lấy các bản ghi từ ngày 2007-02-01 đến 2007-02-02.
data = df.loc[(df['Date'] >= '2007-02-01') & (df['Date'] <= '2007-02-02')].reset_index(drop=True)

#Chuyển kiểu dữ liệu Time
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.time
data['Time'] = pd.to_datetime(data['Date'].astype(str) + ' ' + data['Time'].astype(str))

#Tiền xử lý dữ liệu
# 1. Kiểm tra thuộc tính của dữ liệu
print("Kiểu dữ liệu của các thuộc tính trong dataframe")
print(data.info())
#    Chuyển kiểu dữ liệu của các cột 
columns = ['Global_active_power','Global_reactive_power','Voltage','Global_intensity','Sub_metering_1','Sub_metering_2','Sub_metering_3']
for col in columns:
    data[col] = data[col].astype('float64')

print("\nKiểm tra lại kiểu dữ liệu đã chuyển đổi")
print(data.info())

# 2. Kiểm tra missing value
#    Thay thế các giá trị ? trong dataframe bằng null
data = data.replace('?', np.nan)
print(data.isna().sum())
#    Nhận xét: Không có giá trị missing

############################ Complete the following 4 functions ###############

#Tự động chọn khoảng cách giữa các điểm đánh dấu trên trục thời gian
locator = mdates.AutoDateLocator(minticks=1, maxticks=3)
#Định dạng lại ngày thành chuỗi thứ ngắn gọn
formatter = mdates.ConciseDateFormatter(locator)

def plot1():
    fig1, ax1 = plt.subplots(figsize=(15, 8))
    ax1 = data['Global_active_power'].hist(color='red', edgecolor='black',
                                        bins= np.arange(0, max(data['Global_active_power']) + 0.5, 0.5))
    ax1.grid(False)
    ax1.spines['top'].set_color('none')
    ax1.spines['right'].set_color('none')
    ax1.spines['left'].set_position(('outward', 10))
    ax1.spines['bottom'].set_position(('outward', 10))

    plt.xticks([0,2,4,6])
    ax1.set_title('Global Active Power')
    ax1.set_xlabel('Global_active_power(kilowatts)')
    ax1.set_ylabel('Frequency')
    plt.savefig('plot1.png', bbox_inches='tight')
    plt.show()
    pass

def plot2():
    fig2, ax2 = plt.subplots(figsize=(15, 8))
    ax2 = plt.plot(data['Time'], data['Global_active_power'], color='black')

    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a'))

    plt.ylabel('Global Active Power (kilowatts)')
    plt.savefig('plot2.png', bbox_inches='tight')
    plt.show()
    pass

def plot3():
    fig, ax3 = plt.subplots(figsize=(15, 8))
    ax3.plot(data['Time'], data['Sub_metering_1'], label='Sub_metering_1',color='black')
    ax3.plot(data['Time'], data['Sub_metering_2'], label='Sub_metering_2',color='red')
    ax3.plot(data['Time'], data['Sub_metering_3'], label='Sub_metering_3',color='blue')
    ax3.legend()
    ax3.set_ylabel('Energy sub metering')

    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%a'))

    plt.savefig('plot3.png', bbox_inches='tight')
    plt.show()
    pass

def plot4():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))

    ax1.plot(data['Time'], data['Global_active_power'], color='black')
    ax1.set_ylabel('Global_active_power')
    ax1.xaxis.set_major_locator(locator)
    ax1.xaxis.set_major_formatter(formatter)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%a'))

    ax2.plot(data['Time'], data['Voltage'].astype('float64'), color='black')
    ax2.set_ylabel('Voltage')
    ax2.set_xlabel('datetime')
    ax2.xaxis.set_major_locator(locator)
    ax2.xaxis.set_major_formatter(formatter)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%a'))

    ax3.plot(data['Time'], data['Sub_metering_1'], label='Sub_metering_1', color='black')
    ax3.plot(data['Time'], data['Sub_metering_2'], label='Sub_metering_2', color='red')
    ax3.plot(data['Time'], data['Sub_metering_3'], label='Sub_metering_3', color='blue')
    ax3.legend()
    ax3.set_ylabel('Energy sub metering')
    ax3.xaxis.set_major_locator(locator)
    ax3.xaxis.set_major_formatter(formatter)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%a'))

    ax4.plot(data['Time'], data['Global_reactive_power'].astype('float64'), color='black')
    ax4.set_ylabel('Global_reactive_power')
    ax4.set_xlabel('datetime')
    ax4.xaxis.set_major_locator(locator)
    ax4.xaxis.set_major_formatter(formatter)
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%a'))

    plt.savefig('plot4.png', bbox_inches='tight')
    plt.show()
    pass

plot1()
plot2()
plot3()
plot4()
