import wmi; import os; import time

w = wmi.WMI()

while 1 > 0:
    for process in w.Win32_Process():
        if process.name == "LeagueClient.exe":
            process.Terminate()
            print("stopping league")
            os.system("start \"\" https://www.healthygamer.gg/why-do-video-games-make-you-angry/")
            print("link opened")
    time.sleep(3)
