#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket, time, threading


socket.setdefaulttimeout(3)  # 设置默认超时时间


def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否占用
    """
    try:
        if port >= 65535:
            print('端口扫描结束')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print(ip, ':', port, '端口已占用')
            lock.release()
    except:
        print('端口扫描异常')


def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况, kwargs=(int(i))
    """
    try:
        print('开始扫描 %s' % ip)
        start_time = time.time()
        for i in range(0, 65534):
            mthread = threading.Thread(target=socket_port, args=(ip, int(i)))
            mthread.start()
            #   raw_input("Press Enter to Exit")
        print('扫描端口完成，总共用时：%.2fs' % (time.time() - start_time))
    except:
        print('扫描ip出错')


if __name__ == '__main__':
    url = input('Input the ip you want to scan: ')
    lock = threading.Lock()
    ip_scan(url)
