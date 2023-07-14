import os
from tkinter import*
from tkinter import messagebox

frame=Tk()
frame.geometry("430x380")
frame.title("Zarada")
frame.resizable(False, False)

window_Width = frame.winfo_reqwidth()
window_Height = frame.winfo_reqheight()
 
pozicija_Desno = int(frame.winfo_screenwidth()/3 - window_Width/2)
position_Dole = int(frame.winfo_screenheight()/4 - window_Height/2)
 
frame.geometry("+{}+{}".format(pozicija_Desno, position_Dole))

if os.path.exists("stope_poreza_i_doprinosa_python.txt"):
    print("Eksterni fajl ucitan.")
else:
    print("Eksterni fajl nije ucitan.")
    messagebox.showinfo("Poruka", "Eksterni fajl nije ucitan. Pokretanje programa nije uspesno.")
    quit()

Var1 = IntVar(value = 2)
Var2 = IntVar(value = 1)

frame.izbor = 2
frame.izbor2 = 1

def u1():
    frame.izbor2 = 1

def u2():
    frame.izbor2 = 2;

def r1():
    frame.izbor = 1

def r2():
    frame.izbor = 2;

def oprogramu():
    messagebox.showinfo("O programu", "Naziv programa: Zarada p.02\nAutor: Red Code Wizard\nPoslednje azuriranje: 14/07/23")

def eksternifajl():
    os.system("stope_poreza_i_doprinosa_python.txt")

menubar = Menu(frame)

fajl_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fajl", menu=fajl_menu)
fajl_menu.add_command(label="O programu", command=oprogramu)
fajl_menu.add_command(label="Eksterni fajl", command=eksternifajl)


