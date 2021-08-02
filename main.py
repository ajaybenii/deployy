from io import BytesIO

from PIL import Image,ImageFont,ImageDraw
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse


app = FastAPI()


logo = Image.open("images/logo.jpg")


@app.post("/image_1")
async def For_728_of_60_size(Heading: str, Building_name: str, Launching_time: str, Insert_image: UploadFile=File(...)):
    '''In this function we can upload image and 
    output is google ad image with text 
    '''
    contents = await Insert_image.read()
    image = Image.open(BytesIO(contents))
    
    #____________________Image Resize__________________________
    
    new_img1 = image.resize((182,90))
    width,height = new_img1.size#Size of image
    

    #_____________________Logo Resize__________________________
    

    new_size = logo.resize((60,58))
    w,h = new_size.size
    
    #_____________________WHITE BACKGRAOUND____________________
    
    back_img = Image.new('RGBA', (width+546,height), 'white')
    back_img.paste(new_img1,(100,0, (width+100), (height)))#Here paste the image on white background image 
    back_img.paste(new_size, (650,12, (w+650), (h+12)))#Here paste the logo on white background image at below si

    #________________________TEXT______________________________

    draw = ImageDraw.Draw(back_img)
    
    text= Heading#Heading Text(ADGIOA)
    font = ImageFont.truetype("font_style/Anticva.ttf", 20)
    draw.text((6,24), text, font=font, fill="Brown")#This is the location of text 
    
    caption = Building_name#Building Name 
    font = ImageFont.truetype("font_style/arial-bold.ttf", 13)
    draw.text((295,23), caption, font=font, fill="Black")#This is the location of text

    text= Launching_time#Timing text(Launching soon)
    fonts = ImageFont.truetype("font_style/Serif.ttf", 11)
    draw.text((328,53), text, font=fonts, fill="Black")  

    w_l, h_l = 310, 44 #starting point and end pont
    shape_line = [(430, 44), (w_l, h_l)]#Size and shape of Line
    draw.line(shape_line, fill ="brown", width = 1)
    
    w_r, h_r = 480, 32
    shape_rec = [(630, 57), (w_r, h_r)]#size and Shape of rectangle
    draw.rectangle(shape_rec, fill ="burlywood", width = 2)

    capt_rec = "DOWNLOAD PRICES AND PLANS" #This is for below text 
    font_text = ImageFont.truetype("font_style/arial-bold.ttf", 8)
    draw.text((490,40), capt_rec, font=font_text, fill="white")

    captt = "T&C Apply*"#This is for right bottom text
    fontts = ImageFont.truetype("arial.ttf", 4)
    draw.text((270,565), captt, font=fontts, fill="Black")
    
    #_____________________Image Show__________________________

    buffer = BytesIO()
    rgb_im = back_img.convert('RGB')
    rgb_im.save(buffer, format="jpeg", quality=100)
    buffer.seek(0)
    
    print(rgb_im.size)
    
    return StreamingResponse(buffer, media_type="image/jpeg")

# @app.post("/image_2")
# async def For_970_of_70_size(Insert_image: UploadFile=File(...)):
#     '''In this function we can upload image and add text 
#     '''
#     contents = await Insert_image.read()
#     image = Image.open(BytesIO(contents))
    
#     #____________________Image Resize__________________________
    
#     new_img2 = image.resize((300,90))
#     width,height = new_img2.size#Size of image
    
#     #_____________________Logo Resize__________________________
    
#     new_size = logo.resize((60,58))
#     w,h = new_size.size
#     #_____________________WHITE BACKGRAOUND____________________
    
#     back_img = Image.new('RGBA', (width+670,height), 'white')
#     back_img.paste(new_img2,(200,0, (width+200), (height)))#Here paste the image on white background image 
#     back_img.paste(new_size, (900,12, (w+900), (h+12)))#Here paste the logo on white background image at below side 

#     #________________________TEXT______________________________

#     draw = ImageDraw.Draw(back_img)

#     text= str(db_h[-1])#Heading Text(ADGIOA)
#     font = ImageFont.truetype("font_style/Anticva.ttf", 28)
#     draw.text((40,15), text, font=font, fill="Brown")#This is the location of text 
    
#     caption = str(db_b[-1])#Building Name
#     font = ImageFont.truetype("font_style/arial-bold.ttf", 16)
#     draw.text((515,23), caption, font=font, fill="Black")#This is the location of text 

#     text= str(db_t[-1])#Timing text(Launching soon)
#     fonts = ImageFont.truetype("font_style/Serif.ttf", 14)
#     draw.text((555,55), text, font=fonts, fill="Black")

#     w_l, h_l = 540, 45 #starting point and end pont of line
#     shape_line = [(680, 45), (w_l, h_l)]#Size and shape of Line
#     draw.line(shape_line, fill ="brown", width = 1)
    
#     w_r, h_r = 725, 32
#     shape_rec = [(888, 57), (w_r, h_r)]#size and Shape of rectangle
#     draw.rectangle(shape_rec, fill ="burlywood", width = 2)
    
#     capt_rec = "DOWNLOAD PRICES AND PLANS" #This is for below text 
#     font_text = ImageFont.truetype("font_style/arial-bold.ttf", 9)
#     draw.text((728,40), capt_rec, font=font_text, fill="white")
        
#     captt = "T&C Apply*"#This is for right bottom text
#     fontts = ImageFont.truetype("arial.ttf", 5)
#     draw.text((930,80), captt, font=fontts, fill="Black")
 
#     #_____________________Image Show__________________________

#     buffer = BytesIO()
#     rgb_im = back_img.convert('RGB')
#     rgb_im.save(buffer, format="jpeg", quality=100)
#     buffer.seek(0)
    
