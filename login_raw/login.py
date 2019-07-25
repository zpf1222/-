# 与用户交互 让用户选择机器
import os


def read_ip():
    # 循环读取选择ip地址
    ip_dic = {}
    num = 0
    with open("ip.txt", mode="r", encoding='utf8') as f:
        while 1:
            num += 1
            line = f.readline()
            if len(line) == 0:
                break
            ip_dic[num] = line
    f.close()
    while 1:
        # 循环字典读取ip地址
        for k, v in ip_dic.items():
            print("%s. %s" % (k, v))
        # 输入key，选择ip地址
        option = int(input("请输入主机编号："))
        if option in ip_dic.keys():
            print(ip_dic[option])
            user = input("username:").strip()
            cmd = "ssh %s@%s" % (user, ip_dic[option])
            os.system(cmd)
        else:
            print("请输入编号")
            continue


if __name__ == '__main__':
    read_ip()
