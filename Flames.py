import os
class Flames:
    name1 = ""
    name2 = ""
    count = 0


    def __init__(self, name1=None, name2=None):
        os.system("cls")
        if name1 is None and name2 is None:
            self.name1 = input("Enter your name >> ").upper().replace(" ", "")
            self.name2 = input("Enter your partner's name >> ").upper().replace(" ", "")
        elif name1 is not None and name2 is not None:
            self.name1 = name1.upper().replace(" ", "")
            self.name2 = name2.upper().replace(" ", "")
        else:
            self.name1 = self.name1.upper().replace(" ", "")
            self.name2 = self.name2.upper().replace(" ", "")
        self.strike_out()
    
    def strike_out(self):
        name1 = self.name1
        name2 = self.name2
        for i in name1:
            if i in name2:
                name1 = name1.replace(str(i), "", 1)
                name2 = name2.replace(str(i), "", 1)
        self.count = len(name1) + len(name2)

    def get_relation(self):
        count = self.count - 1
        pos = 0
        flames = "FLAMES"
        for i in range(5):
           pos += count
           pos %= len(flames)
           flames = flames.replace(flames[pos], "")

        print('\n')
        if flames == 'F':
            print(f"{self.name1.capitalize()} and {self.name2.capitalize()} are destined to be Friends and nothing more!!")
            self.print_friend()
        elif flames == 'L':
            print(f"{self.name1.capitalize()} and {self.name2.capitalize()} are destined to be Lovers!!")
            self.print_love()
        elif flames == 'A':
            print(f"{self.name1.capitalize()} and {self.name2.capitalize()} are destined to have an Affair!!")
            self.print_affair()
        elif flames == 'M':
            print(f"{self.name1.capitalize()} and {self.name2.capitalize()} are destined for Marriage!!")
            self.print_marriage()
        elif flames == 'E':
            print(f"{self.name1.capitalize()} and {self.name2.capitalize()} are destined to be Enemies!!")
            self.print_enemies()
        elif flames == 'S':
            print(f"{self.name1.capitalize()} and {self.name2.capitalize()} are Siblings!?")
            self.print_siblings()
        print('\n')
    
    def print_friend(self):
        print("Relation:")
        border = "═" * 55
        print()
        print("╔" + border + "╗")
        print("║ " + "███████╗██████╗ ██╗███████╗███╗   ██╗██████╗ ███████╗" + " ║")
        print("║ " + "██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗██╔════╝" + " ║")
        print("║ " + "█████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║███████╗" + " ║")
        print("║ " + "██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║╚════██║" + " ║")
        print("║ " + "██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝███████║" + " ║")
        print("║ " + "╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝" + " ║")
        print("╚" + border + "╝")

    def print_love(self):
        print("Relation:")
        border = "═" * 36
        print()
        print("╔" + border + "╗")
        print("║ " + "██╗      ██████╗ ██╗   ██╗███████╗" + " ║")
        print("║ " + "██║     ██╔═══██╗██║   ██║██╔════╝" + " ║")
        print("║ " + "██║     ██║   ██║██║   ██║█████╗  " + " ║")
        print("║ " + "██║     ██║   ██║╚██╗ ██╔╝██╔══╝  " + " ║")
        print("║ " + "███████╗╚██████╔╝ ╚████╔╝ ███████╗" + " ║")
        print("║ " + "╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝" + " ║")
        print("╚" + border + "╝")

    def print_affair(self):
        print("Relation:")
        border = "═" * 45
        print("╔" + border + "╗")
        print("║ " + " █████╗ ███████╗███████╗ █████╗ ██╗██████╗ " + " ║")
        print("║ " + "██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗" + " ║")
        print("║ " + "███████║█████╗  █████╗  ███████║██║██████╔╝" + " ║")
        print("║ " + "██╔══██║██╔══╝  ██╔══╝  ██╔══██║██║██╔══██╗" + " ║")
        print("║ " + "██║  ██║██║     ██║     ██║  ██║██║██║  ██║" + " ║")
        print("║ " + "╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝" + " ║")
        print("╚" + border + "╝")   
    
    def print_marriage(self):
        print("Relation:")
        border = "═" * 65
        print()
        print("╔" + border + "╗")
        print("║ " + "███╗   ███╗ █████╗ ██████╗ ██████╗ ██╗ █████╗  ██████╗ ███████╗" + " ║")
        print("║ " + "████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝" + " ║")
        print("║ " + "██╔████╔██║███████║██████╔╝██████╔╝██║███████║██║  ███╗█████╗  " + " ║")
        print("║ " + "██║╚██╔╝██║██╔══██║██╔══██╗██╔══██╗██║██╔══██║██║   ██║██╔══╝  " + " ║")
        print("║ " + "██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║██║██║  ██║╚██████╔╝███████╗" + " ║")
        print("║ " + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝" + " ║")
        print("╚" + border + "╝")

    def print_enemies(self):
        print("Relation:")
        border = "═" * 58
        print("╔" + border + "╗")
        print("║ " + "███████╗███╗   ██╗███████╗███╗   ███╗██╗███████╗███████╗" + " ║")
        print("║ " + "██╔════╝████╗  ██║██╔════╝████╗ ████║██║██╔════╝██╔════╝" + " ║")
        print("║ " + "█████╗  ██╔██╗ ██║█████╗  ██╔████╔██║██║█████╗  ███████╗" + " ║")
        print("║ " + "██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║██╔══╝  ╚════██║" + " ║")
        print("║ " + "███████╗██║ ╚████║███████╗██║ ╚═╝ ██║██║███████╗███████║" + " ║")
        print("║ " + "╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝" + " ║")
        print("╚" + border + "╝")

    def print_siblings(self):    
        print("Relation:")    
        border = "═" * 59
        print()
        print("╔" + border + "╗")
        print("║ " + "███████╗██╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗ ███████╗" + " ║")
        print("║ " + "██╔════╝██║██╔══██╗██║     ██║████╗  ██║██╔════╝ ██╔════╝" + " ║")
        print("║ " + "███████╗██║██████╔╝██║     ██║██╔██╗ ██║██║  ███╗███████╗" + " ║")
        print("║ " + "╚════██║██║██╔══██╗██║     ██║██║╚██╗██║██║   ██║╚════██║" + " ║")
        print("║ " + "███████║██║██████╔╝███████╗██║██║ ╚████║╚██████╔╝███████║" + " ║")
        print("║ " + "╚══════╝╚═╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝" + " ║")
        print("╚" + border + "╝")


run = True
while (run):
    couple = Flames()
    couple.get_relation()
    while (True):
        ch = input ("Would like to check the fate of another pair? (Y/N) >> ")
        if ch == 'N' or ch == 'n':
            run = False
            break
        elif ch == 'Y' or ch == 'y':
            print(end="\n\n")
            break
        else:
            print("\n\nInvalid Input!!\n\n")
            continue


