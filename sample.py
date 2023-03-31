import os
def final_report():
        asciii = open("./data/ascii.txt",'r')
        reports = open("./Reports/Final_Report.txt",'r')

        with open("./Reports/Final_Kabil_report.txt","a") as f:
            f.writelines(asciii)
            f.writelines(reports)
            asciii.close()
            reports.close()
          
            os.system("rm -f ./Reports/Final_Report.txt")

final_report()