def funkcija():
    print("Unos pokrenut.")

    try:
        unos = float(entry.get())

        stope_poreza_i_doprinosa = open('stope_poreza_i_doprinosa_python.txt', "rt")
        porez_na_zaradu_stopa = float(stope_poreza_i_doprinosa.readline())
        pio_na_teret_zaposlenog_stopa = float(stope_poreza_i_doprinosa.readline())
        zdr_na_teret_zaposlenog_stopa = float(stope_poreza_i_doprinosa.readline())
        nez_na_teret_zaposlenog_stopa = float(stope_poreza_i_doprinosa.readline())
        pio_na_teret_poslodavca_stopa = float(stope_poreza_i_doprinosa.readline())
        zdr_na_teret_poslodavca_stopa = float(stope_poreza_i_doprinosa.readline())
        nez_na_teret_poslodavca_stopa = float(stope_poreza_i_doprinosa.readline())
        neoporezivi_iznos = float(stope_poreza_i_doprinosa.readline())
        
        #Ugovor o radu
        if(frame.izbor2 == 1):
            print("Ugovor o radu pokrenut.")
            if frame.izbor == 1:
                print("Bruto zarada pokrenuta.")
                bruto_1_zarada_iznos = unos
        
                porez_iznos = ((bruto_1_zarada_iznos - neoporezivi_iznos) * porez_na_zaradu_stopa)
                pio_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * pio_na_teret_zaposlenog_stopa);
                zdr_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * zdr_na_teret_zaposlenog_stopa);
                nez_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * nez_na_teret_zaposlenog_stopa);
                pio_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * pio_na_teret_poslodavca_stopa);
                zdr_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * zdr_na_teret_poslodavca_stopa);
                nez_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * nez_na_teret_poslodavca_stopa);
                bruto_2_zarada_iznos = unos + pio_na_teret_poslodavca_iznos + zdr_na_teret_poslodavca_iznos + nez_na_teret_poslodavca_iznos     
                neto_zarada_iznos = 0.701 * bruto_1_zarada_iznos + porez_iznos

                label_bruto_1_iznos_prikaz.config(text=format(bruto_1_zarada_iznos, '.2f'))
                label_porez_prikaz.config(text=format(porez, '.2f'))
                label_pio_na_teret_zaposlenog_iznos_prikaz.config(text=format(pio_na_teret_zaposlenog_iznos, '.2f'))
                label_zdr_na_teret_zaposlenog_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))   
                label_nez_na_teret_zaposlenog_iznos_prikaz.config(text=format(nez_na_teret_zaposlenog_iznos, '.2f'))
                label_pio_na_teret_poslodavca_iznos_prikaz.config(text=format(pio_na_teret_poslodavca_iznos, '.2f'))
                label_zdr_na_teret_poslodavca_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))
                label_nez_na_teret_poslodavca_iznos_prikaz.config(text=format(nez_na_teret_poslodavca_iznos, '.2f'))
                label_bruto_2_iznos_prikaz.config(text=format(bruto_2_zarada_iznos, '.2f'))
                label_neto_prikaz.config(text=format(neto_zarada_iznos, '.2f'))

            if frame.izbor == 2:
                print("Neto zarada pokrenuta.")
                bruto_1_zarada_iznos = ((unos -(neoporezivi_iznos*porez_na_zaradu_stopa))/0.701)
                bruto_2_zarada_iznos = ((unos-(neoporezivi_iznos*porez_na_zaradu_stopa))/0.600943)
                porez = ((bruto_1_zarada_iznos - neoporezivi_iznos) * porez_na_zaradu_stopa)
                pio_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * pio_na_teret_zaposlenog_stopa);
                zdr_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * zdr_na_teret_zaposlenog_stopa);
                nez_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * nez_na_teret_zaposlenog_stopa);
                pio_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * pio_na_teret_poslodavca_stopa);
                zdr_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * zdr_na_teret_poslodavca_stopa);
                nez_na_teret_poslodavca_iznos  = (bruto_1_zarada_iznos * nez_na_teret_poslodavca_stopa);
                neto_zarada_iznos = unos

                label_bruto_1_iznos_prikaz.config(text=format(bruto_1_zarada_iznos, '.2f'))
                label_porez_prikaz.config(text=format(porez, '.2f'))
                label_pio_na_teret_zaposlenog_iznos_prikaz.config(text=format(pio_na_teret_zaposlenog_iznos, '.2f'))
                label_zdr_na_teret_zaposlenog_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))   
                label_nez_na_teret_zaposlenog_iznos_prikaz.config(text=format(nez_na_teret_zaposlenog_iznos, '.2f'))
                label_pio_na_teret_poslodavca_iznos_prikaz.config(text=format(pio_na_teret_poslodavca_iznos, '.2f'))
                label_zdr_na_teret_poslodavca_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))
                label_nez_na_teret_poslodavca_iznos_prikaz.config(text=format(nez_na_teret_poslodavca_iznos, '.2f'))
                label_bruto_2_iznos_prikaz.config(text=format(bruto_2_zarada_iznos, '.2f'))
                label_neto_prikaz.config(text=format(neto_zarada_iznos, '.2f'))

        #Ugovor o pp
        elif(frame.izbor2 == 2):
            print("Ugovor o pp pokrenut.")
            if frame.izbor == 1:
                print("Bruto zarada pokrenuta.")
                bruto_1_zarada_iznos = unos
        
                porez = ((bruto_1_zarada_iznos) * porez_na_zaradu_stopa)
                pio_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * pio_na_teret_zaposlenog_stopa);
                zdr_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * zdr_na_teret_zaposlenog_stopa);
                nez_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * nez_na_teret_zaposlenog_stopa);
                pio_na_teret_poslodavca_iznos        = (bruto_1_zarada_iznos * pio_na_teret_poslodavca_stopa);
                zdr_na_teret_poslodavca_iznos       = (bruto_1_zarada_iznos * zdr_na_teret_poslodavca_stopa);
                nez_na_teret_poslodavca_iznos      = (bruto_1_zarada_iznos * nez_na_teret_poslodavca_stopa);
                bruto_2_zarada_iznos = unos + pio_na_teret_poslodavca_iznos        + zdr_na_teret_poslodavca_iznos       + nez_na_teret_poslodavca_iznos     
                neto_zarada_iznos = 0.701 * bruto_1_zarada_iznos


                label_bruto_1_iznos_prikaz.config(text=format(bruto_1_zarada_iznos, '.2f'))
                label_porez_prikaz.config(text=format(porez, '.2f'))
                label_pio_na_teret_zaposlenog_iznos_prikaz.config(text=format(pio_na_teret_zaposlenog_iznos, '.2f'))
                label_zdr_na_teret_zaposlenog_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))   
                label_nez_na_teret_zaposlenog_iznos_prikaz.config(text=format(nez_na_teret_zaposlenog_iznos, '.2f'))
                label_pio_na_teret_poslodavca_iznos_prikaz.config(text=format(pio_na_teret_poslodavca_iznos, '.2f'))
                label_zdr_na_teret_poslodavca_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))
                label_nez_na_teret_poslodavca_iznos_prikaz.config(text=format(nez_na_teret_poslodavca_iznos, '.2f'))
                label_bruto_2_iznos_prikaz.config(text=format(bruto_2_zarada_iznos, '.2f'))
                label_neto_prikaz.config(text=format(neto_zarada_iznos, '.2f'))

            if frame.izbor == 2:
                print("Neto zarada pokrenuta.")
                bruto_1_zarada_iznos = ((unos)/0.701)
                bruto_2_zarada_iznos = ((unos)/0.600943)
                porez = ((bruto_1_zarada_iznos) * porez_na_zaradu_stopa)
                pio_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * pio_na_teret_zaposlenog_stopa);
                zdr_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * zdr_na_teret_zaposlenog_stopa);
                nez_na_teret_zaposlenog_iznos = (bruto_1_zarada_iznos * nez_na_teret_zaposlenog_stopa);
                pio_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * pio_na_teret_poslodavca_stopa);
                zdr_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * zdr_na_teret_poslodavca_stopa);
                nez_na_teret_poslodavca_iznos = (bruto_1_zarada_iznos * nez_na_teret_poslodavca_stopa);
                neto_zarada_iznos = unos


                label_bruto_1_iznos_prikaz.config(text=format(bruto_1_zarada_iznos, '.2f'))
                label_porez_prikaz.config(text=format(porez, '.2f'))
                label_pio_na_teret_zaposlenog_iznos_prikaz.config(text=format(pio_na_teret_zaposlenog_iznos, '.2f'))
                label_zdr_na_teret_zaposlenog_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))   
                label_nez_na_teret_zaposlenog_iznos_prikaz.config(text=format(nez_na_teret_zaposlenog_iznos, '.2f'))
                label_pio_na_teret_poslodavca_iznos_prikaz.config(text=format(pio_na_teret_poslodavca_iznos, '.2f'))
                label_zdr_na_teret_poslodavca_iznos_prikaz.config(text=format(zdr_na_teret_zaposlenog_iznos, '.2f'))
                label_nez_na_teret_poslodavca_iznos_prikaz.config(text=format(nez_na_teret_poslodavca_iznos, '.2f'))
                label_bruto_2_iznos_prikaz.config(text=format(bruto_2_zarada_iznos, '.2f'))
                label_neto_prikaz.config(text=format(neto_zarada_iznos, '.2f'))

        
    except:
        messagebox.showinfo("Poruka", "Greska u unosu.")
        entry.delete(0,50)


