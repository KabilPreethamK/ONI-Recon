import os

class ONI_NET:
    
    def stage1():
        ip=os.system("ip route get 1.2.3.4 ")
        print(ip)