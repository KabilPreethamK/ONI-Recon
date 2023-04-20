class summary_manual:

    def auxiliary(self):
        with open("./Assessments/msfadmin/Gatherings/msfadmin_auxiliary_scan_overall.txt","r") as f:
            
            content= f.readlines()
            length = len(content)
            for i in range(1, length):
                #print(content[i])
                grab = content[i]
                if "esa11" in grab:
                    grab_final=content[i+1].split(" ")
                    join = grab_final[2:]
                    print(" ".join(join))


    def open_file(self):
        with open("./Assessments/family/Ping.txt","r") as ping:
            self.cont=ping.readlines()
            self.cont = [x.replace("time="," ").split() for x in self.cont]
            self.ping_res = self.cont[1]
            self.final_res = str(self.ping_res[6])
        with open("./Assessments/msfadmin/Nmap_Result","r") as f:
            content = f.readlines()
            sep_content1 = []
            self.lists=[]
            self.lists2=[]
            self.version_count = []
            for i in range(5, len(content)-2):
                sep_content = content[i].replace("/tcp"," ").split()
                sep_content1.append(sep_content)
            
            for j in range(0, len(sep_content1)-1):
                ports = sep_content1[j][0]
                self.edited_ports = "[+]"+ports
                self.lists.append(self.edited_ports)
            for k in range(0,len(sep_content1)):
                inter_cont = len(sep_content1[k])
                inner_count1 = inter_cont-3
                self.version_count.append(inner_count1)
                for l in range(3,inter_cont):
                    adf = self.lists2.append(sep_content1[k][l])
            #print(self.version_count)
            #for k in range(0, len(sep_content1)-1):
                #version = sep_content1[j][3]
                #self.edited_version = "[+]"+version
                #self.lists2.append(self.edited_version)
                #print(self.lists2)
    def nmap(self):
        with open("./Assessments/msfadmin/Nmap_Result","r") as f:
            lists = []
            cont = f.readlines()
            content = [x.split() for x in cont]
            for i in range(5,len(cont)-4):
                scan=cont[i].replace(cont[i][0:15]," ")
                lists.append(scan)    
    
    
        
    def summary(self):
        with open("summary.txt","w") as f:
            cont = f.write("---------------------------------> SUMMARY <---------------------------------\n")
            cont = f.write("$From the above reconnaissance done by ONI it is declared that the target is responding and sending back the packets in the time of "+self.final_res+" milliseconds. This shows that the firewall is not blocking our ping. \n")
            cont = f.write("On running nmap the obtained open ports are:\n\n")
            count = 0
            count1 = 0
            for ports in self.lists:
                count = count+1
                l=str(ports)+"\n".join(" ")
                cont = f.writelines(l)
            cont  = f.writelines("\n\n$These are the open ports that are running behind the target,the versions of the ports running in the backgrounds are separately scratched and saved as in map results inside the folder of assessments of the given Target name (location : ./Assessments/yourtargetname/Nmap_Result) \n\n")
            for versions in self.lists2:
                count1 = count1+1
                l = str(versions)+"\n".join(" ")
                cont = f.writelines(l) 
            cont = f.writelines("\n\n$But for further informations oni uses auxiliary scanners with the help of metasploitable toolkit , so that we can obtain the versions of the ports\n")
            #print(self.lists2)
            
    

   
            
x = summary_manual()
x.auxiliary()
#x.open_file()
#x.nmap()
#x.summary()
