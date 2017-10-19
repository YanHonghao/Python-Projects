#!/usr/local/bin/python3
h=float(input("height(m):"));
w=float(input("weight(kg):"));
bmi=w/h/h;
if bmi < 18.5 :
	print("BMI:%.2f -- thin" % bmi);
elif bmi < 25 :
	print("BMI:%.2f -- normal" % bmi);
elif bmi < 28 :
	print("BMI:%.2f -- overweight" % bmi);
elif bmi < 32 :
	print("BMI:%.2f -- fat" % bmi);
else :
	print("BMI:%.2f -- overfat" % bmi);
