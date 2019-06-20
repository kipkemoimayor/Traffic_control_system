# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7,GPIO.OUT)
# for i in range(0,3):
#     GPIO.output(7,True)
#     time.sleep(4)
#     GPIO.output(7,False)
#     time.sleep(1)
#
#
# GPIO.cleanup()
# n=2
# c='125'
# s=''
# count=0
# for i in c:
#     count+=1
#     if count<=n:
#         s+=i+','
#     else:
#         s+=i
# arr=s.split(",")
# arr1=[int(i) for i in arr]
# print(arr1)
# print(max(arr1))
a=0
def namw():
    a=10
    return a

print(namw())

b=a
print(b)
