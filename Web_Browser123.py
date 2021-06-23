#### ""mini project"" ######
#### internet browser #####


from tkinter import *
import webbrowser as wb

root = Tk()
root.geometry("1290x1080")
root.title("web Browser")
root.config(bg = "white")
root.iconbitmap('internet_icon1.ico')

## functionality

def search():
    data = str (e1.get())
    wb.open ("https://www.google.com/search?q="+data)
    
def youtube():
    wb.open("https://www.youtube.com/")
def amazon():
    wb.open("https://www.amazon.com/")
def Facebook():
    wb.open("https://www.facebook.com/")
def instagram():
    wb.open("https://www.instagram.com/")
    
    


##label
'''
tag1 = Label (root,text = "Google",font = ("arial 50"))
tag1.place(x=570 ,y = 100)
'''

g_pic = PhotoImage(file = "google1.png")
tag2 = Label(root,image = g_pic)
tag2.place(x = 570 , y = 80)
'''
amazon_pic = PhotoImage(file = "amazon1.png")
tag3 = Label(root,image = amazon_pic)
tag3.place(x = 250 , y = 450)
'''
fb_pic = PhotoImage(file = "facebook1.png")
tag4 = Label(root,image = fb_pic)
tag4.place(x = 730 , y = 350)

yt_pic = PhotoImage(file = "yt.png")
tag5 = Label(root,image = yt_pic)
tag5.place(x = 470 , y = 350)

ig_pic = PhotoImage(file = "insta.png")
tag6 = Label(root,image = ig_pic)
tag6.place(x = 980 , y = 350)


##entry

e1 = Entry(root,font = ("arial 15"),width = 35)
e1.place (x = 480, y = 200)

##button 

b1 = Button(root,text = "Search",font = "arial 10",padx = 20, bg = "white" ,command = search)
b1.place (x= 625 , y= 250)

a_b = Button (root, text = "Amazon",font = ("arial 10"),padx = 15,pady = 15, bg = "white" ,command = amazon)
a_b.place (x= 250, y=550)

y_b = Button (root, text = "YouTube",font = ("arial 10"),padx = 15,pady = 15, bg = "white" ,command = youtube)
y_b.place (x= 500, y=550)

fb =Button(root,text = "Facebook",font = ("arial 10"),padx = 15,pady = 15, bg = "white" ,command = Facebook)
fb.place(x = 750 , y = 550)

insta = Button(root,text = "Instagram",font = ("arial 10"),padx = 15,pady = 15, bg = "white" ,command = instagram)
insta.place(x= 1000, y = 550)

root.mainloop()
