import os

class ONI_NET:
    
    def stage1(self):
        ip=os.system("ip route get 1.2.3.4 > ./data/stage/stage_myhost.txt")
        with open("./data/stage/stage_myhost.txt", "r") as f:
            cnt = f.readlines()
            cnt1 = [line.split() for line in cnt]
            self.host_ip = cnt1[0][2]
        with open("./data/rc/stage_1.rc","w") as f:
            cnt = f.writelines("use auxiliary/scanner/discovery/arp_sweep\n")
            cnt = f.writelines("set rhosts "+self.host_ip+"/24\n")
            cnt = f.writelines("run\n")
            cnt = f.writelines("exit\n")
        os.system("sudo msfconsole -r ./data/rc/stage_1.rc -o ./data/network/local_net_arp.txt")

        

oni = ONI_NET()
oni.stage1()
