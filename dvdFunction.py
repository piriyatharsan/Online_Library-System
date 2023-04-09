from modelDvd import LectureDvd

def DVD(dvd):
    print(f"Magazine NO: {dvd.dvd_no}, Title: {dvd.title}, Subject: {dvd.subject}, Rental: {dvd.rental},"
          f" Coopies: {dvd.copy}")


class Dvd_Class:
    def __init__(self):
        self.list_of_dvds = []
        self.value()

    def value(self):
        dvd1 = LectureDvd(dvd_no="10", title="Birth of the Solar System", subject="Astronomy", rental=2.50, copy=10)
        self.list_of_dvds.append(dvd1)
        dvd2 = LectureDvd(dvd_no="11", title="Pythagoras Theorem", subject="Math", rental=1.00, copy=50)
        self.list_of_dvds.append(dvd2)

    def add(self):
        dvd = input("Enter DVD No to add the lecturer DVD:")
        title = input("Enter title of the Dvd:")
        subject = input("Enter Subject of the Dvd:")
        try:
            rental = float(input("Enter rental of the Dvd:"))
        except ValueError:
            print("Invalid rental price  type again!!!")
            return ()
        try:
            copy = int(input("Enter copy of the Dvd:"))
        except ValueError:
            print("Invalid copy type again!!!!")
            return ()

        dvd = LectureDvd(dvd_no=dvd, title=title, subject=subject, rental=rental, copy=copy)
        self.list_of_dvds.append(dvd)
        print("DVD added to our Online Library")

    def remove(self):
        dvd = input("Enter DVD No to remove the DVD:")
        match_data = list(x for x in self.list_of_dvds if x.dvd_no == dvd)
        for x in match_data:
            self.list_of_dvds.remove(x)
            print("DVD removed from our online Library")

    def show_available(self):
        match_data = list(item for item in self.list_of_dvds if item.copy > 0)
        for x in match_data:
            DVD(x)

    def show_unavailable(self):
        match_data = list(item for item in self.list_of_dvds if item.copy <= 0)
        if len(match_data) >0:
           for x in match_data:
              DVD(x)
        else:
            print("all DVD are avilable")

    def show_lend(self):
        dvd = input("Enter DVD No to Lend: ")
        copies = int(input("Enter copies"))
        match_data = list(item for item in self.list_of_dvds if item.dvd_no == dvd)
        for x in match_data:
            x.copy -= copies
            print("DVD lent to you")

    def show_receive(self):
        dvd = input("Enter DVD No to receive:")
        copies = int(input("Enter copies"))
        match_data = list(item for item in self.list_of_dvds if item.dvd_no == dvd)
        for x in match_data:
            x.copy += copies
            print("DVD received from you")

    def search_by_subject(self):
        subject_name = input("enter subject to filter:")
        matched_data = list(item for item in self.list_of_dvds if item.subject == subject_name)
        if len(matched_data) > 0:
            for x in matched_data:
                DVD(x)
