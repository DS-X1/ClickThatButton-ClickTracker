from requests_html import HTMLSession
import time


while True:
 
#Start the Session, these three lines basically scour the site to get number of clicks
  session = HTMLSession()
  response = session.get('https://www.clickthatbutton.com/')
  clicks = response.html.find('#clicks-total-number', first=True)


#The response is a string, so I  convert it to a number here 
  true_click = int(clicks.text)
  original = true_click
  time.sleep(10)

#Get number of clicks again so we can get latest amount
  session = HTMLSession()
  response = session.get('https://www.clickthatbutton.com/')
  clicks = response.html.find('#clicks-total-number', first=True)

#We sutract the old number number of clicks and new to get how many appeared in past 10 seconds
  true_click = int(clicks.text)
  new = true_click
  answer = new - original
  print(answer, " new clicks in the past 10 seconds.")
  continue