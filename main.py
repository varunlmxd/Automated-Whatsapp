import pywhatkit as pwk
import datetime
n=10
while(n):
    n=n-1
    current_time = datetime.datetime.now()
    print(current_time.hour,current_time.minute)
    pwk.sendwhatmsg("+91XXXXXXXXXX", "spam!", current_time.hour, current_time.minute+1, wait_time = 15, tab_close=True)
