from modelMagazine import Magazine

def pmagazine(magazine):
    print(f"Magazine NO: {magazine.mag_No}, Title: {magazine.title}, Color: {magazine.color}, "
          f"Subject: {magazine.subject}, Rental: {magazine.rental}, Coopies: {magazine.copy}")


class Mag_Class :
    def __init__(self):
        self.list_of_mags=[]
        self.value()

    def value(self):
        mag_A=Magazine(mag_no="01", title="History of Cricket", color="color", subject="Sports", rental=5.00, copy=7)
        self.list_of_mags.append(mag_A)
        mag_B=Magazine(mag_no="02", title="Evolution of the Computer", color="black&white", subject="Technology",
                       rental=3.00, copy=21)
        self.list_of_mags.append(mag_B)

    def add(self):
        mag=input("Enter Magazine number:")
        title=input("Enter title  of the Magazine:")
        color=input("Enter color of the Magazine:")
        subject=input("Enter Subject of the Magazine: ")
        try:
            rental=float(input("Enter rental of the Magazine: "))
        except ValueError:
            print("Invaild  Rental Price type again crrectly")
            return()
        try:
            copy=int(input("Enter copy of the Magazine: "))
        except ValueError:
            print("Invaild  copy type again crrectly")
            return ()

        magS=Magazine(mag_no=mag, title=title, color=color, subject=subject, rental=rental, copy=copy)
        self.list_of_mags.append(magS)
        print("Magazine added to our online Libary")

    def remove(self):
        mag=input("Enter Magazine number to remove the Magazine:")
        match_data=list(item for item in self.list_of_mags if item.mag_No == mag)
        for x in match_data:
            self.list_of_mags.remove(x)
            print("Magazine removed from our Libary")

    def show_available(self):
        match_data=list(item for item in self.list_of_mags if item.copy > 0)
        for x in match_data:
            pmagazine(x)

    def show_unavailable(self):
        match_data=list(item for item in self.list_of_mags if item.copy == 0)
        if len(match_data) > 0:
           for x in match_data:
              pmagazine(x)
        else:
            print("all MAgazine are availble")

    def show_lend(self):
        mag=input("Enter Magazine no to lend the Magazine:")
        copies=int(input("Enter copies:"))
        match_data=list(item for item in self.list_of_mags if item.mag_No == mag)
        if len(match_data) > 0:
           for x in match_data:
             x.copy-=copies
             print("Magazine lent to you")
        else:
            print("all magazine are availble")

    def show_receive(self):
        mag=input("Enter Magzine No to recevie:")
        copies=int(input("Enter copies:"))
        match_data=list(item for item in self.list_of_mags if item.mag_No == mag)
        for x in match_data:
            x.copy+=copies
            print("Magazine received from you thank you")

    def search_by_subject(self):
        subject_name = input("enter subject to filter:")
        matched_data = list(item for item in self.list_of_mags if item.subject == subject_name)
        if len(matched_data) > 0:
            for magazine in matched_data:
                pmagazine(magazine)