#     print(rgb_im.size)
    
#     return StreamingResponse(buffer, media_type="image/jpeg")

# @app.post("/image_3")
# async def For_468_of_60_size(Insert_image: UploadFile=File(...)):
#     '''In this function we can upload image and add text 
#     '''
#     contents = await Insert_image.read()
#     image = Image.open(BytesIO(contents))
#     #____________________Image Resize__________________________
    
#     new_img3 = image.resize((117,60))
#     width,height = new_img3.size#Size of image
#     #_____________________Logo Resize__________________________
    
#     new_size = logo.resize((43,43))
#     w,h = new_size.size
#     #_____________________WHITE BACKGRAOUND____________________
    
#     back_img = Image.new('RGBA', (width+351,height), 'white')

#     back_img.paste(new_img3,(100,0, (width+100), (height)))#Here paste the image on white background image 
#     back_img.paste(new_size, (425,5, (w+425), (h+5)))#Here paste the logo on white background image at below side 
#     #________________________TEXT______________________________

#     draw = ImageDraw.Draw(back_img)

#     text= str(db_h[-1])#Heading Text(ADGIOA)
#     font = ImageFont.truetype("font_style/Anticva.ttf", 14)
#     draw.text((23,20), text, font=font, fill="Brown")#This is the location of text  
    
#     caption = str(db_b[-1])#Building Name
#     font = ImageFont.truetype("font_style/arial-bold.ttf", 8)
#     draw.text((225,20), caption, font=font, fill="Black")#This is the location of text 

#     text= str(db_t[-1])#Timing text(Launching soon)
#     fonts = ImageFont.truetype("font_style/Serif.ttf",7)
#     draw.text((245,33), text, font=fonts, fill="Black")
    
#     w_l, h_l = 235, 30 #starting point and end pont
#     shape_line = [(310, 30), (w_l, h_l)]#Size and shape of Line
#     draw.line(shape_line, fill ="brown", width = 1)

#     w_r, h_r = 330, 20
#     shape_rec = [(420, 35), (w_r, h_r)]#size and Shape of rectangle
#     draw.rectangle(shape_rec, fill ="burlywood", width = 2)

#     capt_rec = "DOWNLOAD PRICES AND PLANS" #This is for below text 
#     font_text = ImageFont.truetype("font_style/arial-bold.ttf", 5)
#     draw.text((333,26), capt_rec, font=font_text, fill="white")
    
#     captt = "T&C Apply*"#This is for right bottom text
#     fontts = ImageFont.truetype("arial.ttf", 4)
#     draw.text((445,50), captt, font=fontts, fill="Black")
#     #_____________________Image Show__________________________

#     buffer = BytesIO()
#     rgb_im = back_img.convert('RGB')
#     rgb_im.save(buffer, format="jpeg", quality=100)
#     buffer.seek(0)
    
#     print(rgb_im.size)
    
#     return StreamingResponse(buffer, media_type="image/jpeg")    

# @app.post("/image_4")
# async def For_480_of_600_size(Insert_image: UploadFile=File(...)):
#     '''In this function we can upload image and add text 
#     '''
#     contents = await Insert_image.read()
#     image = Image.open(BytesIO(contents))
#     #____________________Image Resize__________________________
    
#     new_img4 = image.resize((480,250)) 
#     width,height = new_img4.size#Size of image
#     #_____________________Logo Resize__________________________
    
#     new_size = logo.resize((90,90))
#     w,h = new_size.size
#     #_____________________WHITE BACKGRAOUND____________________
    
#     back_img = Image.new('RGBA', (width,(height+350)), 'white')

#     back_img.paste(new_img4,(0,80, (width), (height+80)))#Here paste the image on white background image 
#     back_img.paste(new_size, (200,505, (w+200), (h+505)))#Here paste the logo on white background image at below side 

#     #________________________TEXT______________________________

#     draw = ImageDraw.Draw(back_img)

#     text= str(db_h[-1])#Heading Text(ADGIOA)
#     font = ImageFont.truetype("font_style/Anticva.ttf", 29)
#     draw.text((190,15), text, font=font, fill="Brown")#This is the location of text 
    
#     caption = str(db_b[-1])#Building Name 
#     font = ImageFont.truetype("font_style/arial-bold.ttf", 28)
#     draw.text((90,360), caption, font=font, fill="Black")#This is the location of tex

#     text= str(db_t[-1])#Timing text(Launching soon)
#     fonts = ImageFont.truetype("font_style/Serif.ttf", 20)
#     draw.text((170,415), text, font=fonts, fill="Black")
    
#     w_l, h_l = 350, 404
#     shape_line = [(140, 404), (w_l, h_l)]#Size and shape of Line
#     draw.line(shape_line, fill ="brown", width = 2)

#     w_r, h_r = 360, 490
#     shape_rec = [(130, 509), (w_r - 10, h_r - 10)]#size and Shape of rectangle
#     draw.rectangle(shape_rec, fill ="burlywood", width = 2)

#     capt_rec = "DOWNLOAD PRICES AND PLANS" #This is for below text 
#     font_text = ImageFont.truetype("font_style/arial-bold.ttf", 12)
#     draw.text((139,490), capt_rec, font=font_text, fill="white")
    
#     captt = "T&C Apply*"#This is for right bottom text
#     fontts = ImageFont.truetype("arial.ttf", 4)
#     draw.text((460,585), captt, font=fontts, fill="Black")
#     #_____________________Image Show__________________________

#     buffer = BytesIO()
#     rgb_im = back_img.convert('RGB')
#     rgb_im.save(buffer, format="jpeg", quality=100)
#     buffer.seek(0)
    
#     print(rgb_im.size)
    
#     return StreamingResponse(buffer, media_type="image/jpeg")    
