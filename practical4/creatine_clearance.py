age = int (input("请输入您的年龄（岁）："))
weight = int(input ("请输入您的体重（千克）："))
gender = input("请输入您的性别：")
concentration = int(input ("请输入您的Cr的浓度（μmol/l）："))
if age < 100 and 20 < weight < 80 and 0 < concentration < 100 and gender == "男" or gender == "女":
    if gender == "男":
        CrCl = ((140-age)*weight)/(72*concentration)
    else:
        CrCl = ((140-age)*weight*0.85)/(72*concentration) 
    print (f"您的creatine clearance rate为{CrCl}")
else:
    print ("抱歉，您输入的数据不达标，不能计算creatine clearance rate")

# 请输入您的年龄（岁）：18
# 请输入您的体重（千克）：70
# 请输入您的性别：男 
# 请输入您的Cr的浓度（μmol/l）：50
# 您的creatine clearance rate为2.3722222222222222
