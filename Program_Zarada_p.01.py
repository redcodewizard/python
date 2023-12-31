import os
import webbrowser
from tkinter import messagebox


print("                                 Program Zarada p.01")
print()


def unos_iznosa_zarade():
    while True:
        dozvoljeni_karakteri = "0123456789."

        unos = input("Unesite iznos zarade: ")

        unos = unos.replace(',', '.', 1)

        if all(c in dozvoljeni_karakteri for c in unos):
            return float(unos)
        else:
            print("Pogrešan unos! Molimo unesite samo brojeve.")


def obracun_bruto_1_zarade():
    unos_iznos = unos_iznosa_zarade()
    bruto_1_zarada_iznos = unos_iznos
    porez_na_zaradu_iznos = (bruto_1_zarada_iznos - neoporezivi_iznos) * porez_na_zaradu_stopa
    pio_na_teret_zaposlenog_iznos = bruto_1_zarada_iznos * pio_na_teret_zaposlenog_stopa
    zdr_na_teret_zaposlenog_iznos = bruto_1_zarada_iznos * zdr_na_teret_zaposlenog_stopa
    nez_na_teret_zaposlenog_iznos = bruto_1_zarada_iznos * nez_na_teret_zaposlenog_stopa
    pio_na_teret_poslodavca_iznos = bruto_1_zarada_iznos * pio_na_teret_poslodavca_stopa
    zdr_na_teret_poslodavca_iznos = bruto_1_zarada_iznos * zdr_na_teret_poslodavca_stopa
    nez_na_teret_poslodavca_iznos = bruto_1_zarada_iznos * nez_na_teret_poslodavca_stopa
    neto_zarada_iznos = bruto_1_zarada_iznos - porez_na_zaradu_iznos - pio_na_teret_zaposlenog_iznos - zdr_na_teret_zaposlenog_iznos - nez_na_teret_zaposlenog_iznos
    bruto_2_zarada_iznos = (neto_zarada_iznos - (neoporezivi_iznos * porez_na_zaradu_stopa)) / bruto_2_koeficijent


    print("Neto zarada            : ", f"{neto_zarada_iznos: .2f}")
    print("Porez                  : ", f"{porez_na_zaradu_iznos: .2f}")
    print("PIO na teret zaposlenog: ", f"{pio_na_teret_zaposlenog_iznos: .2f}")
    print("ZDR na teret zaposlenog: ", f"{zdr_na_teret_zaposlenog_iznos: .2f}")
    print("NEZ na teret zaposlenog: ", f"{nez_na_teret_zaposlenog_iznos: .2f}")
    print("PIO na teret poslodavca: ", f"{pio_na_teret_poslodavca_iznos: .2f}")
    print("ZDR na teret poslodavca: ", f"{zdr_na_teret_poslodavca_iznos: .2f}")
    print("NEZ na teret poslodavca: ", f"{nez_na_teret_poslodavca_iznos: .2f}")
    print("Bruto 2 zarada         : ", f"{bruto_2_zarada_iznos: .2f}")


def obracun_neto_zarade():
    unos_iznos = unos_iznosa_zarade()
    bruto_1_zarada_iznos = ((unos_iznos) - (neoporezivi_iznos * porez_na_zaradu_stopa)) / bruto_1_koeficijent
    bruto_2_zarada_iznos = ((unos_iznos) - (neoporezivi_iznos * porez_na_zaradu_stopa)) / bruto_2_koeficijent
    porez_na_zaradu_iznos = (bruto_1_zarada_iznos - neoporezivi_iznos) * porez_na_zaradu_stopa
    pio_na_teret_zaposlenog_iznos = bruto_1_zarada_iznos * pio_na_teret_zaposlenog_stopa
    zdr_na_teret_zaposlenog_iznos = bruto_1_zarada_iznos * zdr_na_teret_zaposlenog_stopa
    nez_na_teret_zaposlenog_iznos = bruto_1_zarada_iznos * nez_na_teret_zaposlenog_stopa
    pio_na_teret_poslodavca_iznos = bruto_1_zarada_iznos * pio_na_teret_poslodavca_stopa
    zdr_na_teret_poslodavca_iznos = bruto_1_zarada_iznos * zdr_na_teret_poslodavca_stopa
    nez_na_teret_poslodavca_iznos = bruto_1_zarada_iznos * nez_na_teret_poslodavca_stopa


    print("Bruto 1 zarada         : ", f"{bruto_1_zarada_iznos: .2f}")
    print("Porez                  : ", f"{porez_na_zaradu_iznos: .2f}")
    print("PIO na teret zaposlenog: ", f"{pio_na_teret_zaposlenog_iznos: .2f}")
    print("ZDR na teret zaposlenog: ", f"{zdr_na_teret_zaposlenog_iznos: .2f}")
    print("NEZ na teret zaposlenog: ", f"{nez_na_teret_zaposlenog_iznos: .2f}")
    print("PIO na teret poslodavca: ", f"{pio_na_teret_poslodavca_iznos: .2f}")
    print("ZDR na teret poslodavca: ", f"{zdr_na_teret_poslodavca_iznos: .2f}")
    print("NEZ na teret poslodavca: ", f"{nez_na_teret_poslodavca_iznos: .2f}")
    print("Bruto 2 zarada         : ", f"{bruto_2_zarada_iznos: .2f}")


