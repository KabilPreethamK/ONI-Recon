import os

class ONI_NET:
    
    def stage1(self):
        ip=os.system("ip route get 1.2.3.4 > ./data/stage/stage_myhost.txt")
        with open("./data/stage/stage_myhost.txt", "r") as f:
            cnt = f.readlines()
            cnt1 = [line.split() for line in cnt]
            self.host_ip = cnt1[0][2]
        os.system("sudo fping -aqg "+self.host_ip+"/24" +" > ./data/network/local_net_arp.txt")
        
        with open("./data/network/local_net_arp.txt","r") as f:
            cnt = f.readlines()
            cnt1 = [line.split() for line in cnt]
            file =  open("./data/network/local_ip.txt","w") 
            for i in range(0,len(cnt)):
                self.host_ip = cnt1[i][0] 
                file.writelines(self.host_ip+"\n")
            file.close()


        

oni = ONI_NET()
oni.stage1()
