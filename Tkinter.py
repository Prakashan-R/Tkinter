# creating a GUI window using Python Tkinter library
from tkinter import *
window=Tk()     #frame creat cheyyan oru class ne call cheyyanam athanu Tk()

window.geometry('800x400')     # ithu upayogikkunnathu creat cheitha windowinde size (width & hight) kramikarikan

#creat cheitha windowil nammal nalkunna information display cheyyan upayogikunnathu labelanu

label=Label(window, text='hello world', font=('courier',40), bg='red', fg='white', width=20, height=3)
# labelil nalkun information 'window' enna objectilude main windowileku call cheyyunnu
# labelile enthu informationanu display chayyandathu aa info 'text='ennathil quatsinullil nalkunnu
# nammal nalkunna info ude stylum sizum mattan upayogikunnathu 'font("style",size)'
# ithil 'bg' labelinte background colour chenge cheyyunnu, 'fg' labelil nalkirikkunna info ude color chenge cheyyunnu
# 'width & height' upayogikkunnathu window ude size adjest cheyyananu

label.pack()     # ithu upayogikunnathu nammal nalkirikkunna label main windowil add cheiyyananu

# main widowil nammal oru button creat cheyyunnu

button=Button(window, text='Clickme', bg='yellow', fg='red', font=('courir',30), width=20, height=3)
#'window' enna objectiloode button main windowleku call chethu
#'text=' ethil buttonil enth text anu display akandathu athu nalkunnu
#'font=("style", size) buttonde text le stylum sizum mattunnu
#'bg & fg' ethu buttonile textindeyum backgroundindeyum colour mattunnu
#'height & width' ithu buttonde size adjest cheyyunnu

button.pack() # creat cheitha button main windowil display cheyikkunnu

window.mainloop()# ithinte upayogam ee program start cheitha muthal end cheyyunna vare main window closs agthirikkananu