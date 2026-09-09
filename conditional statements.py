#conditional statements-how to make decisions in python using( if, elif & else)
from main import score1

#if-this is true,to do something
#elif-else if this is true to do something
#eles-if nothing above is true, do this

cookies =   5

if  cookies ==  1:
    print("then i will cook 1 cookie")
elif cookies >  1:
    print("then i   will    cook    2   cookie  many    cookies")
else:
    print("i    failed  to  cook    cookies")

#second practice

score = int(input("enter your score:)"))
if  score >=    90:
    print("grade A")
elif score  >= 75:
    print("grade: B")
elif score >= 50:
    print("grade: C")
else:
    print("grade: F -   Fail")