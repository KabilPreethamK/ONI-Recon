import os
from msf_grab import separate_vul_1, overall, separate_vul_2, gobust
import glob
from gtts import gTTS
import os
from playsound import playsound
def convey(a):
    tts = gTTS(text=a, lang='en')
    tts.save("hello.mp3")
    playsound("hello.mp3")
    os.remove("hello.mp3")
    print(a)
    


class hack_manual:

   


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
        self.target_cmd = input("|O|N|I|[Hacking-Automatic]['What is the target ip']~~> ")

    def target_name(self):
        var = "|O|N|I|[Hacking-Automatic", self.target_cmd, "['What is the assesment name(eg: test)']~~> "   
        self.target_name_cmd = input(var)

    def process(self):
        

        response = os.system("ping -c 1 " + self.target_cmd + " > ./Assessments/"+self.actuall_folder+"/Ping.txt")
        if response == 0:
            convey("The Target it responding and sending packets.Target is alive.")
            convey("Proceeding network layer scan with nmap.This may take time.")
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
                        convey("Http is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line1 = g.writelines("use auxiliary/scanner/http/http_version \n")
                            line2 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line3 = g.writelines("run\n")

                    if ports == "21/tcp":
                        convey("Ftp is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/ftp/ftp_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports == "22/tcp":
                        convey("ssh is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/ssh/ssh_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports == "23/tcp":
                        convey("Telnet is open.")
                        with open("./data/rc/"+self.actuall_folder+"_msf.rc", "a") as g:
                            line4 = g.writelines("use auxiliary/scanner/telnet/telnet_version \n")
                            line5 = g.writelines("set rhosts "+self.target_cmd+"\n")
                            line6 = g.writelines("run\n")

                    if ports == "3306/tcp":
                        convey("Mysql is running and port is open.")
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
                    convey("Gobuster cannot run on this IP.")
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
            convey("Network Error")


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
            convey("Some error occured. Try redoing")

    def show_report(self):
        cmd = input("Do you want to show the report? (y/n)~~> ")
        if "y" in cmd:
            with open("./Reports/Report_"+self.actuall_folder+".txt", "r") as f:
                print(f.read())
        else:
            pass

x = finall_Report()
x.check_sep1()
x.check_sep2()
x.check_rc()
x.check_overall()
x.check_vulnerable()
x.ascii()
x.target()
x.target_name()
x.edit_()
x.process()
try:
    x.report()
    x.Adding_report()
except:
    convey("some error skipping machine")
x.final_report() 
