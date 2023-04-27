import os
def separate_vul_1(x):

    with open(x,"r") as f:
        lines = [line.rstrip('\n') for line in f]

    count_http = 0
    count_ftp = 0
    count_telnet = 0
    count_ssh = 0
    count_mysql = 0

    for i in range(len(lines)):
        if "http_version" in lines[i]:
            http_in_line = i+1
            for stop in range(http_in_line,1000):
                end_point = lines[stop]
    
                if "100%" in end_point:
                    count_http = stop
                    break
            with open("./data/separate_1/msf_http.txt","w") as m:
                for i in range(http_in_line,count_http):
                    m.writelines(lines[i]+"\n")
        else:
            pass

    for j in range(len(lines)):
        if "ftp_version" in lines[j]:
            ftp_in_line = j+1
            for stop1 in range(ftp_in_line,1000):
                end_point1 = lines[stop1]
                
                if "100%" in end_point1:
                    count_ftp = stop1
                    break
            with open("./data/separate_1/msf_ftp.txt","w") as m:
                for i in range(ftp_in_line,count_ftp):
                    m.writelines(lines[i]+"\n")
        else:
            pass
    for k in range(len(lines)):
        if "telnet_version" in lines[k]:
            telnet_in_line = k+1
            for stop4 in range(telnet_in_line,1000):
                end_point4 = lines[stop4]

                if "100%" in end_point4:
                    count_telnet = stop4
                    break
            with open("./data/separate_1/msf_telnet.txt","w") as m:
                for i in range(telnet_in_line,count_telnet):
                    m.writelines(lines[i]+"\n")
        else:
            pass

    for l in range(len(lines)):
        if "mysql_login" in lines[l]:
            mysql_in_line = l+1
            for stop3 in range(mysql_in_line,1000):
                end_point3 = lines[stop3]
                if "100%" in end_point3:
                    count_mysql = stop3
                    break
            with open("./data/separate_1/msf_mysql.txt","w") as m:

                for i in range(mysql_in_line,count_mysql):
                    m.writelines(lines[i]+"\n")

        else:
            pass       

    for m in range(len(lines)):
        if "ssh_version" in lines[m]:
            ssh_in_line = m+1
            for stop2 in range(ssh_in_line,1000):
                end_point2 = lines[stop2]
                if "100%" in end_point2:
                    count_ssh = stop2
                    break
            with open("./data/separate_1/msf_ssh.txt","w") as m:

                for i in range(ssh_in_line,count_ssh):
                    m.writelines(lines[i]+"\n")

        else:
            pass




def separate_vul_2():
    try:
        with open("./data/separate_1/msf_http.txt","r") as f:
            lines = [line.rstrip('\n') for line in f]
    except:
        pass

    try:
        with open("./data/separate_1/msf_ftp.txt","r") as f:
            lines1 = [line.rstrip('\n') for line in f]
    except:
        pass
    
    try:
        with open("./data/separate_1/msf_ssh.txt","r") as f:
            lines2 = [line.rstrip('\n') for line in f]
    except:
        pass
    
    try:
        with open("./data/separate_1/msf_telnet.txt","r") as f:
            lines3 = [line.rstrip('\n') for line in f]
    except:
        pass

    try:
        with open("./data/separate_1/msf_mysql.txt","r") as f:
            lines4 = [line.rstrip('\n') for line in f]
    except:
        pass

    try:

        for i in range(len(lines)):
            if "run" in lines[i]:
                run_in_line = i+1
                break
        with open("./data/separate_2/msf_http.txt","w") as f:
            for j in range(run_in_line,len(lines)):
                f.writelines(lines[j]+"\n")
    except:
        pass
    
    try:

        

        for ij in range(len(lines1)):
            if "run" in lines1[ij]:
                run_in_line1 = ij+1
                break
        with open("./data/separate_2/msf_ftp.txt","w") as f:
            for j in range(run_in_line1,len(lines1)):
                f.writelines(lines1[j]+"\n")
    except:
        pass

   



    try:    
    
        for ik in range(len(lines2)):
            if "run" in lines2[ik]:
                run_in_line2 = ik+1
                break

        with open("./data/separate_2/msf_ssh.txt","w") as f:
            for j in range(run_in_line2,len(lines2)):
                f.writelines(lines2[j]+"\n")
    except:
        pass
    
    try:
        for il in range(len(lines3)):
            if "run" in lines3[il]:
                run_in_line3 = il+1
                break

        with open("./data/separate_2/msf_telnet.txt","w") as f:
            for j in range(run_in_line3,len(lines3)):
                f.writelines(lines3[j]+"\n")
    except:
        pass
    try:
        for im in range(len(lines4)):
            if "run" in lines4[im]:
                run_in_line4 = im+1
                break

        with open("./data/separate_2/msf_mysql.txt","w") as f:
            for j in range(run_in_line4,len(lines4)):
                f.writelines(lines4[j]+"\n")

    except:
        pass
def overall(x):

    string1 = "\n------------HTTP(esa11) Version Report---------------\n"
    string2 = "\n------------FTP(esa12)  Version Report---------------\n"
    string3 = "\n------------SSH(esa13)  Version Report---------------\n"
    string4 = "\n------------TELNET(esa14) Version Report---------------\n"
    string5 = "\n------------MYSQL(esa21) Version Report---------------\n"


    try:

        with open("./data/separate_2/msf_http.txt","r") as a:
            content1 = a.read()
    except:
        string1 = ""
        content1 = ""
        
    
    try:

        with open("./data/separate_2/msf_ftp.txt","r") as b:
            content2 = b.read()
    except:
        string2 = ""
        content2 = ""

    try:
        with open("./data/separate_2/msf_telnet.txt","r") as c:
            content4 = c.read()
    
    except:
        string4 = ""
        content4 = ""
    
    try:
        with open("./data/separate_2/msf_ssh.txt","r") as d:
            content3 = d.read()
    
    except:
        content3 = ""
        string3 = ""

    try:

        with open("./data/separate_2/msf_mysql.txt","r") as e:
            content5 = e.read()
    
    except:
        string5 = ""
        content5 = ""

    with open(x,"w") as app:
        app.writelines(string1+content1+"\n"+string2+content2+"\n"+string4+content3+"\n"+string3+content4+"\n"+string5+content5+"\n")         

   
def gobust(x,y):
    path = "./data/overall_vul/"+y+"_auxiliary_scan_overall.txt"
    check = os.path.isfile(path)

    if check == True:
        with open("./data/overall_vul/"+y+"_auxiliary_scan_overall.txt","r") as f:
            content = f.read()
            if "esa11" in content:
                print("Just exit at a point you want.. ")
                process=os.system("gobuster dir -u http://"+x+"/ -w ./data/directory-medium.txt -o ./data/gobust/gobuster_"+y+".txt")
            else:
                with open("./data/gobust/gobuster_"+y+".txt","w") as f:
                    f.writelines("\nDictionary enumerations show no findings\n\n")

    else:
        print("no")



    path1 = "./data/gobus/gobuster_"+y+".txt"
    check1 = os.path.isfile(path1)
    if check1 == True:
        pass
    else:
        with open("./data/gobuster_"+y+".txt","w") as f:
            pass
        print("gobuster attack is not possible at this situation")






