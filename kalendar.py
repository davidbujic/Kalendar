from time import sleep,strftime,localtime
name = "David"
calendar = {}
def welcome():
    print "Dobro dosli u Kalendar %s" % name
    print "Kalendar se otvara..."
    sleep(1)
    print "Danasnji datum je: " + strftime("%A %B %d, %Y",localtime())
    print "Sada je: " + strftime("%H:%M:%S",localtime())
    sleep(1)
    print "Sta biste zeleli da uradite?"
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("Unesite 'A' za Dodavanje, 'U' za Apdejt, 'V' za Pregled, 'D' za Brisanje, 'X' za Izlaz:  ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print "Kalendar je prazan trenutno."
            else:
                print calendar
        elif user_choice == "U":
            date = raw_input("Koji datum zelite?")
            update = raw_input("Unesite apdejt: ")
            calendar[date] = update
            print "Apdejt uspesan."
            print calendar
        elif user_choice == "A":
            event = raw_input("Unesite dogadjaj: ")
            date = raw_input("Unesite datum(MM/DD/YYYY):")
            if len(date) > 10 or int(date[6:]) < \
            int(strftime("%Y")):
                print "Datum je nepravilno unet."
                try_again = raw_input("Da li zelite da pokusate opet? Y za Da, N za Ne: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print "Dogadjaj je uspesno dodat."
                print calendar
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print "Kalendar je prazan."
            else:
                event = raw_input("Koji dogadjaj zelite da obrisete?")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del(calendar[date])
                        print "Dogadjaj je uspesno obrisan."
                        print calendar
                    else:
                        print "Nekorektan dogadjaj je unet."
        elif user_choice == "X":
            start = False
        else:
            print("Nekorektna komanda je uneta.")
            start = False
start_calendar()