def danka(event):
    funkcija()

frame.bind('<Return>', danka)


label_razmak1 = Label(frame, width = 2, bg="purple")
label_razmak1.grid(row=0, column=0)


#Ugovor radiobutton
u1 = Radiobutton(frame, text="Ugovor o radu", value=1, width = 14, font='TimesNewRoman 10 bold', command = u1, variable = Var2, bg="orange", anchor="w")
u1.grid(row=1, column=1)

u2 = Radiobutton(frame, text="Ugovor o pp", value=2, width = 14, font='TimesNewRoman 10 bold', command = u2, variable = Var2, bg="orange", anchor="w")
u2.grid(row=1, column=2)


#Zarada radiobutton
R1 = Radiobutton(frame, text="Bruto zarada", value=1, width = 14, font='TimesNewRoman 10 bold', command = r1, variable = Var1, anchor="w")
R1.grid(row=2, column=2)

R2 = Radiobutton(frame, text="Neto zarada", value=2, width = 14, font='TimesNewRoman 10 bold', command = r2, variable = Var1, anchor="w")
R2.grid(row=2, column=1)


label_razmak1 = Label(frame, width = 2, bg="purple")
label_razmak1.grid(row=3, column=3)


label = Label(frame, text="Unesite zaradu: ", anchor="w", width = 17, font='TimesNewRoman 10 bold')
label.grid(row=4, column=1)

entry = Entry(frame, width = 15, font='TimesNewRoman 12 bold')
entry.grid(row=4, column=2)

