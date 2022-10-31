import string
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new
import smtplib
sender='nu_vreau_spam@coneasorin.ro'
subject='Pretul a scazut la:'
to_addr_list = ['adriancostica06@yahoo.com']
cc_addr_list = ['']
def sendemail(sender,message, subject,to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'
        header  = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
 
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,"stiinte216_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        print("Error: unable to send email")
        return False
 
#sendemail(sender, "Pretul a scazut la: ", subject, to_addr_list, cc_addr_list)
 
def data_scraping ():
    req=requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-128gb-5g-deep-purple-mq9t3rx-a/pd/DXDY4LMBM/?X-Search-Id=8078e075de34c00fc8f2&X-Product-Id=101075766&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view")
    soup=BeautifulSoup(req.text,"html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    pret_referinta = 7969
    if ( new_price<pret_referinta ):
        sendemail(sender,"Pretul a scazut la: "+str(new_price),subject,to_addr_list, cc_addr_list=[])
        print ("Pretul a scazut ")
    else:
       print ("Pretul nu a scazut")
#sendemail(sender, "Pretul a scazut la: ", subject, to_addr_list, cc_addr_list)
# # scheduler = BlockingScheduler()
# # scheduler.add_job(data_scraping, 'interval', seconds=10)
# # scheduler.start()
data_scraping()