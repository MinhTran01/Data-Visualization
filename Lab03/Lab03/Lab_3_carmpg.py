# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:53:34 2015

@author: nymph
"""


#################################### Read the data ############################
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#Thư viện matplotlib được sử dụng để vẽ các biểu đồ trong python

''' read_csv()
The read_csv() function in pandas package parse an csv data as a DataFrame data structure. What's the endpoint of the data?
The data structure is able to deal with complex table data whose attributes are of all data types. 
Row names, column names in the dataframe can be used to index data.
'''

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original", delim_whitespace = True, \
 header=None, names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin', 'car_name'])

data['mpg']
data.mpg
data.iloc[0,:]

print(data.shape)

################################## Enter your code below ######################

#1. How many cars and how many attributes are in the data set.
print("\n1.\n")

print("Number of cars: ", data.shape[0])
print("Number of attributes: ", data.shape[1])

#2. How many distinct car companies are represented in the data set? What is the name of the car with the best MPG? What car company produced the most 8-cylinder cars? What are the names of 3-cylinder cars? Do some internet search that can tell you about the history and popularity of those 3-cylinder cars.
print("\n2.\n")

# Lấy dữ liệu tên hãng xe
data['car_company'] = data["car_name"].str.split().str[0]
print(data)

# How many distinct car companies are represented in the data set?
companies_dis = np.unique(data['car_company'] )
print("Number distinct car companies are represented: ", len(companies_dis),'\n')

# What is the name of the car with the best MPG?
index_MPG_max = np.argmax(data['mpg'])
best_MPG = data.iloc[index_MPG_max]['car_name']
print("The name of the car with the best MPG: ", best_MPG,'\n')

# Car company produced the most 8-cylinder cars
temp = data.loc[data['cylinders']==8.0]
car_counts = temp['car_company'].value_counts()
print("Car company produced the most 8-cylinder cars: ", car_counts.idxmax())
print("The company's number of 8-cylinder vehicles : ", car_counts.max()),'\n'

# The names of 3-cylinder cars
tempt = data.loc[data['cylinders']==3.0]
name_car = tempt['car_name'].to_list()
print(name_car,'\n')

#3. What is the range, mean, and standard deviation of each attribute? Pay attention to potential missing values.
print("\n3.\n")

# Check missing value
print(data.isnull().sum())
# --> Handling missing values: Giữ nguyên missing value để tránh mất mát dòng dữ liệu quan trọng

# What is the range, mean, and standard deviation of each attribute
print(data.describe().loc[['mean','std','min','max']])

#4. Plot histograms for each attribute. Pay attention to the appropriate choice of number of bins. Write 2-3 sentences summarizing some interesting aspects of the data by looking at the histograms.
print("\n4.\n")

# names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin']
# for col in names:
#     sns.histplot(data=data, x=col, bins=8, kde=False, color='#86bf91', fill=True)
#     plt.title("Histogram of attribute " + col)
#     plt.show()



# Nhận xét
#   Dữ liệu về tốc độ tăng tốc của xe - acceleration có phân phối chuẩn, điều này cũng có nghĩa là các loại xe tập trung vào thiết kế các xe có acceleration trung bình
#   Phân phối của mpg và weight đều có phân phối lệch sang trái, nghĩa là số lượng xe được tạo với mpg và weight càng lớn thì càng ít dần
#   Trong phân phối của cyclines, dữ liệu tập trung nhất ở giá trị 4, nghĩa là các loại xe chủ yếu sẽ là 4 xi lanh 


#5. Plot a scatterplot of weight vs. MPG attributes. What do you conclude about the relationship between the attributes? What is the correlation coefficient between the 2 attributes?
print("\n5.\n")

sns.scatterplot(x="weight", y="mpg", data=data)
plt.show()

# Nhận xét biểu đồ: 
#   Hai dữ liệu có sự tương quan cao: Khi dữ liệu của weight càng tăng thì mpg càng giảm. Điều này có nghĩa weight và mpg tương quan âm.")

corr = data["weight"].corr(data["mpg"]).round(2)
print("Hệ số tương quan giữa weight vs. MPG  : ", corr )

#6. Plot a scatterplot of year vs. cylinders attributes. Add a small random noise to the values to make the scatterplot look nicer. What can you conclude? Do some internet search about the history of car industry during 70’s that might explain the results.(Hint: data.mpg + np.random.random(len(data.mpg)) will add small random noise)
print("\n6.\n")
tempt = data
tempt.cylinders = tempt.cylinders + np.random.random(len(tempt.cylinders))
sns.lmplot(x="model", y="cylinders", data=tempt, line_kws={'color': 'red'})
plt.title("A scatterplot of year vs. cylinders attributes")
plt.show()


#Nhận xét biểu đồ:
#   Dựa vào biểu đồ ta thấy được rằng số lượng cylinder giảm qua các năm\nTa có thể biết rằng khi số lượng cylinder càng lớn thì công suất và tốc độ xe cũng tăng theo. Đây có thể là nguyên do chính dẫn ra xu hướng thiết kế xe hơi có càng ít xi lanh càng tốt. Ngoài ra cũng có thể vì một số nhu cầu sau:")
#   Trong những năm 70 và đầu những năm 80, chính phủ Hoa Kỳ đã đưa ra những quy định nghiêm ngặt về khí thải độc hại của các phương tiện giao thông, nhằm bảo vệ môi trường và sức khỏe con người. Điều này đã đẩy các nhà sản xuất xe hơi phải thay đổi thiết kế và sử dụng công nghệ mới để giảm thiểu khí thải. Trong đó, giảm số lượng xi lanh trên mỗi xe là một trong những giải pháp được áp dụng. Việc giảm số lượng xi lanh trên mỗi xe giúp giảm lượng nhiên liệu tiêu thụ và do đó giảm khí thải. Ngoài ra, cũng có sự tiến bộ trong công nghệ sản xuất động cơ, giúp tăng hiệu suất và sử dụng nhiên liệu một cách hiệu quả hơn.\n- Tuy nhiên, trong thời kỳ này, khi nền kinh tế Mỹ bị suy thoái, sự cạnh tranh về giá thành ô tô làm giảm doanh số bán xe của Mỹ, vì thế Mỹ đã tập trung sản xuất xe nhỏ gọn tiết kiệm nhiên liệu và giá thành thấp hơn để cải thiện doanh số.\n=> Vì vậy số lượng Cylinder của xe hơi có xu hướng giảm.


#7. Show 2 more scatterplots that are interesting do you. Discuss what you see.
print("\n7.\n")

# Scatterplots of acceleration vs. horsepower
sns.lmplot(x="acceleration", y="horsepower", data=data, line_kws={'color': 'red'})
plt.title("Scatterplots of acceleration vs. horsepower")
plt.show()

# Nhận xét
# Horsepower và acceleration có mối tương quan âm, vì vậy ta có thể hiểu:
    # Tốc độ tăng tốc của động cơ càng giảm thì công suất của động cơ càng lớn, xe càng mạnh.
    # Điều này liên quan đến cách mà công suất được tính toán. Trong một động cơ, công suất được tính bằng công việc được thực hiện trong một đơn vị thời gian. Tốc độ tăng tốc của động cơ càng chậm, thì động cơ càng dễ dàng đạt được mức công suất cao hơn.


# Scatterplots of weight vs. horsepower
sns.lmplot(x="weight", y="horsepower", data=data, line_kws={'color': 'red'})
plt.title("Scatterplots of weight vs. horsepower")
plt.show()

# Nhận xét
# Weight và horsepower có mối tương quan dương, vì vậy ta có thể hiểu:
    # Khi trọng lượng của xe càng tăng thì công suất của động cơ càng lớn. CÓ lẽ vì thường thì những chiếc xe hơi có động cơ công suất lớn sẽ có trọng lượng tương đối nặng để đảm bảo khả năng vận hành ổn định và an toàn

#8. Plot a time series for all the companies that show how many new cars they introduces during each year. Do you see some interesting trends? (Hint: data.car name.str.split()[0] returns a vector of the first word of car name column.)
print("\n8.\n")

df_grouped = data.groupby(['car_company', 'model']).count().reset_index()

fig,ax = plt.subplots(figsize=(25, 10))
colors = cm.tab20(np.linspace(0, 1, len(data['car_company'].unique())))
for name, color in zip(data['car_company'].unique(), colors):
    df = df_grouped[df_grouped['car_company'] == name]
    ax.plot(df['model'], df['car_name'], label=name, color=color)

ax.legend(bbox_to_anchor=(1, 1))
ax.set_xlabel('Year')
ax.set_ylabel('Number of cars')
ax.set_title('Number of cars produced by each car company over time')
plt.show()

# Nhận xét:
#   Hãng xe nổi tiếng như BMW, Ford có xu hướng giảm số lượng xe ra mắt mỗi năm
#   Cuối thập niên 70 đầu thập niên 80 thị trường ngày càng xôi nổi khi có các thương hiệu mới nổi đến từ Hàn, Nhật như Huyndai, Nissan, Kia,...

#9. Calculate the pairwise correlation, and draw the heatmap with Matplotlib. Do you see some interesting correlation? (Hint: data.iloc[:,0:8].corr(), plt.pcolor() draws the heatmap.)
print("\n9.\n")

temp = data
temp.drop(['car_name', 'car_company'], axis=1)
corr = temp.corr().round(2)
sns.heatmap(corr, annot=True, fmt=".2f")
plt.title('the heatmap of all attributes')
plt.show()

# Nhận xét
#   Hệ số tương quan giữa các thuộc tính cylinders, displacement, horsepower và weight có sự tương quan dương với nhau. 
#       Trong đó, displacement và cylinders có sự tương quan chặt chẽ với Hệ số tương quan là 0.95
#   Riêng mpg là tương quan âm với các thuộc tính cylinders, displacement, horsepower, và weight.
#       Trong đó hệ tương quan của mpg và weight là -0.84
