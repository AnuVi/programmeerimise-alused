from tkinter import *
aken = Tk()
aken.title("Sauga valla lipp")
louend = Canvas(aken, width=400)
# valge ristkülik
louend.create_rectangle(0, 0, 350, 250 , fill="green", outline="green")
#valge joon vasakul paremale
louend.create_line(0,0, 200,120,0,245, width=20, fill ="white")
korgus = 20
x = 0
i = 0
while i<14:
#tähe joonistamine
    if i >3 and i<8:
        x = 20
        korgus = 35
    if i>9 and i<12:
        x = 40
        korgus = 50
    if i>12:
        x = 60
        korgus = 65
    
    louend.create_polygon( 40+x ,korgus+40, 45+x,korgus+45, 50+x,korgus+45, 46+x,korgus+50, 50+x,korgus+55, 43+x,korgus+52, 35+x,korgus+55,40+x,korgus+50, 35+x,korgus+45,40+x,korgus+45,40+x,korgus+40,  fill="yellow", outline="yellow")
    i+=1
    korgus +=30
# paigutame tahvli raami ja teeme nähtavaks
louend.pack()

# siseneme põhitsüklisse
loend.mainloop()