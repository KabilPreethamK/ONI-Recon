import os
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
class maindish:

    cmd = input("Do You Want Voice Assist (y|n) >>")
    if "y" in cmd:
        def show(self,a):
            convey(a)
    else:
        def show(self,a):
            print(a)
    
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
    def start_menu(self):

        while True:
            
            self.menu_cmd = input("|O|N|I|[Hacking]~~> ").lower()
            if "exit" in self.menu_cmd:
                break
            
            if "options" in self.menu_cmd or "help" in self.menu_cmd:
                self.show("Type auto for Automatic reconnaissance and for manual type manual.")
                print("1-Automatic reconnaissance  -------> Assessment held by ONI---- To use type 'auto'")
                print("2-Manual Targeting  -------> Assessment held by you---- To use type 'manual'")
                print("3-iplist -------> shows the machines active in local network.")

                continue

            if "iplist" in self.menu_cmd:
                with open("./data/network/local_ip.txt","r") as f:
                    content = f.read()
                    print("\n",content,"\n")
                continue
                

            if "manual" in self.menu_cmd:
                from oni_manual import finall_Report 
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
                    print("some error skipping machine")
                x.final_report() 
                continue

            if "auto" in self.menu_cmd:
                with open("./data/network/local_ip.txt","r") as f:
                    lines = [line.rstrip('\n') for line in f]
                    machine = input("Give this Assessment a name: ")

                from oni_auto import finall_Report
                x = finall_Report()
                x.check_sep1()
                x.check_sep2()
                x.check_rc()
                x.check_overall()
                x.check_vulnerable()
                x.ascii()
                for i in range(0,len(lines)):
                    
                    x.target(lines[i])
                    x.target_name(machine)
                    x.edit_()
                    x.process()
                    try:
                        x.report()
                        x.Adding_report()
                    except:
                        print("some error skipping machine")
                x.final_report() 
                continue

            else:
                os.system(self.menu_cmd)
            



class main(maindish):

    
    def __init__(self):
        pass

    def display(self):
        playsound("./data/gtts/Oni_Startup.mp3")
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
            if "empty" in self.command or "clean" in self.command:
                os.system("rm -f -r ./Assessments/*")
                os.system("rm -f ./Reports/*")
                os.system("rm -f ./data/gobust/*")
                os.system("rm -f ./data/network/*")
                os.system("rm -f ./data/overall_vul/*")
                os.system("rm -f ./data/rc/*")
                os.system("rm -f ./data/seperate_1/*")
                os.system("rm -f ./data/seperate_2/*")
                os.system("rm -f ./data/stage/*")
                os.system("rm -f ./data/vulnerabilities/*")
                continue
            if "recon" == self.command:
                self.show("Welcome To O N I Reconnaissance")
                x = maindish()
                x.stage1()
                x.start_menu()
                print("Type Options to proceed.")
                continue
            if "exit" in self.command:
                self.show("See You later..")
                break

            if "help" in self.command or "options" == self.command:
                self.show("Here are the options available.To start oni type recon.")
                print("\n\n------------------ONI HELPS YOU------------\n")
                print("\n1.empty/clean ----------------- Delete and empty the folders of all reports of scanners etc.")
                print("2.exit            ----------------- return to the terminal.")
                print("3.about           ----------------- Discription about oni.")
                print("4.recon           ----------------- Oni begins\n\n")
                print("5.Oni allows you to use general commands of linux.\n\n")
                

                continue

            if "about" == self.command:
                with open("./data/oni.txt","r") as f:
                    content = f.read()
                cmd = input("Do you wish to play the audio file?(2.03 min) [y|n]:")
                if "y" in cmd:

                    playsound("./data/gtts/about.mp3")
                    print("\n",content,"\n")
                else:
                    print("\n",content,"\n")

            else:
                os.system(self.command)

x = main()
x.display()
x.cmd()