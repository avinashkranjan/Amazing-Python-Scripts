class BAC(object):
    def __init__(self,weight, time, vol, amount, gender):
        self.weight = weight
        self.time = time 
        self.vol = vol
        self.amount = amount
        self.gender = gender 
        self.std = 0.0068 
    def standard_drink(self):
        return round((self.std * self.vol) * self.amount, 2)
    def promille_man(self):
        return round((self.standard_drink() * 12) / ((self.weight*1.7) - (0.15*self.time)), 2)
    def promille_woman(self):
        return round((self.standard_drink() * 12) / ((self.weight*1.6) - (0.15*self.time)), 2)


    def result(self):
        if self.gender == 'woman':
            print(f'\nAs a woman who have had {self.amount} cl. of {self.vol}% vol, {self.time} hour ago.')
            print(f'You`ve had {self.standard_drink()} drinks,which gives you a {self.promille_woman()}% BAC\n')
        elif self.gender == 'man':
            print(f'\nAs a man who have had {self.amount} cl. of {self.vol}% vol, {self.time} hour ago.')
            print(f'You`ve had {self.standard_drink()} drinks,which gives you a {self.promille_man()}% BAC\n')
        else:
            print("Fault.")

if __name__ == "__main__":
    weight = int(input("Weight of the patient in kg: "))
    time = int(input("Enter the time of drink (in hour only): "))
    vol  = float(input("Volume percent of alcohol in the drink:"))
    amount = int(input("Enter the amount the you drank: "))
    gender = str(input("You are man or woman: "))

    BAC(weight,time,vol,amount,gender).result()
