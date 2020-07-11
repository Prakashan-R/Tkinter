# creating a GUI window using Python Tkinter library
from tkinter import *

def click_me():     #button press cheithu kazhinjal athil nalkirikkunn ee function ayathukondu ethinde ullil enthano
    # nalkirikkunnath athu print cheyyukayo work cheyyukayo cheyyunnu
    
    label2=Label(window, text='welcome')
    label2.pack()

window=Tk()     #frame creat cheyyan oru class ne call cheyyanam athanu Tk()

window.geometry('800x600')     # ithu upayogikkunnathu creat cheitha windowinde size (width & hight) kramikarikan

#creat cheitha windowil nammal nalkunna information display cheyyan upayogikunnathu labelanu

label=Label(window, text='hello world', font=('courier',40), bg='red', fg='white', width=0, height=0)
# labelil nalkun information 'window' enna objectilude main windowileku call cheyyunnu
# labelile enthu informationanu display chayyandathu aa info 'text='ennathil quatsinullil nalkunnu
# nammal nalkunna info ude stylum sizum mattan upayogikunnathu 'font("style",size)'
# ithil 'bg' labelinte background colour chenge cheyyunnu, 'fg' labelil nalkirikkunna info ude color chenge cheyyunnu
# 'width & height' upayogikkunnathu window ude size adjest cheyyananu

label.pack()     # ithu upayogikunnathu nammal nalkirikkunna label main windowil add cheiyyananu

# main widowil nammal oru button creat cheyyunnu

button=Button(window, text='Clickme', bg='yellow', fg='red', font=('courir',30), width=0, height=0, activebackground='green', activeforeground='blue', command=click_me)
#'window' enna objectiloode button main windowleku call chethu
#'text=' ethil buttonil enth text anu display akandathu athu nalkunnu
#'font=("style", size) buttonde text le stylum sizum mattunnu
#'bg & fg' ethu buttonile textindeyum backgroundindeyum colour mattunnu
#'height & width' ithu buttonde size adjest cheyyunnu
#'activebackground & activeforeground' is the button color and text color change to courser enter to button
#'command' upayogikkunnathu enthu functionanu button cheyyandathu athine aa functionilekku call cheithu work cheyyunnu

button.pack() # creat cheitha button main windowil display cheyikkunnu


#oru canvas creat cheithu athil work cheyyunnu
canvas=Canvas(window, width=500, height=400, bg='orange')     # windowil canvas creat cheithu , ethum mattu label button evayil ulla
# pole thanne styles nalkan kazhiyum

canvas.pack()

canvas.create_line(0, 0, 500, 400, width=5, fill='pink', dash=(3,3))
canvas.create_line(0, 400, 500, 0, width=5, fill='pink', dash=(3,3))

#creat_line() ithu oru line canvasil creat cheyyuvan upayogikkunnu
# 0, 0, 500, 400 ee values creat cheyyunna lininte randattathulla X axis Y axis valueskalanu
# 'width=' lininte strength koottunnu
# 'fill=' lininte color mattunnu
# 'dash=' linine dot reethiyil print cheyyunnu

window.mainloop()# ithinte upayogam ee program start cheitha muthal end cheyyunna vare main window closs agthirikkananu