def prikaz_koriscenih_stopa_u_programu():
    print("Prikaz koriscenih stopa poreza i doprinosa.\n\n")
    print("Stopa doprinosa za penzijsko i invalidsko osiguranje na teret zaposlenog: ", f"{pio_na_teret_zaposlenog_stopa * 100: .2f}")
    print("Stopa doprinosa za zdravstveno osiguranje na teret zaposlenog           : ", f"{zdr_na_teret_zaposlenog_stopa * 100: .2f}")
    print("Stopa doprinosa za nezaposlenost na teret zaposlenog                    : ", f"{nez_na_teret_zaposlenog_stopa * 100: .2f}")
    print("Stopa doprinosa za penzijsko i invalidsko osiguranje na teret poslodavca: ", f"{pio_na_teret_poslodavca_stopa * 100: .2f}")
    print("Stopa doprinosa za zdravstveno osiguranje na teret poslodavca           : ", f"{zdr_na_teret_poslodavca_stopa * 100: .2f}")
    print("Stopa doprinosa za nezaposlenost na teret poslodavca                    : ", f"{nez_na_teret_poslodavca_stopa * 100: .2f}")


#provera postojanja fajla stope_poreza_i_doprinosa_file.txt
PATH = 'stope_poreza_i_doprinosa_file.txt'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    stope_poreza_i_doprinosa_filename = 'stope_poreza_i_doprinosa_file.txt'
    with open(stope_poreza_i_doprinosa_filename, 'rt') as stope_poreza_i_doprinosa:
        porez_na_zaradu_stopa = float(stope_poreza_i_doprinosa.readline())
        pio_na_teret_zaposlenog_stopa = float(stope_poreza_i_doprinosa.readline())
        zdr_na_teret_zaposlenog_stopa = float(stope_poreza_i_doprinosa.readline())
        nez_na_teret_zaposlenog_stopa = float(stope_poreza_i_doprinosa.readline())
        pio_na_teret_poslodavca_stopa = float(stope_poreza_i_doprinosa.readline())
        zdr_na_teret_poslodavca_stopa = float(stope_poreza_i_doprinosa.readline())
        nez_na_teret_poslodavca_stopa = float(stope_poreza_i_doprinosa.readline())
        neoporezivi_iznos = float(stope_poreza_i_doprinosa.readline())
        bruto_1_koeficijent = float(stope_poreza_i_doprinosa.readline())
        bruto_2_koeficijent = float(stope_poreza_i_doprinosa.readline())


else:
    print("Fajl stope_poreza_i_doprinosa_file.txt nije pronadjen!\n")
    messagebox.showinfo("Poruka", "Fajl stope_poreza_i_doprinosa_file.txt nije pronadjen! Pokretanje programa nije uspesno.")
    quit()


while True:
    unos_izbor = (input(
    "MENI\n\n"
    " 1. Obracun zarade bruto 1 na neto\n\n"
    " 2. Obracun zarade neto na bruto 1\n\n"
    " 3. Prikaz stopa poreza i doprinosa koriscenih u programu\n\n"
    " 4. Prikaz aktuelnih stopa poreza i doprinosa na internetu\n\n"
    " x. Napustiti program\n\n"
    "   Unesite opciju: "))

    print("----------------------------------------------------")

    if unos_izbor == "1":
        print("Obracun zarade bruto 1 na neto\n\n")

        obracun_bruto_1_zarade()

        
    elif unos_izbor == "2":
        print("Obracun zarade neto na bruto 1\n\n")

        obracun_neto_zarade()  


    elif unos_izbor == "3":
        prikaz_koriscenih_stopa_u_programu()


    elif unos_izbor == "4":
        print("Otvaranje internet stranice.")
        webbrowser.open('https://www.poslovnisavetnik.net/statistika/tabelarni-pregled-osnovica-stopa-uplatnih-racuna-i-oznaka-vrste-prihoda-ovp-za-neka-licna-primanja/', new=2)


    elif unos_izbor == "x":
        quit()

    else:
        print("Pogresan unos! Nepostojeca opcija.")
        
    print("----------------------------------------------------")