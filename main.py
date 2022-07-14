from colorama import Fore, Style, Back
from multiprocessing.dummy import Pool
import multiprocessing, time, datetime, ctypes
import re
import sys
import random
import time
import os
import datetime
import threading
import queue, time
from datetime import datetime , date
import requests, re, sys, random, os
from colorama.initialise import init
count = len(open('list.txt').readlines(  ))
countlive = 0
countdd = 0
countall2 = 0
countrec = 0

init(autoreset=True)
from random import choice

init()
class bounce():
    countlive = 0
    countdd = 0
    countall2 = 0
    countrec = 0
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    live = '"Status":"Valid"'.encode()
    die = '"Status":"Invalid"'.encode()
    inputQueue = queue.Queue()
    def __init__(self):            
        def slowprint(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1. / 10)
        def logo():
            fg = [
    '\033[91;1m',  # RED     0
    '\033[92;1m',  # GREEN   1
    '\033[93;1m',  # YELLOW  2
    '\033[94;1m',  # BLUE    3
    '\033[95;1m',  # MAGENTA 4
    '\033[96;1m',  # CYAN    5
    '\033[97;1m'  # WHITE   6
                ]
            os.system('cls')
            print(f""" 
[0;40;37m

[71C[1mÜ
[0m[71CÞÝ
[15C[31mÜÜÜ[41;37mÜÜÜÜÜ[40;31mÜÜÜÜ[37m[43C[31mÜ[1;47mÝ[0;41mÝ[0m
[11CÜ[1;31mÜ[47mÜÜ[40mÛÛÛÛÛÛÛÛÛÛ[47mÜÜ[41mÜÜ[0;41mÜÜ[40;31mÜÜÜÜÜ[37m[30C[31mÜÜ[1;41mÜÜÛ[0;41m²[1;31mÝ[0;31mÝ
[37m[9CÜ[1;31mÛÛÛÛ[41mßßßßßßßßßß[40mÛÛÛÛÛÛÛÛÛ[47mßß[40mÛ[41mÜÜÜÜÜÜ[0;31mÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ[1;41mÜÜÜ[40mÛÛ[47mÛßÜ[41mß[0;31mÛÝ
[37m[7C[31mÜ[1mÛÛ[41mß [0;31mÛßßßßßßßÛÛÛ[41m     [1mßßßß[40mÛÛÛ[47mÛÜÜÛÛÛßßßÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛß[41mÛÛß [0;31mÛÛ
[37m[6C[1;41;31mÞ[40mÛ[41mß[0;31mÛß[37m[12C[31mßßßÛÛÛÛÛÛÛÛ[41m  [1mßßßßß[40mÛ[47mÛÛÛÛÛ²²²²²±±±±°°°°°ÞÜÜ[40mÛ[41mßß  [0;31mÛÛÛ
[37m[5C[1;41;31mÞ[40mÛ[41m [0;31m²[37m[20C[31mßßßßÛÛÛÛÛÛÛÛ[41m      [1mßßßßßßßßßßßßßßß        [0;31mß
    [1mÞÛ[41m  [0m[29C[31mßßßßÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛßß
    [1mÞ[41mÝ[0;31mÛÝ[37m[30CÜþ[5C[31mßßßßÛÛÛÛÛÛÛÛÛÛÛßßß
    [1mÞ[41mÝ[0;31mÛÝ[37m[26CÜ[1;31mÜ[47mÜ[41mß[0;31mß[37m[6C[31mÜÜÜ[1;41m°°[40;30m°  [0mÝ
[5C[1;31mÛ[0;31mÛÝ[37m[23CÜ[1;47;31mÜ[40mÛÛ[41mß[0;31mß  ÜÜÜÛ[1;41m   °°°°[40;30m±  [0mÝ
[5C[1;31mÛ[0;31mÛÛ[37m[21CÜ[1;47;31mÜ[40mÛÛ[47mÛ[0;31mÛ[1;30m°    [41;31m [0;31mÛ[1;41m °°°°°°±[40;30m²  [0mÝ
[6C[1;31m²[41m  [40;30m [0m[17C[31mÜ[1;47mÞÛ[40mÛ[47mÛÛ[0;31mÛ[1;30m±[0m[5C[31mÞ[1;41m °°°°°°°±[40;30mÞ  [0mÝ
[7C[1;31mß[41m  [0;31mÜ [37m[14C[31mÛ[1;47mÞÛ[40mÛ[47mÛÛ[0;31mÛ[1;30m²[0m[7C[1;41;31m °°°°°°±²[40;30mÞ  [0mÝ
[9C[1;31mß[0;31mß[1;41mþ[0;31mÜÜ    Üþ[37m    [31mÞÛ[1;47mÞ[40mÛ[47mÛÛÛ[0;31mÛ[1;30mÞ[0m[8C[1;41;31m °°°°°±±²[40;30mÞ  [0mÝ
[13C[31mßßßßß[37m[5C[31mÞÛ[1;47mÞ[40mÛÛ[47mÛÛ[41mÝ[0;31mÝ[1;30mÝ[0m[8C[1;41;31m°°°°°±±±²[40;30mÞ  [0mÝ  [31mThis Is xMarvel
[37m    [30mÛ[37m[18C[31mÛ[47mÝ[1;40mÛ[47mÛÛÛÛ[41m [0;31mÝ[1;30mÝ[0m[8C[1;41;31m±°°°±±±±Ý[40;30mÞ  [0mÝ
[6C[30mÛ[37m[15C[31mÞÛ[1;47mÞ[40mÛÛ[47mÛÛÛ[0;31mÛ[1;30mÞ[0m[9C[1;41;31m±°°±±±±±Ý[40;30mÞ  [0mÝ
[15C[31mÜÜÜÜÜÜÜÛÛ[1;47mÞ[40mÛ[47mÛÛ²[41mÝ[0;31mÛ[1;30mÞ[0m[9C[1;41;31m±°±±±±±²Ý[40;30mÞ  [0mÝ
[1m°°°°°°°°[30mÝ [0;31mÜÜ[1;41m°°±±±±°° [0;31mÞ[41m [47mÝ[1;41mÛÛ[47mÛ²²[41mÝ[0;31mÝ[1;30mÝ [37m°°°°°°° [41;31mÞ±±±±±²²Ý[40;30mÞ  [0mÝ[1m°°°°°°°°°°°°°°°°°°°°°°°°°
²²²²²²²² [0;31mÛ[1;41mÜÛÛÛ²²²±° [0;31mÝÛÛ[47mÝ[1;40mÛ[47mÛ²±Þ[0;31mÛÝ[1;30mÝ[0mÞ[1m²²²²²²² [41;31mÞ±±±²²²²Ý[40;30mÞ  [0mÛ[1m²²²²²²²²²²²²²²²²²²²²²²²²²
²²²²²²²[0mÝ[31mÞ[1;41m²ß[0;31mßßß [37mÜÜÜÜÜ [31mÛÛ[1;47mÞ[40mÛ[47m²±°Þ[0;31mÛÝ[1;30mÝ[0mÞ[1m²²²²²²² [41;31mÞ±²²²²²²Ý[40;30mÞ  [0mÛ[1m²²²²²²²²²²²²²²²²²²²²²²²²²
²²²²²²²[0mÝ[31mß[37m ÜÜÛ[1m²²²²²²² [0;31mÛÛ[1;47mÞÛ²° Þ[0;31mÛÝ[1;30mÝ[0mÞ[1m²²²²²²² [41;31mÞ²²²²²²Û[0;41mÝ[1;40;30mÞ  [0mÛ[1m²²²²²²²²²²²²²²²²²²²²²²²²²
²²²²²²²²²²²[0mÛßßßß [31mÜÜÜÜÛÛ[1;47mÞ²±° Þ[0;31mÛÝ[1;30mÝ[0mÞ[1m²²²²²²[47;30mÞ[40m [41;31mÞ²²²²ÛÛ[47mÝ[0;31mÝ[1;30mÝ  [0mÝ[1m²²²²²²²²²²²²²²²²²²²²²²²²²
²²²²²²²²²[0mß [31mÜÜ[1;41m±±±°°  [0;31mÝÛÛ[1;47mÞ±°  Þ[41m [0;31mÝ[1;30mÝ[0mÞ[1m²²²²²²[0mÝ [1;41;31mÞ²²ÛÛÛÛ[47mÝ[0;31mÝ[1;30mÝ  [0mÝ[1m²²²²²²²²²²²²²²²²²²²²²²²²²
²²²²²²²[0mß[31mÜ[1;41mÜÜ²²²±±±°°[0;31mÛÝÛÛ[1;47mÞ±°  Þ[41m [0;31mÝ[1;30mÝ[0mÞ[1m²²²²²²[0mÝ[1;30m [41;31mÞÛÛÛÛÛ[40mÛ[0;41mÝ[1;40;30mÝ   [0mÝ[1m²²²²²²²²²²²²[0mßßßß[1m²²²²²²²²²
°°°°°° [41;31mÞÛÛÛÛÛ²²²±±°[0;31mÛÝÛÛ[1;47mÞ°   Þ[41m [0;31mÝ[1;30mÝ [37m°°°°°° [30mÞ[41;31mÞÛÛÛÛÛ[37mþ[40;30m²    [0mÝ[1m°°°°°°°°°°°° [47mÞ[40mÝ °°°°°°°°°
[0m[6C[1;30mÞ[41;31mÛÛßß[0;31mßßß[37m[7C[31mÞÛ[1;47mÞ°    [41mÝ[0;31mÝ[1;30mÝ[0m[8C[1;41;30mÝ[31mÛÛÛÛ[47mß[41;37mß[40;30m°[0m[5CÝ[13CÞ[1mÛ
[0m[6C[1;30mÞ[41;31mÝ[0;31mß[37m[12C[31mÞÛ[47mÝ[1mÝ  [37m° [41;31mÝ[0;31mÛ[1;30m²[0m[7C[1;41;30mÝ[31mÜÛ[47mß[0;41mß[40;31mßß[37m[7CÝ[13CÞ[1;47m²[0m
[22C[31mÛ[41m [1;47m²  [37m± [31m±[41m [0;31mÝ[1;30m±[0m[5C[1;30mÞ[0;41mþ[47;31mÜ[40mßß[37m[10CÝ[13C[41mÛ[1;47m°[0m
[23C[31mÛÛ[1;47mÜ  [37m² [41;31m²[0;31mÛ [1;30m°    [0;31mß[37m[14CÝ[12C[41mÛÛ[0m
[24C[31mßÛ[1;41mß[47mÜ [37mßÜ[31mß[41mÜ[0;31mÜ[37m[19CÝ[10CÜ[41mÛ[47;31mÜ[0m
[25C[31m ßÛ[1;41mß[47mÜ [37mßþ[31mß[41mÜ[0;31mÜ[37m[17CÝ[7CÜÜ[41mÛ[47;31mÜ[40mß
[37m[28C[31mßß[1;41mßß[47mÜÜÜß[41mÜÜ[0;31mÜÜÜÜ[37m[11CÝ  [1;30mÜ[0mÜÜ[41mÛÛ[47;31mÜ[40mßß
[37m[32C[31mßßßß[1;41mß[0;41mßßß[47;31mÛ[1;41mÜ[0;41mÜ[1;31mÜÜ[0;41mÜÜÜÜÜÜ[47;31mßß[40;37mÝÛÛ[41mÛÛ[40mß[31mß
[37m[40C[31mßßßßßßßßßßßßß[37mÝ[31mß
[37m[53CÝ
[48CÜÜ[1;47mÜÜÜÜ[0;47;30mwa[40;37mÜÜ
[46CÜ[1;47mÜÛÛÛÛÜÜÜ²°[0mÛÛÜ
[45CÞ[1;47m²²²Ûß[0mÛßßÛ[1;47mßÛÝ[0mÛÛÝ
[45CÛ[1;47m²²Û[0mÛß    Û[1;47mÞÛ Ý[0mÛ
[45CÛ[1;47m²²Û [0mÜ    Þ[1;47mÞÝ[0mÛÛÛ
[45CÞ[1;47mÞ²²ÛÜ [0mÜÜ[47m [1mÜß[0mÛ[1;47mÜ[0mÛÝ
[46Cß[1;47mßß²ÛÛßßß Üß[0mÛß
[48CßßÛ[1;47mßßßß[0mÛßß






                                           CODED BY @THE_REAL_MARVEL : TELEGRAM




                                           
                        """)


        logo()

        bl = Fore.BLACK
        wh = Fore.WHITE
        yl = Fore.YELLOW
        red = Fore.RED
        gr = Fore.GREEN
        ble = Fore.BLUE
        res = Style.RESET_ALL
        init(autoreset=True)
        self.mailist = input(f'{gr}  Give Me Your List{wh}/{red}root> {gr}${res} ')
        self.threadscounter = input(f'{gr}  Enter Threads [ 50 Recommended ]{wh}/{red}root> {gr}${res} ')
        self.thread = self.threadscounter
        self.countList = len(list(open(self.mailist)))
        self.clean = 'n'
        if self.clean == 'y':
            self.clean_rezult()
        print('')

    def save_to_file(self, nameFile, x):
        kl = open(nameFile, 'a+')
        kl.write(x)
        kl.close()

    def clean_rezult(self):
        open('live.txt', 'w').close()
        open('die.txt', 'w').close()
        open('unknown.txt', 'w').close()

    def post_email(self, eml):
        try:
            r = requests.get('https://verify.gmass.co/verify?email='+eml+'&key=52d5d6dd-cd2b-4e5a-a76a-1667aea3a6fc',
                              headers={'User-Agent': self.ua}
                              )
            if self.live in r.content:
                return 'live'
            else:
                return 'die'
        except:
            return 'unknown'

    def chk(self):
        while 1:
            global countall2
            global countdd
            global countlive
            global countrec
            eml = self.inputQueue.get()
            rez = self.post_email(eml)

            if rez == 'die':
                countall2 += 1
                countdd += 1
                print(Fore.CYAN + f'[Bounce Checker 3.0]' + Fore.WHITE + ' | ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.RED + f" | {eml} | Die  [ [ {countlive}/{count} ]")       
                ctypes.windll.kernel32.SetConsoleTitleW(f"[Bounce Checker 3.0] [ @xMarvel_OFFiCiAL] {countall2}/{count} | Live : {countlive} Recheck :{countrec} | Die : {countdd}")
                self.save_to_file('die.txt', eml+'\n')
            elif rez == 'live':
                countall2 += 1
                countlive += 1
                print(Fore.CYAN + f'[Bounce Checker 3.0]' + Fore.WHITE + ' | ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.GREEN + f" | {eml} | live  [ [ {countlive}/{count} ]")       
                ctypes.windll.kernel32.SetConsoleTitleW(f"[Bounce Checker 3.0] {countall2}/{count} | Live : {countlive} Recheck :{countrec} | Die : {countdd}")
                self.save_to_file('live.txt', eml+'\n')
            elif rez == 'unknown':
                countall2 += 1
                countdd += 1
                print(Fore.CYAN + '[Bounce Checker 3.0]' + Fore.WHITE + ' | ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.RED + f" | {eml} | die [  {countdd}/{count} ]")
                self.save_to_file('die.txt', eml+'\n')
            else:
                print('contact @xMarval_support')
            self.inputQueue.task_done()

    def run_thread(self):
        for x in range(int(self.thread)):
            t = threading.Thread(target=self.chk)
            t.setDaemon(True)
            t.start()
        for y in open(self.mailist, 'r').readlines():
            self.inputQueue.put(y.strip())
        self.inputQueue.join()

    def finish(self):
        print('')
        print('Checking', self.countList, 'emails has been Checked by xMarvel Checker')
        print('')
        print('Live Emails    : ', len(list(open('live.txt'))), 'emails')
        print('Die  Emails   : ', len(list(open('die.txt'))), 'emails')
        print('')
        input('Enter To Exit --> ')


heh = bounce()
heh.run_thread()
heh.finish()
