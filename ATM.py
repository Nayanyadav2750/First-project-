class Atm:
    
    def __init__(self):
        self.pin = ""
        self.balance = 0 
        
        self.menu()
    def menu(self):
        while True:
             
         user_input = input("""
                      1. for Create pin 
                      2. For check balance
                      3. For deposit 
                      4. For withdraw
                      """)
                      
         if user_input == "1":
                       self.create_pin()
         elif user_input == "2":
                self.check_balance()
         elif user_input == "3":
                self.deposit()
         elif user_input == "4":
                self.withdraw()
         elif user_input == "5":
             print ("exit form bank")
             break
         else :
              print("Invalid input")
        
    def create_pin(self):
        self.pin = int(input("Enter the pin >>"))
        print("pin is set successfully")
            
    def check_balance(self):
        check_pin = int(input("Enter the valid pin>>"))
        if check_pin == self.pin :
         print(f"Your balance is >>  {self.balance}")
        else :
             print ("Pin is invalid") 
        
    def deposit(self):
        amount = int (input("enter the amount"))
        self.balance  = self.balance + amount
        print ("money is deposited ")
        
    def withdraw(self):
        amount= int(input("Enter the amount want to withdraw>>"))
        if amount <= self.balance :
            self.balance = self.balance - amount
        else :
            print ( " Insufficient Balance ")
        print("The balance is >>",self.balance)    
SBI = Atm()

        
        
        
        
        
        
        
        
        
        
        
        