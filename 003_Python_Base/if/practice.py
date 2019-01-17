#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
s1 = input('please input height:')
s2 = input('please input weight:')
height = float(s1)
weight = float(s2)
#bmi = ((weight) / (height*height))
bmi = weight / (height**2)
if bmi < 18.5:
	print('BMI指数 ', bmi, '：过轻')
elif bmi < 25:
	print('BMI指数 ', bmi, '：正常')
elif bmi < 28:
	print('BMI指数 ', bmi, '：过重')
elif bmi < 32:
	print('BMI指数 ', bmi, '：肥胖')
else:# >32
	print('BMI指数 ', bmi, '：严重肥胖')