button = Button(frame, text = "Unos", command = funkcija, width = 14, font='TimesNewRoman 8 bold')
button.grid(row=4, column=3)

label_razmak2 = Label(frame, width = 2, bg="purple")
label_razmak2.grid(row=5, column=0)

label_bruto1_naslov = Label(frame, text="Bruto 1 zarada: ", anchor="w", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_bruto1_naslov.grid(row=6, column=1)

label_porez_naslov = Label(frame, text="Porez na zaradu: ", anchor="w", width = 17, font='TimesNewRoman 10 bold')
label_porez_naslov.grid(row=7, column=1)

label_pio_na_teret_zaposlenog_iznos_naslov = Label(frame, text="PIO(na teret zap.): ", anchor="w", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_pio_na_teret_zaposlenog_iznos_naslov.grid(row=8, column=1)

label_zdr_na_teret_zaposlenog_iznos_naslov = Label(frame, text="ZDR(na teret zap.): ", anchor="w", width = 17, font='TimesNewRoman 10 bold')
label_zdr_na_teret_zaposlenog_iznos_naslov.grid(row=9, column=1)

label_nez_na_teret_zaposlenog_iznos_naslov = Label(frame, text="NEZ(na teret zap.): ", anchor="w", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_nez_na_teret_zaposlenog_iznos_naslov.grid(row=10, column=1)

label_pio_na_teret_poslodavca_iznos_naslov = Label(frame, text="PIO(na teret pos.): ", anchor="w", width = 17, font='TimesNewRoman 10 bold')
label_pio_na_teret_poslodavca_iznos_naslov.grid(row=11, column=1)

label_zdr_na_teret_poslodavca_iznos_naslov = Label(frame, text="ZDR(na teret pos.): ", anchor="w", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_zdr_na_teret_poslodavca_iznos_naslov.grid(row=12, column=1)

label_nez_na_teret_poslodavca_iznos_naslov = Label(frame, text="NEZ(na teret pos.): ", anchor="w", width = 17, font='TimesNewRoman 10 bold')
label_nez_na_teret_poslodavca_iznos_naslov.grid(row=13, column=1)

label_bruto_2_iznos_prikaz = Label(frame, text="Bruto 2 zarada: ", anchor="w", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_bruto_2_iznos_prikaz.grid(row=14, column=1)

label_neto_naslov = Label(frame, text="Neto zarada: ", anchor="w", width = 17, font='TimesNewRoman 10 bold')
label_neto_naslov.grid(row=15, column=1)

label_bruto_1_iznos_prikaz = Label(frame, text="-", anchor="e", bg="white", width = 17, font='TimesNewRoman 10 bold')
label_bruto_1_iznos_prikaz.grid(row=6, column=2)

label_porez_prikaz = Label(frame, text="-", anchor="e", width = 17, font='TimesNewRoman 10 bold')
label_porez_prikaz.grid(row=7, column=2)

label_pio_na_teret_zaposlenog_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_pio_na_teret_zaposlenog_iznos_prikaz.grid(row=8, column=2)

label_zdr_na_teret_zaposlenog_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, font='TimesNewRoman 10 bold')
label_zdr_na_teret_zaposlenog_iznos_prikaz.grid(row=9, column=2)

label_nez_na_teret_zaposlenog_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_nez_na_teret_zaposlenog_iznos_prikaz.grid(row=10, column=2)

label_pio_na_teret_poslodavca_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, font='TimesNewRoman 10 bold')
label_pio_na_teret_poslodavca_iznos_prikaz.grid(row=11, column=2)

label_zdr_na_teret_poslodavca_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_zdr_na_teret_poslodavca_iznos_prikaz.grid(row=12, column=2)

label_nez_na_teret_poslodavca_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, font='TimesNewRoman 10 bold')
label_nez_na_teret_poslodavca_iznos_prikaz.grid(row=13, column=2)

label_bruto_2_iznos_prikaz = Label(frame, text="-", anchor="e", width = 17, bg="white", font='TimesNewRoman 10 bold')
label_bruto_2_iznos_prikaz.grid(row=14, column=2)

label_neto_prikaz = Label(frame, text="-", anchor="e", width = 17, font='TimesNewRoman 10 bold')
label_neto_prikaz.grid(row=15, column=2)

frame.config(menu=menubar, bg="purple")
frame.mainloop()