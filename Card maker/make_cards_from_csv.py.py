from Tkinter import *
import  ImageDraw,ImageFont
from PIL import Image
import csv

fontPath="times.ttf"
csv_path='New Dominion Kingdom Set.csv'
the_font =  ImageFont.truetype ( fontPath, 32 )
small_font =ImageFont.truetype(fontPath,20)
card_width=475
card_height=card_width*1.543
num_per_sheet=9
max_sheets=42


class card:
    x=0
    y=0
    width=0
    cost=0
    name=""
    def __init__(self,name,cost,x=0,y=0,width=0):
        self.name=name
        self.x=x
        self.y=y
        self.width=width
        self.cost=cost
        self.ratio=1.543
        self.y2=y+width*self.ratio
        self.center=(self.x*2+self.width)/2

def draw_line(canvas,pil_draw,x1,y1,x2,y2):
    canvas.create_line([x1,y1,x2,y2])
    pil_draw.line([x1,y1,x2,y2],(0,0,0))

def draw_rect(canvas,pil_draw,x1,y1,x2,y2):
    canvas.create_rectangle(x1,y1,x2,y2)
    pil_draw.rectangle([x1,y1,x2,y2],outline=(0,0,0))

def c_dim(pil_draw,x,y,font,text):
    width=pil_draw.textsize(text,font=font)[0]
    new_x=x+(width/2)
    return (new_x,y)

def draw_text(canvas,pil_draw,x,y,text,font=the_font):
    canvas.create_text(x,y,text=text,anchor=NW,font=("Times","28"))
##    right_pos=c_dim(pil_draw,x,y,the_font,text)
    pil_draw.text((x,y),text,fill=(0,0,0),font=font)
    
def draw_card_frame(canvas,pil_draw,card):
    x=card.x
    y=card.y
    width=card.width
    center=((x+x+width)/2)-(6*len(card.name)/2)
    y2=card.y2
    x2=x+width
    middle=(x+x2)/2
    
    draw_rect(canvas,pil_draw,x,y,x+width,y2)
    draw_text(canvas,pil_draw,center,y+10,card.name)
    draw_text(canvas,pil_draw,x+10,y2-40,str(card.cost))

def formatt(string_in):
    str_list=string_in.split()
    buf=""
    buf_size=30
##    print str_list
    for el in str_list:
        buf_size=buf_size-len(list(el))
        if buf_size<0:
            buf=buf+"~"+el+" "
            buf_size=30
        else:
            buf+=el+" "
    return buf
        

def split_tilde(string_in):
    return string_in.split("~")

def draw_text_lines(canvas,pil_draw,center,middle,lines):
    i=0
    for line in lines:
        draw_text(canvas,pil_draw,center,middle+i,line,small_font)
        i+=30
        
def make_plus(effect):
    return effect.replace("?","+")

def draw_action_card(canvas,pil_draw,card,effects):
    draw_card_frame(canvas,pil_draw,card)
    middle=(card.y+card.y2)/2
##    center=((card.x*2+card.width)/2)-(6*len(card.name)/2)
    center=((card.x*2+card.width)/2)-(190)
##    draw_text(canvas,pil_draw,center,middle,formatt(effects))
    draw_text_lines(canvas,pil_draw,center,middle+50,split_tilde(formatt(effects)))



def row_to_action(canvas,pil_draw,row,x,y):
    c=card(row[0],row[3],x,y,card_width)
    buf=""
    if (not row[4]==""):
        buf+=row[4]+"~~"
    if (not row[5]==""):
        buf+=row[5]+"~~"
    if (not row[6]==""):
        buf+=row[6]
    draw_action_card(canvas,pil_draw,c,make_plus(buf))
    draw_text(canvas,pil_draw,c.center-40,c.y2-40,row[1]+"   "+row[2])

width = 2100
height = 1600
center = height//2
white = (255, 255, 255)
green = (0,128,0)

#28 characters

root = Tk()

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
images=[]
draws=[]
for i in range(max_sheets):
    images.append(Image.new("RGB",(width,height),white))
    draws.append(ImageDraw.Draw(images[i]))


csvfile=open(csv_path,'rb')
reader=csv.reader(csvfile, delimiter=',')
num_card=0
sheet_card=1
num_draw=0
i=1
j=0

for row in reader:
    for k in range(10):
        if row[0]=='':
            break
        if (num_card>=10):
            if (sheet_card%num_per_sheet==0):
                num_draw+=1
                sheet_card=1
                i=1
                j=0
            row_to_action(cv,draws[num_draw],row,(card_width+10)*(i-1)+10,(card_height*j+10)+j*10)

            if (not i%4==0):
                i+=1
            else:
                j+=1
                i=1
            sheet_card+=1 
        num_card+=1
    
        
    

##print formatt("This is a very long string. I wonder what will happen?")

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
filename = "Output/cardSheet"
for i in range(max_sheets):
    images[i].save(filename+str(i)+".png")

##root.mainloop()
