import random 
import math
import smtplib

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your OTP"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("dpk91219@gmail.com","ourw uitd antq exyi")
user="dpk91219@gmail.com"

emailid=input("enter your email:")
s.sendmail(user,emailid,msg)

while True:
    a=input("enter otp:")
    if a==OTP:
        print("successful")
    else:
        print("invalid")