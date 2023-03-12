import os 
from msf_grab import separate_vul_1 , overall , separate_vul_2 , gobust
import glob
class hack_auto:

    def __init__(self) -> None:
        pass
    
    def check_sep1(self):
        _, _, files = next(os.walk("./msfconsole/separate_1/"))
        file_count = len(files)      
        if file_count > 0:           
            os.system("rm -f ./msfconsole/separate_1/*")
        else:
            pass
    
    def check_sep2(self):
        _, _, files = next(os.walk("./msfconsole/separate_2/"))
        file_count = len(files)      
        if file_count > 0:           
            os.system("rm -f ./msfconsole/separate_2/*")
        else:
            pass



    def check_rc(self):

        _, _, files = next(os.walk("./msfconsole/rc/"))
        file_count = len(files)
        
        if file_count > 5:
            cmd = input("Rc folder contains files more than 5. Do you want to clean the dictionary(recomended=yes) y or n ? ~~> ")
            if "y" in cmd:
                os.system("rm -f ./msfconsole/rc/*")
            if "n" in cmd:
                pass
        else:
            pass

    def check_vulnerable(self):

        _, _, files = next(os.walk("./msfconsole/vulnerabilities/"))
        file_count = len(files)
        if file_count >5:
            cmd = input("Vulnerabilities folder contains files more than 5. Do you want to clean the dictionary(recomended=yes) y or n ? ~~> ")
            if "y" in cmd:
                os.system("rm -r ./msfconsole/vulnerabilities/*")
                
            if "n" in cmd:
                pass
        else:
            pass
    
    def check_overall(self):

        _, _, files = next(os.walk("./msfconsole/overall_vul/"))
        file_count = len(files)
        if file_count >5:
            cmd = input("Overall_vulnerabilities folder contains files more than 5. Do you want to clean the dictionary(recomended=yes) y or n ? ~~> ")
            if "y" in cmd:
                os.system("rm -r ./msfconsole/overall_vul/*")
                
            if "n" in cmd:
                pass
        else:
            pass
                

    def target(self):
        self.target_cmd = input("|O|N|I|[Hacking-Automatic]['What is the target ip']~~> ")
    
    def target_name(self):
        var = "|O|N|I|[Hacking-Automatic",self.target_cmd,"['What is the assesment name(eg: test)']~~> "
        self.target_name_cmd = input(var)

    def process(self):       
        if not os.path.exists(self.target_name_cmd):
            os.makedirs(self.target_name_cmd)
            self.actuall_folder = self.target_name_cmd
        else:
            for i in range(1,100):
                add_folder = self.target_name_cmd+str(i)
                if not os.path.exists(add_folder):
                    os.makedirs(add_folder)
                    self.actuall_folder = add_folder
                    break
                else:
                    pass
        
        with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","w") as create1:
            pass

        with open("./msfconsole/vulnerabilities/"+self.actuall_folder+"_vulnerable.txt","w") as create2:
            pass
        
        response = os.system("ping -c 1 " + self.target_cmd+ " > ./"+self.actuall_folder+"/Ping.txt")
        if response == 0:
            print("Network Active")
            print("Proceeding layer scan with nmap.. This may take time..")
            os.system("nmap -sV "+self.target_cmd+" > ./"+self.actuall_folder+"/Nmap_Result")
            sep_content1 = []
            with open("./"+self.actuall_folder+"/Nmap_Result","r") as f:
                content = f.readlines()
                for i in range(5,len(content)-2):
                    sep_content = content[i].split()
                    sep_content1.append(sep_content)           
                for j in range(0,len(sep_content1)-1):
                    ports = sep_content1[j][0]


                # starts with http
                    if ports == "80/tcp":
                        print("Http is open.")
                        with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","a") as g:
                            line1 = g.writelines("use auxiliary/scanner/http/http_version \n")
                            line2 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line3 = g.writelines("run\n")                                                    

                    if ports== "21/tcp":
                        print("Ftp is open.")
                        with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","a") as g:
                            line4 = g.writelines("use auxiliary/scanner/ftp/ftp_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")
                        
                    
                    if ports== "22/tcp":
                        print("ssh is open.")
                        with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","a") as g:
                            line4 = g.writelines("use auxiliary/scanner/ssh/ssh_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports== "23/tcp":
                        print("Telnet is open.")
                        with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","a") as g:
                            line4 = g.writelines("use auxiliary/scanner/telnet/telnet_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports== "3306/tcp":
                        print("Mysql is running and port is open.")
                        with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","a") as g:
                            line4 = g.writelines("use auxiliary/scanner/mysql/mysql_login \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")
                        
                with open("./msfconsole/rc/"+self.actuall_folder+"_msf.rc","a") as g:
                    line1 = g.writelines("exit")
                
                os.system("msfconsole -r msfconsole/rc/"+self.actuall_folder+"_msf.rc -o ./msfconsole/vulnerabilities/"+self.actuall_folder+"_vulnerable.txt")
                separate_vul_1("./msfconsole/vulnerabilities/"+self.actuall_folder+"_vulnerable.txt")
                separate_vul_2()
                overall("./msfconsole/overall_vul/"+self.actuall_folder+"_auxiliary_scan_overall.txt")
                gobust(self.target_cmd,self.actuall_folder)
                os.system("mkdir "+self.actuall_folder+"/Gatherings/")
                os.system("cp ./msfconsole/overall_vul/"+ self.actuall_folder +"_auxiliary_scan_overall.txt "+self.actuall_folder+"/Gatherings/")
                os.system("cp ./msfconsole/gobuster_"+self.actuall_folder+".txt "+self.actuall_folder+"/Gatherings/")
                os.system("cp ./msfconsole/rc/"+self.actuall_folder+"_msf.rc "+self.actuall_folder+"/Gatherings/")
                os.system("cp -r ./msfconsole/separate_1 "+self.actuall_folder)
                os.system("cp -r ./msfconsole/separate_2 "+self.actuall_folder)


                
                



        else:
            print("Network Error")

    def edit_(self):
        path = "./"+self.target_name_cmd+"/Target.txt"
        with open(path,"w") as f:
            line = "----------------Target-"+self.target_cmd+"-------------------"
            f.writelines(line)

class finall_Report(hack_auto):

    def report(self):
        with open("./Reports/Report_"+self.actuall_folder+".txt","w") as f , open("./"+self.actuall_folder+"/Target.txt","r") as g , open("./"+self.actuall_folder+"/Nmap_Result","r") as h,open("./"+self.actuall_folder+"/Ping.txt","r") as i, open("./"+self.actuall_folder+"/Gatherings/"+self.actuall_folder+"_auxiliary_scan_overall.txt","r") as j , open("./"+self.actuall_folder+"/Gatherings/gobuster_"+self.actuall_folder+".txt", "r") as k:
            l1 = f.write(".oPYo. o    o o        .oPYo.                            \n")
            l2 = f.write("8    8 8b   8 8        8   `8                            \n")
            l2 = f.write("8    8 8`b  8 8       o8YooP' .oPYo. .oPYo. .oPYo. odYo. \n")
            l2 = f.write("8    8 8 `b 8 8 ooooo  8   `b 8oooo8 8    ' 8    8 8' `8 \n")
            l2 = f.write("8    8 8  `b8 8        8    8 8.     8    . 8    8 8   8 \n")
            l2 = f.write("`YooP' 8   `8 8        8    8 `Yooo' `YooP' `YooP' 8   8 \n")
            l2 = f.write(":.....:..:::....:::::::..:::..:.....::.....::.....:..::..\n")
            l2 = f.write(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            l2 = f.write(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n\n")
            l2 = f.write("       Internet Protocol Adress of the target:\n\n")
            for lines in g:
                    f.write(lines)
            
            l2 = f.write("\n\n")
            l2 = f.write(">>>>>>>>> Ping response:\n\n")

            for lines in i:
                    f.write(lines)

            l2 = f.write("\n\n")
            l2 = f.write(">>>>>>>>> Nmap Result and Foundings:\n\n")

            for lines in h:
                    f.write(lines)

            l2 = f.write("\n\n")
            l2 = f.write(">>>>>>>>> Auxiliary scanners Report:\n\n")

            for lines in j:
                    f.write(lines)
            
            try:
                l2 = f.write("\n\n")
                l2 = f.write(">>>>>>>>> Dictionary Enumeration:\n\n")

                for lines in k:
                        f.write(lines)
            except:
                pass
            




class hacking:

    def start_menu(self):
        while True:
            self.menu_cmd = input("|O|N|I|[Hacking]~~> ").lower()
            if "exit" in self.menu_cmd:
                break
            if "options" in self.menu_cmd or "help" in self.menu_cmd:
                print("1-Automatic  -------> Assessment held by ONI---- To use type '1'")
            if "1" in self.menu_cmd:
                x = finall_Report()
                x.check_sep1()
                x.check_sep2()
                x.check_rc()
                x.check_overall()
                x.check_vulnerable()
                x.target()
                x.target_name()
                x.process()
                x.edit_()
                x.report()
            else:
                os.system(self.menu_cmd)
class main:
    def __init__(self):
        pass
    def display(self):
        print(" _______  _       _________     _______  _______  _______  _______  _       ")
        print("(  ___  )( (    /|\__   __/    (  ____ )(  ____ \(  ____ \(  ___  )( (    /|")
        print("| (   ) ||  \  ( |   ) (       | (    )|| (    \/| (    \/| (   ) ||  \  ( |")
        print("| |   | ||   \ | |   | | _____ | (____)|| (__    | |      | |   | ||   \ | |")
        print("| |   | || (\ \) |   | |(_____)|     __)|  __)   | |      | |   | || (\ \) |")
        print("| |   | || | \   |   | |       | (\ (   | (      | |      | |   | || | \   |")
        print("| (___) || )  \  |___) (___    | ) \ \__| (____/\| (____/\| (___) || )  \  |")
        print("(_______)|/    )_)\_______/    |/   \__/(_______/(_______/(_______)|/    )_)")
        print("\n")
        print("                  Developed by - KABIL PREETHAM K \n")
        print("         Git Hub :- https://github.com/KabilPreethamK \n")
    def cmd(self):
        while True:
            self.command = input("|O|N|I|~~> ").lower()
            if "hack" in self.command:
                x = hacking()
                x.start_menu()
            if "exit" in self.command:
                break

            if "help" in self.command:
                print("Type hack to see magic")
            
            else:
                os.system(self.command)


    

x = main()
x.display()
x.cmd()
