from plyer import notification
import requests,time
from bs4 import BeautifulSoup
import tensorflow
def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='C:/Users/lenovo/PycharmProjects/corona/corona.ico',
        timeout=30
    )
def getdata(url):
   r= requests.get(url)
   return r.text
if __name__ == '__main__':
 #while(True):
   # notifyme("gaurav","this is me")
    myhtmlData=getdata('https://www.mohfw.gov.in/')
    #print(myhtmlData)
    soup = BeautifulSoup(myhtmlData,"html.parser")
    myDataStr=""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
      myDataStr+=tr.get_text()
    myDataStr=myDataStr[1:]
    itemlist=myDataStr.split("\n\n")
    states=['Uttarakhand','Uttar Pradesh','Rajasthan','Punjab','Gujarat','Maharashtra']
    for item in itemlist[0:22]:
        datalist=item.split('\n')
        if(datalist[1] in states):
            ntitle="cases of COVID-19"
            ntext=f"State : {datalist[1]}\n Indians : {datalist[2]}\n" \
                  f" Foreign : {datalist[3]}\n Cured : {datalist[4]} Deaths : {datalist[5]}"
            notifyme(ntitle,ntext)
            time.sleep(2)
    #time.sleep(10)

