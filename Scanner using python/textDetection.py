import cv2
import pytesseract
import qrcode
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('plate.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
str=pytesseract.image_to_string(img)
strset=str.splitlines()
strjson='{"FirstName":"John", "SecondName":"Doe", "BookingDate":"03-05-2021", "BookingTime":"14.30", "LicenseNumber":"PB 15 K 2806"};'
strjson=strjson.strip(';')
strjson=strjson.strip('{')
strjson=strjson.strip('}')
strjson_temp=strjson.split(',')
str_add=''
str_no=''
l=0
for s in strjson_temp:
    json_temp=s.split(':')
    l+=1
    if(l==len(strjson_temp)):
        str_add+=json_temp[1].strip('"')
        str_no=json_temp[1].strip('"')
    else:
        str_add+=json_temp[1].strip('"')+"_"

count=0
for x in strset:
    if(len(x)>0):
        count+=1
        if(x==str_no):
            print("Yes")
            code=qrcode.make(str_add)
            code.save(f"QRCode{count}.jpg")
hImg,wImg,_=img.shape
boxes=pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b=b.split(' ')
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
    cv2.putText(img,b[0],(x,hImg-y+30),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

cv2.imshow('Result',img)
cv2.waitKey(0)
