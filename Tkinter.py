# creating a GUI window using Python Tkinter library
from tkinter import *
window=Tk()     #frame creat cheyyan oru class ne call cheyyanam athanu Tk()

window.geometry('800x400')     # ithu upayogikkunnathu creat cheitha windowinde size (width & hight) kramikarikan

#creat cheitha windowil nammal nalkunna information display cheyyan upayogikunnathu labelanu

label=Label(window, text='hello world', font=('courier',40), bg='red', fg='white', width=200, height=400, justify=LEFT)
# labelil nalkun information 'window' enna objectilude main windowileku call cheyyunnu
# labelile enthu informationanu display chayyandathu aa info 'text='ennathil quatsinullil nalkunnu
# nammal nalkunna info ude stylum sizum mattan upayogikunnathu 'font("style",size)'
# ithil 'bg' labelinte background colour chenge cheyyunnu, 'fg' labelil nalkirikkunna info ude color chenge cheyyunnu
# 'width & height' upayogikkunnathu window ude size adjest cheyyananu

label.pack()     # ithu upayogikunnathu nammal nalkirikkunna label main windowil add cheiyyananu

window.mainloop()# ithinte upayogam ee program start cheitha muthal end cheyyunna vare main window closs agthirikkananu