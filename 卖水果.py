#定义水果价格字典price，其中保存了苹果、桃子、香蕉、梨子四个水果与对应的价格
#Define the fruit price dictionary price, which stores the prices of four fruits: apple, peach, banana, and pear
price = {'苹果':5, '桃子':6, '香蕉':3, '梨子':4}

#通过循环，配合相应的信息，将字典中的水果与价格打印出来
#Through circulation, with corresponding information, print out the fruits and prices in the dictionary
print("今日水果价格:")
for fruit in price:
    print("%s %d 元/斤"%(fruit, price[fruit]))
print("")

#输入购买水果的种类数量，存储到变量n中
#Enter the type and quantity of fruit purchased and store it in variable n
n = int(input("请输入购买水果的种类数量:"))

#设置sum_price存储总金额
#Set sum_price to store the total amount
sum_price = 0

for i in range(0, n):
    #输入购买的水果名称与数量，存储至fruit与num
    #Enter the name and quantity of the purchased fruit and store it in fruit and num
    fruit = input("输入购买水果%d的名称:"%(i + 1))
    num = int(input("输入购买的水果%d的数量（斤）:"%(i + 1)))

    #如果输入的水果在price字典中
    #If the input fruit is in the price dictionary
    if fruit in price:
        #将水果单价price[fruit]乘购买的数量num累加到sum_price当中
        #Multiply the unit price price[fruit] of the fruit by the number of purchases num and add it to sum_price
        sum_price += price[fruit] * num

print("总价格为%d"%(sum_price))
'''
最后输出总价格sum_price
Finally, output the total price sum_price
'''
    
