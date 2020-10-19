#copy()方法，浅复制
score = {'Tom': 77, 'Alice': ["English",100]}
print(score)
#copy字典
copy_score = score.copy()
print(copy_score)
#修改copy后的字典值，原字典不受影响
copy_score["Tom"] = 88
print(score)
print(copy_score)
#copy后的新字典增加或删除时，对原字典有影响
copy_score["Bob"] = 60
print(score)
print(copy_score)
#删除
copy_score["Alice"].remove(100)
print(copy_score)
print(score)
del copy_score["Tom"]
print(copy_score)
print(score)