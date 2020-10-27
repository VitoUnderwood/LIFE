# not
age = int(input("年龄："))
if not (age < 18):
    grade = int(input("年级："))
    if grade >= 12:
        print("OK")
    else:
        print("不行！")
else:
    print("年龄不满18")