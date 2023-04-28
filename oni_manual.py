import os
from msf_grab import separate_vul_1, overall, separate_vul_2, gobust
import glob
from gtts import gTTS
import os
from playsound import playsound







def convey(a):
    tts = gTTS(text=a, lang='en-us')
    tts.save("hello.mp3")
    playsound("hello.mp3")
    os.remove("hello.mp3")
    print(a)
    
def welcome():
    playsound("./data/gtts/Oni_Startup.mp3")


class hack_manual:
    cmd = input("Voice or text? >>")
    if "voice" in cmd:
        def show(self,a):
            convey(a)
    else:
        def show(self,a):
            print(a)
    

   


    def __init__(self) -> None:
        pass

   



    def check_sep1(self):
        _, _, files = next(os.walk("./data/separate_1/"))
        file_count = len(files)
        if file_count > 0:
            os.system("rm -f ./data/separate_1/*")
        else:
            pass

    def check_sep2(self):
        _, _, files = next(os.walk("./data/separate_2/"))
        file_count = len(files)
        if file_count > 0:
            os.system("rm -f ./data/separate_2/*")
        else:
            pass

    def check_rc(self):

        _, _, files = next(os.walk("./data/rc/"))
        file_count = len(files)

        if file_count > 5:
            cmd = input("Rc folder contains files more than 5. Do you want to clean the dictionary(recomended=yes) y or n ? ~~> ")
            if "y" in cmd:
                os.system("rm -f ./data/rc/*")
            if "n" in cmd:
                pass
        else:
            pass

    def check_vulnerable(self):

        _, _, files = next(os.walk("./data/vulnerabilities/"))
        file_count = len(files)
        if file_count > 5:
            cmd = input("Vulnerabilities folder contains files more than 5. Do you want to clean the dictionary(recomended=yes) y or n ? ~~> ")
            if "y" in cmd:
                os.system("rm -r ./data/vulnerabilities/*")

            if "n" in cmd:
                pass
        else:
            pass

    def check_overall(self):

        _, _, files = next(os.walk("./data/overall_vul/"))
        file_count = len(files)
        if file_count > 5:
            cmd = input("Overall_vulnerabilities folder contains files more than 5. Do you want to clean the dictionary(recomended=yes) y or n ? ~~> ")
            if "y" in cmd:
                os.system("rm -r ./data/overall_vul/*")

            if "n" in cmd:
                pass
        else:
            pass

    def target(self):
        self.show("Enter the IP address of the system.")
        self.target_cmd = input("|O|N|I|[Hacking-Manual]['What is the target ip']~~> ")
        self.show(self.target_cmd+" is set as target.")

    def target_name(self):
        self.show("Enter the Name of the target.Note! folder containing scan reports is named after this.")
        var = "|O|N|I|[Hacking-Automatic", self.target_cmd, "['What is the assesment name(eg: test)']~~> "   
        self.target_name_cmd = input(var)
        self.show(self.target_name_cmd+" is set as name of the target.")

    def process(self):
        

        response = os.system("ping -c 1 " + self.target_cmd + " > ./Assessments/"+self.actuall_folder+"/Ping.txt")
        if response == 0:
            self.show("The Target is responding and sending packets.Target is alive.")
            self.show("Proceeding network layer scan with nmap.This may take time.")
            os.system("nmap -sV "+self.target_cmd+" > ./Assessments/" +self.actuall_folder+"/Nmap_Result")
            sep_content1 = []
            with open("./Assessments/"+self.actuall_folder+"/Nmap_Result", "r") as f:
                content = f.readlines()
                for i in range(5, len(content)-2):
                    sep_content = content[i].split()
                    sep_content1.append(sep_content)
                for j in range(0, len(sep_content1)-1):
                    ports = sep_content1[j][0]
                    

                # starts with http
                    if ports == "80/tcp":
                        self.show("Http is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line1 = g.writelines("use auxiliary/scanner/http/http_version \n")
                            line2 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line3 = g.writelines("run\n")

                    if ports == "21/tcp":
                        self.show("Ftp is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/ftp/ftp_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports == "22/tcp":
                        self.show("ssh is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/ssh/ssh_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports == "23/tcp":
                        self.show("Telnet is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/telnet/telnet_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports == "3306/tcp":
                        self.show("Mysql is running and port is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/mysql/mysql_login \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                    line1 = g.writelines("exit")

                os.system("msfconsole -r ./data/rc/"+self.actuall_folder +"_msf.rc -o ./data/vulnerabilities/"+self.actuall_folder+"_vulnerable.txt")
                separate_vul_1("./data/vulnerabilities/" +self.actuall_folder+"_vulnerable.txt")
                separate_vul_2()
                overall("./data/overall_vul/"+self.actuall_folder +"_auxiliary_scan_overall.txt")
                try:
                    gobust(self.target_cmd, self.actuall_folder)
                except:
                    self.show("Gobuster cannot run on this IP.")
                os.system("mkdir ./Assessments/"+self.actuall_folder+"/Gatherings/")
                os.system("cp ./data/overall_vul/" + self.actuall_folder +"_auxiliary_scan_overall.txt "+"./Assessments/"+self.actuall_folder+"/Gatherings/")
                os.system("cp ./data/gobust/gobuster_"+self.actuall_folder +".txt "+"./Assessments/"+self.actuall_folder+"/Gatherings/")
                os.system("cp ./data/rc/"+self.actuall_folder +"_msf.rc "+"./Assessments/"+self.actuall_folder+"/Gatherings/")
                os.system("cp -r ./data/separate_1/ "+"./Assessments/"+self.actuall_folder)
                os.system("cp -r ./data/separate_2/ "+"./Assessments/"+self.actuall_folder)
                try:
                    os.system("chmod a+rw -R ./Reports/*")
                    os.system("chmod a+rw -R ./Assessments/*")
                    os.system("chmod a+rw -R ./data/*")
                except:
                    pass

        else:
            self.show("Network Error. Network is down or firewall is blocking our ping request")


    def edit_(self):
        if not os.path.exists("./Assessments/"+self.target_name_cmd):
            os.makedirs("./Assessments/"+self.target_name_cmd)
            self.actuall_folder = self.target_name_cmd
        else:
            for i in range(1, 100):
                add_folder = self.target_name_cmd+str(i)
                if not os.path.exists("./Assessments/"+add_folder):
                    os.makedirs("./Assessments/"+add_folder)
                    self.actuall_folder = add_folder
                    break
                else:
                    pass

        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "w") as create1:
            pass

        with open("./data/vulnerabilities/"+self.actuall_folder+"_vulnerable.txt", "w") as create2:
            pass
        with open("./Assessments/"+self.target_name_cmd+"/Target.txt", "w") as f:
            line = "\n\n----------------Target-"+self.target_cmd+"-------------------\n"
            f.writelines(line)


class finall_Report(hack_manual):

    def ascii(self):
        with open("./data/ascii.txt","w")as f:
            l1 = f.write(".oPYo. o    o o        .oPYo.                            \n")
            l2 = f.write("8    8 8b   8 8        8   `8                            \n")
            l2 = f.write("8    8 8`b  8 8       o8YooP' .oPYo. .oPYo. .oPYo. odYo. \n")
            l2 = f.write("8    8 8 `b 8 8 ooooo  8   `b 8oooo8 8    ' 8    8 8' `8 \n")
            l2 = f.write("8    8 8  `b8 8        8    8 8.     8    . 8    8 8   8 \n")
            l2 = f.write("`YooP' 8   `8 8        8    8 `Yooo' `YooP' `YooP' 8   8 \n")
            l2 = f.write(":.....:..:::....:::::::..:::..:.....::.....::.....:..::..\n")
            l2 = f.write(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            l2 = f.write(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n\n")

    def Adding_report(self):
        report = open("./Reports/Report_"+self.actuall_folder+".txt", "r")
        with open("./Reports/Final_Report.txt", "a") as f:
            line = "----------------Target-"+self.target_cmd+"-------------------\n"
            f.writelines(line)
            cont = f.writelines(report)
            report.close()
        
        
    def final_report(self):
        try:
            asciii = open("./data/ascii.txt",'r')
            reports = open("./Reports/Final_Report.txt",'r')
            create = open("./Reports/Final_"+self.target_name_cmd+"_report.txt" ,"w")

            with open("./Reports/Final_"+self.target_name_cmd+"_report.txt","a") as f:
                f.writelines(asciii)
                f.writelines(reports)
                asciii.close()
                reports.close()
                create.close()
                os.system("rm -f ./Reports/Final_Report.txt")
                
        except:
            pass
            


    def report(self):
        #try:
            with open("./Reports/Report_"+self.actuall_folder+".txt", "w") as f, open("./Assessments/"+self.actuall_folder+"/Nmap_Result", "r") as h, open("./Assessments/"+self.actuall_folder+"/Ping.txt", "r") as i, open("./Assessments/"+self.actuall_folder+"/Gatherings/"+self.actuall_folder+"_auxiliary_scan_overall.txt", "r") as j:

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
                    with open("./Assessments/"+self.actuall_folder+"/Gatherings/gobuster_"+self.actuall_folder+".txt", "r") as k:
                        l2 = f.write("\n\n")
                        l2 = f.write(">>>>>>>>> Dictionary Enumeration:\n\n")

                        for lines in k:
                            f.write(lines)
                except:
                    with open("./data/gob.txt", "r") as k:
                        l2 = f.write("\n\n")
                        l2 = f.write(">>>>>>>>> Dictionary Enumeration:\n\n")
                        f.writelines(k)

                    

                    pass
            os.system("rm -f ./data/overall_vul/*")
            os.system("rm -f ./data/rc/*")
            os.system("rm -f ./data/vulnerabilities/*")
            os.system("rm -f ./data/separate_1/*")
            os.system("rm -f ./data/separate_2/*")
            self.show("Some error occured. Try redoing")

    def show_report(self):
        cmd = input("Do you want to self.show the report? (y/n)~~> ")
        if "y" in cmd:
            with open("./Reports/Report_"+self.actuall_folder+".txt", "r") as f:
                print(f.read())
        else:
            pass

class summary_manual(finall_Report):
    def open_file(self):
        with open("./Reports/Final_msfadmin_report.txt","r") as report:
            self.cont = report.readlines()
            print(len(self.cont))
    
    with open("summary.txt","w") as f:
        cont = f.writelines("---------------------------------> SUMMARY <---------------------------------\n")
        cont = f.writelines(" ")