from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Style
from tkinter import ttk
import random
import threading
from tkinter import messagebox
from tkinter import filedialog
import os
import time
import shutil
from mutagen.mp3 import MP3

#=====================================Back End==========================================
#===============================Window Theme=======================================
def change_mode():
        if switch_2.get() == 1:
          set_appearance_mode("dark")
          s.configure("TScrollbar",background="#2e2e2e",troughcolor="#2e2e2e")
          my_canvas.config(bg="#f0f0f0")
          launch_button.config(bg="#333333",activebackground="#333333")
          copy_button.config(bg="#333333",activebackground="#333333")
          delete_button.config(bg="#333333",activebackground="#333333")
          rename_button.config(bg="#333333",activebackground="#333333")
        else:
          set_appearance_mode("light")
          s.configure("TScrollbar",background="#dedede",troughcolor="#dedede")
          my_canvas.config(bg="#f0f0f0")
          launch_button.config(bg="#dedede",activebackground="#dedede")
          copy_button.config(bg="#dedede",activebackground="#dedede")
          delete_button.config(bg="#dedede",activebackground="#dedede")
          rename_button.config(bg="#dedede",activebackground="#dedede")
#===============================Window Theme=======================================

#===============================Preview panel=====================================

def get_cords(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x   
    y = widget.winfo_y() - widget.startY + event.y   
    widget.place(x=x,y=y)
    win.update()
def clear_frame():
    global slider_Height
    global slider_Width
    global animation
    for i in Display.winfo_children():
            i.destroy()
    Display_menu = CTkFrame(master=Display)
    Display_menu.place(x=10,y=10)
    Title_info = CTkLabel(Display_menu,text="View Scale")
    Title_info.place(x=40,y=2)
    button_clear = CTkButton(master=Display,text="Clear Frame",
              fg_color=("gray75", "gray30"),command=clear_frame)
    button_clear.place(x=50,y=215)
    slider_Height = CTkSlider(master=Display_menu,height=175,
                              from_=5,to=1000,orient=VERTICAL)
    slider_Height.place(x=10,y=2)
    slider_Width = CTkSlider(master=Display_menu,width=180,from_=5,to=1000,)
    slider_Width.place(x=10,y=180)
    animation = CTkLabel(master=Display_menu,image=emo1)
    animation.place(x=30,y=10)
    anim2 = threading.Thread(target=emo_switch,daemon=True)
    anim2.start()
def create_Text(link):
    print(link)
    text_val = open(link,"r")
    text_value = text_val.read()
    text_val.close() 
    label2 = Label(Display,text=text_value,justify=LEFT)
    label2.place(x=30,y=30)
    label2.bind("<Button-1>",get_cords)
    label2.bind("<B1-Motion>",drag)
    mainloop()
def create_audio(link):
    file_info =MP3(link)
    file_info = file_info.info.length
    file_info = round(file_info)
    print(file_info)
    label2 = CTkLabel(Display,
    text="Unfortunatly this file can't be displayed"+'\n'+"File Type: Audio"+'\n'+"Track Lenght: "+str(file_info)+"seconds",
                                                                                                               justify=LEFT)
    label2.place(x=10,y=250)
def create_video():
    label2 = CTkLabel(Display,
    text="Unfortunatly this file can't be displayed"+'\n'+"File Type: Video"+'\n'+"Video Lenght:  ?",
                                                                                        justify=LEFT)
    label2.place(x=10,y=250)
def create_zip():
    label2 = CTkLabel(Display,
    text="Unfortunatly this file can't be displayed"+'\n'+"File Type: Rar/Zip"+'\n',justify=LEFT)
    label2.place(x=10,y=250)
def create_exe():
    label2 = CTkLabel(Display,
    text="Unfortunatly this file can't be displayed"+'\n'+"File Type: Exe"+'\n',
                                                                    justify=LEFT)
    label2.place(x=10,y=250)
def create_other():
    label2 = CTkLabel(Display,
    text="Unfortunatly this file can't be displayed"+'\n'+"File Type: Unknown"+'\n',
                                                                       justify=LEFT)
    label2.place(x=10,y=250)
def create_image(link):
    global slider_Height
    global slider_Width
    print(link)
    image_h = slider_Height.get()
    image_w = slider_Width.get()
    image = Image.open(link)
    new_image = image.resize((int(image_w),int(image_h)))
    out_image = ImageTk.PhotoImage(new_image)
    label = Label(Display,image=out_image)
    label.place(x=30,y=30)
    label.bind("<Button-1>",get_cords)
    label.bind("<B1-Motion>",drag)
    mainloop()
#===============================Preview panel=====================================

#================================animations=======================================
def emo_switch():
    global animation
    objects = [emo1,emo2,emo3,emo4,emo5]
    new_emo = random.choice(objects)
    animation.configure(image=new_emo)
    animation.after(1000,emo_switch)
#================================animations======================================

#================================launch file=====================================
def launch_file():
         link_file = open(PATH+"\\path.dat","r")
         link_info = link_file.read()
         try:
          os.startfile(link_info)
         except:
             pass
         link_file.close()
#================================launch file=====================================

#================================rename file=====================================
def rename_file():
   def new_name():  
    global ent
    if messagebox.askyesno(title="Prompt" ,
    message="Do You Want To Rename This File"):
      path_link = ent.get()   
      link_file = open(PATH+"\\path.dat","r")
      link = link_file.read()
      link_file.close()
      info = ent2.get()
      file_ex = link.split(".")
      exten = (repr(file_ex[-1]))
      exten = exten.replace("'","")
      file_ex = link.split("\\")
      file_name = (repr(file_ex[-1]))
      exten = exten.replace("'","")
      full_info = path_link+"\\"+info+"."+exten
      os.rename(link, full_info)
      Entery_path_assign(E)
      messagebox.showinfo(title='Prompt',
      message='The File Has Been Renamed Sucessfully!') 
    else:
      messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 
    top.destroy()
   top = CTkToplevel()
   top.title("Rename File")
   ent2 = CTkEntry(top,width=300,placeholder_text="New File Name")
   ent2.pack(padx=10,pady=20)
   submit = CTkButton(top,text="Rename",command=new_name)
   submit.pack(padx=10,pady=20)
   mainloop() 
#================================rename file=====================================

#==================================copy file=====================================
def copy():
        link_file = open(PATH+"\\path.dat","r")
        link = link_file.read()
        link_file.close()
        file_path = filedialog.askdirectory()
        if messagebox.askyesno(title="Prompt" ,
        message="Do You Want To Copy To This Location"):
          shutil.copy(link, file_path)
          messagebox.showinfo(title='Prompt',
          message='The File Has Been Copied Sucessfully!')  
        else:
          messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!') 
def copy_file():
        x = threading.Thread(target=copy,daemon=True)  
        x.start()   
#==================================copy file=====================================

#================================delete file=====================================         
def delete_file():
  if messagebox.askyesno(title="Prompt" , message="Do You Want To Delete This File"):
     link_file = open(PATH+"\\path.dat","r")
     link = link_file.read()
     link_file.close()
     os.remove(link)
     Entery_path_assign(E)
     messagebox.showinfo(title='Prompt',message='The File Has Been Deleted Sucessfully!')
  else:
     messagebox.showinfo(title='Prompt',message='The Operation Was Canciled!')    
#================================delete file=====================================

class Make:
    def __init__(self):
        print("active")
#==================chirld file preview assigner and generator====================
    def send(link):
        link_file = open(PATH+"\\path.dat","w")
        link_file.write(link)
        link_file.close()
        print(link)
        file_name = link.split("\\")
        file_name = (repr(file_name[-1]))
        file_name = file_name.replace("'", "")
        print(file_name)
        file_size = os.path.getsize(link)
        file_info.config(text="File Name :    "+file_name+'\n'+"File Path :       "+link+'\n'+"File Size :        "+str(file_size)+" Bytes",justify=LEFT)
        file_ex = file_name.split(".")
        exten = (repr(file_ex[-1])).lower()
         #==========================================
        if exten == "'mp3'" :
            create_audio(link)
        elif exten == "'wav'":
            create_audio(link)
        elif exten == "'wma'":
           create_audio(link)
        elif exten == "'act'":
           create_audio(link)
        #==========================================
        elif exten == "'docx'":
             create_Text(link)   
        elif exten == "'bat'":
             create_Text(link)  
        elif exten == "'py'":
             create_Text(link)  
        elif exten == "'txt'" :
             create_Text(link) 
        elif exten =="'php'":
             create_Text(link)  
        elif exten == "'vbs'":
             create_Text(link)         
        elif exten == "'html'" :
             create_Text(link)
        #==========================================
        elif exten == "'gif'":
           create_image(link)
        elif exten == "'png'":
            create_image(link)
        elif exten == "'bmp'":
            create_image(link)        
        elif exten == "'jepg'":
            create_image(link)
        elif exten == "'jpg'":
            create_image(link)
        #==========================================
        elif exten == "'avi'":
           create_video()
        elif exten == "'3gp'":
           create_video()
        elif exten == "'svi'":
           create_video()
        elif exten == "'mpeg'":
           create_video()
        elif exten == "'wmv'":
           create_video()         
        elif exten == "'mov'":
           create_video()
        elif exten == "'flv'":
           create_video()
        elif exten == "'mkv'":
           create_video()  
        elif exten == "'webm'":
           create_video()             
        elif exten == "'mp4'":
           create_video()
        #==========================================
        elif exten == "'rar'":
           create_zip()
        elif exten == "'zip'": 
           create_zip()
        #==========================================
        elif exten == "'exe'":
            create_exe()
        #==========================================
        else:
            create_other()
#==================chirld file preview assigner and generator====================

#====================chirld file assigner and generator==========================
    def Child_files(name,link,color,frame):
        file_ex = name.split(".")
        exten = (repr(file_ex[-1])).lower()
        if len(name) >=25:
          name = name[0:21]     
        else:
            pass
        name = Button(frame,text=name,compound=TOP,fg=color,font=("arial",10,"bold"),
                                                                             border=0)
        name.pack(pady=5,padx=90)
        name.config(command= lambda : Make.send(link))
        name.config(image=base1)
        range_list = random.randint(1, 100)
        my_canvas.config(width=range_list)
        list1 = [400,396,397,403,401,399,402]
        from_list1 = random.choice(list1)
        my_canvas.config(width=from_list1)
        #==========================================
        if exten == "'mp3'" :
            name.config(image=base7)
        elif exten == "'wav'":
            name.config(image=base7)
        elif exten == "'wma'":
            name.config(image=base7)
        elif exten == "'act'":
            name.config(image=base7)   
        #==========================================
        elif exten == "'docx'":
            name.config(image=base5)   
        elif exten == "'pdf'":
            name.config(image=base5)  
        elif exten == "'xlsx'":
            name.config(image=base3)  
        elif exten == "'txt'" :
            name.config(image=base5) 
        elif exten =="'xls'":
            name.config(image=base3)  
        elif exten == "'ppt'":
            name.config(image=base3)  
        elif exten == "'pptx'" :
            name.config(image=base3)         
        elif exten == "'html'" :
            name.config(image=base1)
        #==========================================
        elif exten == "'gif'":
            name.config(image=base2)
        elif exten == "'png'":
            name.config(image=base2)
        elif exten == "'bmp'":
            name.config(image=base2)        
        elif exten == "'jepg'":
            name.config(image=base2)
        elif exten == "'jpg'":
            name.config(image=base2)
        #==========================================
        elif exten == "'avi'":
            name.config(image=base8)
        elif exten == "'3gp'":
            name.config(image=base8)
        elif exten == "'svi'":
            name.config(image=base8)
        elif exten == "'mpeg'":
            name.config(image=base8)
        elif exten == "'wmv'":
            name.config(image=base8)            
        elif exten == "'mov'":
            name.config(image=base8)
        elif exten == "'flv'":
            name.config(image=base8)
        elif exten == "'mkv'":
            name.config(image=base8)   
        elif exten == "'webm'":
            name.config(image=base8)              
        elif exten == "'mp4'":
            name.config(image=base8)
        #==========================================
        elif exten == "'rar'":
            name.config(image=base6)
        elif exten == "'zip'": 
            name.config(image=base6)
        #==========================================
        elif exten == "'exe'":
            name.config(image=base10)
        #==========================================
        else:
            name.config(image=base9)
        #==========================================    
#====================chirld file assigner and generator==========================

#============================chirld folder assigner==============================            
def create_folder_link(link):
    dirinfo = os.listdir(link)
    frame = second_frame
    ent.delete(0,"end")
    ent.insert(0, link)
    for i in second_frame.winfo_children():
            i.destroy()
    Object_assign(link,"#51932a",frame)
#============================chirld folder assigner==============================  
    
#===========================chirld folder generator==============================     
def Child_folders(link,name,color,frame):
        if len(name) >=25:
          name = name[0:21]     
        else:
            pass
        name = Button(frame,text=name,compound=TOP,image=base4,fg=color,
                                       font=("arial",10,"bold"),border=0)
        name.pack(pady=5,padx=90)
        name.config(command= lambda : create_folder_link(link))         
        range_list = random.randint(1, 100)
        my_canvas.config(width=range_list)
        list1 = [400,396,397,403,401,399,402]
        from_list1 = random.choice(list1)
        my_canvas.config(width=from_list1)
#===========================chirld folder generator==============================              

#==========================back adresses generator================================     
def back():
    entry_info = ent.get()
    file_ex = entry_info.split("\\")
    exten = (repr(file_ex[-1])) 
    name_lent = len(exten)
    name_lent = int(name_lent) - 1
    frame = second_frame
    print(exten)
    back_address = entry_info[0:-int(name_lent)] 
    print(back_address)
    ent.delete(0,"end")
    ent.insert(0, back_address)  
    for i in second_frame.winfo_children():
            i.destroy()
    Object_assign(back_address,"#b23232",frame)
#==========================back adresses generator================================  
        
#==============================manually assigned adresses=========================            
def Entery_path_assign(e):
    in_ent = ent.get()
    addtext1 = in_ent.split("\\")
    addtext = (repr(addtext1[-1]))
    frame = second_frame
    for i in second_frame.winfo_children():
            i.destroy()
    Object_assign(in_ent,"#1774a5",frame)
#==============================manually assigned adresses=========================   
             
#=============================file and dir diffrentiator==========================
def Object_assign(new_info,color,frame):
    dirinfo = os.listdir(new_info)
    for x in dirinfo:
        if os.path.isfile(new_info+"\\"+x):
            Make.Child_files(x,new_info+"\\"+x,color,frame)
        else:
            Child_folders(new_info+"\\"+x, x,color,frame)
#=============================file and dir diffrentiator==========================
#=====================================Back End==========================================

#======================================Front End========================================
win = CTk()
win.geometry("420x700")
PATH = os.path.dirname(os.path.realpath(__file__))
link_file = open(PATH+"\\path.dat","w")
link_file.write("NONE")
link_file.close()
#======================================image imports==============================
image = Image.open(PATH+'\\images\\buttons\\1.png')
new_image1 = image.resize((200,200))
base1 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\2.png')
new_image1 = image.resize((200,200))
base2 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\3.png')
new_image1 = image.resize((200,200))
base3 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\4.png')
new_image1 = image.resize((200,200))
base4 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\5.png')
new_image1 = image.resize((200,200))
base5 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\6.png')
new_image1 = image.resize((200,200))
base6 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\7.png')
new_image1 = image.resize((200,200))
base7 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\8.png')
new_image1 = image.resize((200,200))
base8 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\9.png')
new_image1 = image.resize((200,200))
base9 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\10.png')
new_image1 = image.resize((200,200))
base10 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\11.png')
new_image1 = image.resize((90,90))
base11 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\12.png')
new_image1 = image.resize((90,90))
base12 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\13.png')
new_image1 = image.resize((90,90))
base13 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\buttons\\14.png')
new_image1 = image.resize((90,90))
base14 = ImageTk.PhotoImage(new_image1)
#=====================================================
image = Image.open(PATH+'\\images\\emojis\\1.png')
new_image1 = image.resize((150,150))
emo1 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\emojis\\2.png')
new_image1 = image.resize((150,150))
emo2 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\emojis\\3.png')
new_image1 = image.resize((150,150))
emo3 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\emojis\\4.png')
new_image1 = image.resize((150,150))
emo4 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\emojis\\5.png')
new_image1 = image.resize((150,150))
emo5 = ImageTk.PhotoImage(new_image1)
image = Image.open(PATH+'\\images\\emojis\\5.png')
new_image1 = image.resize((60,60))
emo6 = ImageTk.PhotoImage(new_image1)
#======================================image imports=============================


 


set_appearance_mode("Light") 
set_default_color_theme("dark-blue") 
win.grid_columnconfigure(1, weight=1)
win.grid_rowconfigure(0, weight=1)
frame_left = CTkFrame(master=win,width=310,corner_radius=0)
frame_left.grid(row=0, column=0, sticky="nswe")
cover = CTkFrame(master=frame_left,)
cover.pack()
ent = CTkEntry(master=cover,width=260,placeholder_text=">Path Address//")
ent.grid(row=0,column=0,pady=20,padx=5)
button_2 = CTkButton(master=cover,text="Back",fg_color=("gray75", "gray30"),command=back)
button_2.grid(row=0,column=1,pady=20,padx=5)
s = Style()
s.theme_use('alt')
s.configure("TScrollbar",troughcolor="#dedede")
main_frame = CTkFrame(master=frame_left,width=80,corner_radius=30)
main_frame.pack(padx=5,side=LEFT,fill=Y)
my_canvas = Canvas(main_frame,borderwidth=0,bg="#f0f0f0")
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame,command=my_canvas.yview,style="TScrollbar")
my_scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure
                   (scrollregion = my_canvas.bbox("all")))
