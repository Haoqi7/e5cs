import time  
import winsound  
  
def focus_clock():  
    while True:  
        print(time.strftime("%H:%M:%S"))  # 打印当前时间  
        time.sleep(1)  # 等待1秒  
  
        if time.strftime("%M") == "00":  # 如果当前分钟是00，提醒用户专注  
            print("Focus time!")  
            winsound.Beep(1000, 1000)  # 播放一段提示音  
  
focus_clock()  # 开始专注时钟
