from datetime import datetime
import os
import paramiko

today = datetime.today().strftime("%Y%m%d%H%M")
b_today = datetime.today().strftime("%Y%m%d")

################################################################################

up_file = "/WEB-INF/classes/mall/sql/xml/Product.xml"
#up_file = "/WEB-INF/"

################################################################################

_find = up_file.rfind('/')
source_find = up_file[_find:len(up_file)]

# print(source_find)
# 경로 Make
local_temp = "D:/YT_PROJECT/workspace/fmall_backup/src/main/webapp"
server_temp = "/home/tomcat/market"

local = f"{local_temp}{up_file}"
server = f"{server_temp}{up_file}"
#print(server)

b_today_local = f"C:/Users/treed/Desktop/운영서버 반영 및 백업(개발전)/청정/백업/{b_today}"
b_local = f"C:/Users/treed/Desktop/운영서버 반영 및 백업(개발전)/청정/백업/{b_today}/{today}"

# 서버 접속 정보

yt = ""
ytuser = ""
ytpwd = ""

# paramiko 접속
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

def connect_server():
    try:
        ssh.connect(cj, username=cjuser, password=cjpwd)
        print('ssh connected. \n')

    except Exception as err:
        print(err)

def dist_backup():
    createFolder(b_today_local)
    createFolder(b_local)
    try:
        sftp = ssh.open_sftp()
        sftp.get(server, f"{b_local}{source_find}")
        print(f"{b_local}{source_find}")
        print(f'{server} backup success \n')

    except Exception as err:
        print(err)

def dist_reflection():
    try:
        sftp = ssh.open_sftp()
        sftp.put(local, server)
        print(f'{local} upload success \n')

    except Exception as err:
        print(err)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
connect_server()
dist_backup()
#함수명을 'f2'를 눌러서 수정해주면 사용하는 위치의 함수명도 자동으로 수정

dist_reflection()
# 반영 함수이기 때문에 주의해서 사용해야 함. 
# 반영 직전까지는 무조건 주석처리 해놓는 것이 원칙.

ssh.close()
