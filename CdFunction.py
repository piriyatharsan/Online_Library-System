from modelCd import CD
def pCD(cd):
    print(f"Magazine NO: {cd.cd_no}, Title: {cd.title}, Subject: {cd.subject}, Rental: {cd.rental}, Coopies: {cd.copy}")

class Cd_Class:
    def __init__(self):
        self.list_of_cds = []
        self.data()

    def data(self):
        cd1 = CD(cd_no="21", title="Basics of Western Music, Music", subject="Music", rental=1.50, copy=11)
        self.list_of_cds.append(cd1)
        cd2 = CD(cd_no="22", title="Japanese Language", subject="Foreign Languages", rental=2.00, copy=3)
        self.list_of_cds.append(cd2)



    def add(self):
        cd = input("Enter cd no to add libary: ")
        title = input("Enter title to cd ")
        subject = input("Enter Subject for cd ")
        try:
            rental = float(input("Enter rental price of cd per day:"))
        except ValueError:
            print("Invalid rental type so please enter correctly!!!")
            return ()
        try:
            copy = int(input("Enter copy of book:"))
        except ValueError:
            print("Invalid copy type so please enter correctly!!!")
            return ()

        cd = CD(cd_no=cd, title=title, subject=subject, rental=rental, copy=copy)
        self.list_of_cds.append(cd)
        print("The cd added")

    def remove(self):
        cd = input("Enter cd no to romove: ")
        match_data = list(item for item in self.list_of_cds if item.cd_no == cd)
        for x in match_data:
            self.list_of_cds.remove(x)
            print("cd removed from our online libary")

    def show_available(self):
        match_data = list(item for item in self.list_of_cds if item.copy > 0)
        for x in match_data:
            pCD(x)

    def show_unavailable(self):
        match_data = list(item for item in self.list_of_cds if item.copy <= 0)
        if len(match_data) >0:
          for x in match_data:
            pCD(x)
        else:
            print("all CD are avialable")

    def show_lend(self):
        cd = input("Enter cd no to lend cd:")
        copies = int(input("Enter copies"))
        match_data = list(item for item in self.list_of_cds if item.cd_no == cd)
        for x in match_data:
            x.copy -= copies
            print("cd lent")

    def show_receive(self):
        cd = input("Enter cd no to recive:")
        copies = int(input("Enter copies"))
        match_data = list(item for item in self.list_of_cds if item.cd_no == cd)
        for x in match_data:
            x.copy += copies
            print("Cd received")

    def search_by_subject(self):
        subject_name = input("enter subject to filter:")
        matched_data = list(item for item in self.list_of_cds if item.subject == subject_name)
        if len(matched_data) > 0:
            for x in matched_data:
                pCD(x)
