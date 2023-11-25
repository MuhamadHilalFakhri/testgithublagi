#1

def if_else_example():
    number = int(input("Masukkan angka : "))
    if number==0:
        print("number is zero value")
    else:
        print("number is non zero value")
if_else_example()

#
def if_elif():
    nilai = float(input("Masukkan angka : "))
    if nilai >=90:
        print("Excellent performance")
    elif nilai >=80:
        print("Very Good performance")
    elif nilai >=70:
        print("70 then Good performance")
    elif nilai >=60:
        print("average performance")
    else:
        print("Poor performance")
if_elif()

#
def number():
    num1 = int(input("Masukkan angka ke-1 : "))
    num2 = int(input("Masukkan angka ke-2 : "))
    if num1>num2:
        print("Angka yg terbesar adalah : ", num1)
    else:
        print("Angka yg terbesar adalah : ", num2)
number()