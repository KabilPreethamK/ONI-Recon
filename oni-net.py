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
    
    def stage_sep(self):
        with open("./data/network/local_net_arp.txt","r") as f:
            lines = [line.rstrip('\n') for line in f]
        for i in range(len(lines)):
            if "run" in lines[i]:
                ip_in_line = i+1
                for stop in range(ip_in_line,1000):
                    end_point = lines[stop]
        
                    if "100%" in end_point:
                        count_http = stop
                        break
                with open("./data/network/final_local_arp.txt","w") as m:
                    for i in range(ip_in_line,count_http):
                        m.writelines(lines[i]+"\n")
            else:
                pass
        
        with open("./data/network/final_local_arp.txt","r") as f:
            cnt = f.readlines()
            cnt1 = [line.split() for line in cnt]
            file =  open("./data/network/local_ip.txt","w") 
            for i in range(0,len(cnt)):
                self.host_ip = cnt1[i][1] 
                file.writelines(self.host_ip+"\n")
            file.close()


        

oni = ONI_NET()
oni.stage_sep()