second_frame = Frame(my_canvas,bg="#f0f0f0")
my_canvas.create_window((0,0), window=second_frame, anchor="nw")
frame_right = CTkFrame(master=win)
frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
Display = CTkFrame(master=frame_right,height=600)
Display.grid(row=1, column=0,sticky="wesn", padx=20, pady=20)
Display_menu = CTkFrame(master=Display)
Display_menu.place(x=10,y=10)
Title_info = CTkLabel(Display_menu,text="View Scale")
Title_info.place(x=40,y=2)
button_clear = CTkButton(master=Display,text="Clear Frame",
          fg_color=("gray75", "gray30"),command=clear_frame)
button_clear.place(x=50,y=215)
slider_Height = CTkSlider(master=Display_menu,height=175,from_=5,to=1000,orient=VERTICAL)
slider_Height.place(x=10,y=2)
slider_Width = CTkSlider(master=Display_menu,width=180,from_=5,to=1000,)
slider_Width.place(x=10,y=180)
animation = CTkLabel(master=Display_menu,image=emo1)
animation.place(x=30,y=10)
anim = threading.Thread(target=emo_switch,daemon=True)
anim.start()
controll = CTkFrame(master=frame_right)
controll.grid(row=2, column=0,sticky="wesn", padx=20, pady=20)
launch_button = Button(master=controll,border=0,bg="#dedede",activebackground="#dedede",
                                                       image=base14,command=launch_file)
