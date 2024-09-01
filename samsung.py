# -*- coding: utf-8 -*-
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import os
import datetime
import time
import re
import smtplib
import random

def requests_retry_session(
    retries=50,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

httpheaders = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}

while True:

    mainurlphone = 'https://fota-cloud-dn.ospserver.net/firmware/BGL/SM-G985F/version.xml'
    #mainurlwatch = 'https://fota-cloud-dn.ospserver.net/firmware/XAR/SM-R830/version.xml'
    mainurlwatch2 = 'https://fota-cloud-dn.ospserver.net/firmware/BGL/SM-R875F/version.xml'
    mainurlbuds = 'https://wsu-dms.samsungdm.com/common/support/firmware/downloadUrlList.do?prd_mdl_name=SM-R175FOTA&loc=global'    
    
    server = smtplib.SMTP('IP', PORT)
    server.login("USERNAME", "PASSWORD")
    #Galaxy S20+
    mainurlphone = requests_retry_session().get(mainurlphone, headers=httpheaders)
    samsungphonesoup = BeautifulSoup(mainurlphone.text.encode('utf-8'), 'html.parser')
    #print (samsungphonesoup)

    headers = ("Message-ID: <"+str(random.randint(1000000000000000000000000000,9999999999999999999999999999))+"@mailer.DOMAIN.COM>\nFrom: name1 <user1@domain1.com>\nTo: name2 <user2@domain2.com>\nSubject: Samsung Upgrade Available\nMIME-Version: 1.0\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: 8bit\n")

    for version_element_phone in samsungphonesoup.find_all('latest'):
        print('Raw: '+str(version_element_phone))
        version_element_phone = (version_element_phone).text
        print('Prettified: '+str(version_element_phone))
        f = open( 'PATHTOTEMPTXTFILE/latestphone.txt', 'r' )
        if (not (version_element_phone in f.read())):
            msg = ('\n\n<!DOCTYPE html><head><meta charset="UTF-8"></head><body><p style="margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:&quot;Calibri&quot;,sans-serif;">New upgrade for Samsung Galaxy S20+: '+version_element_phone.encode('utf-8')+'\n<br>Please check your phone.\n<br></p>'+'</body></html>\n\n')
            server.sendmail("MAILFROMADDRESS", "MAILTOADDRESS", headers+msg)
            f.close()
            f = open('PATHTOTEMPTXTFILE/latestphone.txt', 'w')
            print ('Saved in the temp file: '+str(version_element_phone))
            f.seek(0,2)
            f.write(version_element_phone.encode('utf-8'))
            f.close()
        else: print('No new version was detected for the phone. Nothing written in the temp file.\n')
        f.close()

    '''
    #Galaxy Watch Active 2
    mainurlwatch = requests_retry_session().get(mainurlwatch)
    samsungwatchsoup = BeautifulSoup(mainurlwatch.text.encode('utf-8'), 'html.parser')
    #print samsungwatchsoup
    for version_element_watch in samsungwatchsoup.find_all('latest'):
        print('Raw: '+str(version_element_watch))
        version_element_watch = (version_element_watch).text
        print('Prettified: '+str(version_element_watch))
        f = open( 'PATHTOTEMPTXTFILE/latestwatch.txt', 'r' )
        if (not (version_element_watch in f.read())):
            msg = ('\n\n<!DOCTYPE html><head><meta charset="UTF-8"></head><body><p style="margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:&quot;Calibri&quot;,sans-serif;">New upgrade for Samsung Galaxy Watch Active 2: '+version_element_watch.encode('utf-8')+'\n<br>Please check Galaxy Wearable on your phone.\n<br></p>'+'</body></html>\n\n')
            server.sendmail("MAILFROMADDRESS", "MAILTOADDRESS", headers+msg)
            f.close()
            f = open('PATHTOTEMPTXTFILE/latestwatch.txt', 'w')
            print ('Saved in the temp file: '+str(version_element_watch))
            f.seek(0,2)
            f.write(version_element_watch.encode('utf-8'))
            f.close()
        else: print('No new version was detected for the watch. Nothing written in the temp file.\n')
        f.close()
    '''

    #Galaxy Watch 4
    mainurlwatch2 = requests_retry_session().get(mainurlwatch2, headers=httpheaders)
    samsungwatchsoup2 = BeautifulSoup(mainurlwatch2.text.encode('utf-8'), 'html.parser')
    #print samsungwatchsoup2
    for version_element_watch2 in samsungwatchsoup2.find_all('latest'):
        print('Raw: '+str(version_element_watch2))
        version_element_watch2 = (version_element_watch2).text
        print('Prettified: '+str(version_element_watch2))
        f = open( 'PATHTOTEMPTXTFILE/latestwatch2.txt', 'r' )
        if (not (version_element_watch2 in f.read())):
            msg = ('\n\n<!DOCTYPE html><head><meta charset="UTF-8"></head><body><p style="margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:&quot;Calibri&quot;,sans-serif;">New upgrade for Samsung Galaxy Watch 4: '+version_element_watch2.encode('utf-8')+'\n<br>Please check Galaxy Wearable on your phone.\n<br></p>'+'</body></html>\n\n')
            server.sendmail("MAILFROMADDRESS", "MAILTOADDRESS", headers+msg)
            f.close()
            f = open('PATHTOTEMPTXTFILE/latestwatch2.txt', 'w')
            print ('Saved in the temp file: '+str(version_element_watch2))
            f.seek(0,2)
            f.write(version_element_watch2.encode('utf-8'))
            f.close()
        else: print('No new version was detected for the watch. Nothing written in the temp file.\n')
        f.close()


    #Buds Plus
    mainurlbuds = requests_retry_session().get(mainurlbuds)
    samsungbudssoup = BeautifulSoup(mainurlbuds.text.encode('utf-8'), 'html.parser')
    #print samsungbudssoup
    for version_element_buds in samsungbudssoup.find_all('fwversion'):
        print('Raw: '+str(version_element_buds))
        version_element_buds = (version_element_buds).text
        print('Prettified: '+str(version_element_buds))
        f = open( 'PATHTOTEMPTXTFILE/latestbuds.txt', 'r' )
        if (not (version_element_buds in f.read())):
            msg = ('\n\n<!DOCTYPE html><head><meta charset="UTF-8"></head><body><p style="margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:&quot;Calibri&quot;,sans-serif;">New upgrade for Samsung Buds Plus: '+version_element_buds.encode('utf-8')+'\n<br>Please check Galaxy Wearable on your phone.\n<br></p>'+'</body></html>\n\n')
            server.sendmail("MAILFROMADDRESS", "MAILTOADDRESS", headers+msg)
            f.close()
            f = open('PATHTOTEMPTXTFILE/latestbuds.txt', 'w')
            print ('Saved in the temp file: '+str(version_element_buds)+'\n')
            f.seek(0,2)
            f.write(version_element_buds.encode('utf-8'))
            f.close()
        else: print('No new version was detected for the buds. Nothing written in the temp file.\n')
        f.close()


    server.quit
    print('Cycle done! '+str(datetime.datetime.now())[0:-7]+'\n\n\n')
    for i in range(3600):
        time.sleep(1)
