#! usr/bin/env python
#! coding:utf-8

# 子网划分：现有两个 C 类网，202.203.204.0 和 202.203.224.0，分别把它们平均分成 4 个（子网号2位）和 8 个（子网号3位）子网，写出每个子网的起始、终结 IP 和子网掩码。
# 下次任务：添加--1.输入纠错，2.IP地址段起始到终止显示
"""network 1.0
Usage:
  network.py -i <ip> -m <mask>...

Options:
  -h --help     Show this screen.
  -i      	Input IP address
  -m		Input mask
"""

import sys,getopt
from docopt import docopt

# 输入一个二进制数，返回十六进制数、
def bin2hex(bin):
    return hex(int(bin,2))
# 输入一个十六进制数，返回一个二进制数
def hex2bin(hexl):
    hexstr = str(hexl)
    num = int(hexstr,16)
    bit = []
    while True:
        if num == 0:break
        num,rem = divmod(num,2)
        bit.append(str(rem))
    return ''.join(bit[::-1])

# 输入一个十进制数，返回二进制数
def dec2bin(dec):
    decstr = str(dec)
    num = int(decstr,10)
    bit = []
    while True:
        if num == 0:break
        num,rem = divmod(num,2)
        bit.append(str(rem))
    return ''.join(bit[::-1])
# 输入一个二进制数，返回十进制数
def bin2dec(bin):
    return int(bin,2)

# 二进制数的逻辑与，或，取反，异或，右移位，左移位计算符 & | ~ ^ >> <<

def calcIP(cnetip,mask):
# IP地址分成四份，每份转化为二进制地址，与子网掩码进行逻辑与运算
	# 把IP地址按小数点号分成四份
    cnet = str(cnetip).split(".")
	# 主机号是第四组ip
    hostip = int(cnet[3])
	# 转为二进制以便于之后的计算
	# 子网掩码转为10进制数
    mask_dec = int(mask)
	# 获取子网个数，转为二进制位数
    mask_bin = dec2bin(mask_dec-1) # 11,111
    mask_bin_str = str(mask_bin)   #'11','111'
    mask_count = len(mask_bin_str) # 2,3
    mask_str = '{0:0<8}'.format(mask_bin_str) #'11000000' ,'11100000'
    maskdec = int(mask_str,2)

    netip = hostip & maskdec # 计算
    ips = '{0:0>8}'.format(netip)
    maskip = ips[:mask_count]
    hostips = ips[mask_count:]
    hostseg = cnet[0]+'.'+cnet[1]+'.'+cnet[2]+'.'+str(int(ips,10))
    return maskip,hostips,hostseg

if __name__ == "__main__":
    arguments = docopt(__doc__,version='network 1.0')
# IP 地址就可看作 IP = 网络号 + 子网号 + 主机号
    opts, args = getopt.getopt(sys.argv[1:], "hi:m:")
    cnetip = ""
    mask = ""
    for op,value in opts:
	if op == "-i":
	    cnetip = value
	elif op == "-m":
	    mask = value
        elif op == "-h":
	    print(arguments)
	    sys.exit()
    maskip,hostip,hostseg = calcIP(cnetip,mask)
    print('子网掩码='+str(maskip))
    print('主机起始地址='+str(hostip))
    print('IP地址起始='+str(hostseg))