launch_button.grid(row=1,column=0,padx=20,pady=5,sticky="nsew")
copy_button = Button(master=controll,border=0,bg="#dedede",activebackground="#dedede",
                                                         image=base12,command=copy_file)
copy_button.grid(row=1,column=1,padx=20,pady=5,sticky="nsew")
delete_button = Button(master=controll,border=0,bg="#dedede",activebackground="#dedede",
                                                       image=base13,command=delete_file)
delete_button.grid(row=1,column=2,padx=20,pady=5,sticky="nsew")

rename_button = Button(master=controll,border=0,bg="#dedede",activebackground="#dedede",
                                                       image=base11,command=rename_file)
rename_button.grid(row=1,column=3,padx=20,pady=5,sticky="nsew")
frame_right.grid_columnconfigure(0, weight=1)
frame_right.grid_rowconfigure(2, weight=1)
switch_2 = CTkSwitch(master=frame_right,text="Dark Mode",command=change_mode)
switch_2.grid(row=0, column=0, pady=10, padx=20, sticky="sw")
info_frame = CTkFrame(master=controll)
info_frame.grid(row=0, column=0,columnspan=4,sticky="wesn", padx=20, pady=10)
controll.grid_columnconfigure(0, weight=1)
controll.grid_rowconfigure(2, weight=1)
file_info = CTkLabel(master=info_frame,
text="File Name  : ?"+'\n'+"File Path     : ?"+'\n'+"File Size      : ?",justify=LEFT)
file_info.pack(pady=10)
ent.bind("<Return>",Entery_path_assign)
#======================================Front End========================================

win.mainloop()
