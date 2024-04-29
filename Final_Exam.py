import random

class User:
  def __init__(self, name, email, address, account_type, balance=0, transactions=[]): 
    
    self.name = name
    self.email = email
    self.address = address
    self.account_type = account_type
    self.balance = balance
    self.minimum_withdraw = 100
    self.maximum_withdraw = 10000
    self.transactions = transactions
    self.account_number = f"3113{random.randint(100000, 999999)}"  
    self.loan_count = 0 
    users.append(self) 
    print(f"New Account Name: {self.name} created successfully with Account Number: {self.account_number}")

   
  def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        self.transactions.append(f"Deposited: BDT {amount}")
        print(f"Deposited BDT {amount} Successfully.")

  def withdraw(self, amount):
    if amount < self.minimum_withdraw:
        print(f"You cannot withdraw below BDT {self.minimum_withdraw}")
    elif amount > self.maximum_withdraw:
        print(f"The Bank is Bankrupt!! You cannot withdraw more than BDT {self.maximum_withdraw}")
    elif amount > self.balance:
        print("Withdrawal amount exceeded!! Please enter a lower amount.")
    else:
        self.balance -= amount
        self.transactions.append(f"Withdrew: BDT {amount}")
        print(f"Withdrew BDT {amount} Successfully.")

  def check_balance(self):
     print(f"Your current balance is: BDT {self.balance}")

  def transactions_history(self):
    if not self.transactions:
      print("No Transactions!!.")

    else:
      print("Recent Transactions are:")
      for transaction in self.transactions:
        print(transaction)

  def take_loan(self, amount):
    if self.loan_count >= 2:
      print("Loan limit reached. You can only take two loans maximum.")
      return
    
    self.balance += amount
    self.transactions.append(f"Loan: BDT {amount}")
    self.loan_count += 1
    print(f"Loan of BDT {amount} approved.")

  def transfer(self, reciever_account_number, amount):
    reciever_account = find_account(reciever_account_number)
    if not reciever_account:
      print("Account does not exist.")
      return

    if amount > self.balance:
      print("Balance is not sufficient for transfer.")

    else:
      self.balance -= amount
      reciever_account.deposit(amount)
      self.transactions.append(f"Transferred BDT {amount} to {reciever_account.name} (Acc: {reciever_account_number})")
      reciever_account.transactions.append(f"Received BDT {amount} from {self.name} (Acc: {self.account_number})")
      print(f"Transferred BDT {amount} to {reciever_account.name} Successfully.")


class Admin:
  def create_account(self, name, email, address, account_type):
    new_user = User(name, email, address, account_type)

  def delete_account(self, account_number):
    account = find_account(account_number)
    if not account:
      print("Account does not exist.")
      return

    users.remove(account)
    print(f"Account {account_number} deleted successfully.")

  def see_all_accounts(self):
    if not users:
      print("No Accounts Found.")
      return

    print("All User Accounts:")
    for user in users:
      print(f"Name: {user.name}, Account Number: {user.account_number}, Account Type: {user.account_type}")

  def check_total_balance(self):
    total_balance = sum(user.balance for user in users)
    print(f"Total bank balance: BDT {total_balance}")

  def check_total_loan(self):
    total_loan = sum(user.balance - float(user.transactions[0].split()[2].strip("BDT")) for user in users if user.transactions)
    print(f"Total loan amount: BDT {total_loan}")

  def ON_OFF_loan_feature(self, current_state):
    global allow_loans
    allow_loans = not allow_loans
    print(f"Loan feature {'enabled' if allow_loans else 'disabled'}.")


def find_account(account_number):
  for user in users:
    if user.account_number == account_number:
      return
    
    

users = []  

allow_loans = True 
admin_password = "123"

def main():
  while True:
    print("\nWelcome to the Online Banking")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")


    choice = input("Enter your choice: ")

    if choice == '1':
     
      name = input("Enter your name: ")
      email = input("Enter your email: ")
      address = input("Enter your address: ")
      account_type = input("Enter account type (Savings/Current): ").upper()
      new_user = User(name, email, address, account_type)
      
     
    elif choice == '2':
      user_role = input("Enter user role (user/admin): ").lower()
      if user_role == 'user':
        account_number = input("Enter your account number: ")
        account = find_account(account_number)
        if not account:
          print("Invalid account number.")
          continue

        while True:
          print("\nUser Menu")
          print("1. Deposit")
          print("2. Withdraw")
          print("3. Check Balance")
          print("4. Transactions History")
          print("5. Take Loan (if enabled)")
          print("6. Transfer Money")
          print("7. Logout")

          choice = input("Enter your choice: ")

          if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

          elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

          elif choice == '3':
            account.check_balance()

          elif choice == '4':
            account.transactions_history()

          elif choice == '5':
            if allow_loans:
              amount = float(input("Enter amount for loan: "))
              account.take_loan(amount)
            else:
              print("Loan feature is currently disabled.")

          elif choice == '6':
            reciever_account_number = input("Enter reciever account number: ")
            amount = float(input("Enter amount to transfer: "))
            account.transfer(reciever_account_number, amount)

          elif choice == '7':
            break

          else:
            print("Invalid choice.")

      elif user_role == 'admin':
        admin_login = input("Enter admin password: ")

        if admin_login == admin_password:
            admin = Admin()

            while True:
                print("\nAdmin Menu")
                print("1. Create Account")
                print("2. Delete Account")
                print("3. See All Accounts")
                print("4. Check Total Balance")
                print("5. Check Total Loan Amount")
                print("6. ON/Off Loan Feature")
                print("7. Logout")

                choice = input("Enter your choice: ")

                if choice == '1':
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    account_type = input("Enter account type (Savings/Current): ").upper()
                    admin.create_account(name, email, address, account_type)

                elif choice == '2':
                    account_number = input("Enter account number to delete: ")
                    admin.delete_account(account_number)

                elif choice == '3':
                    admin.see_all_accounts()

                elif choice == '4':
                    admin.check_total_balance()

                elif choice == '5':
                    admin.check_total_loan()

                elif choice == '6':
                    admin.ON_OFF_loan_feature(allow_loans)

                elif choice == '7':
                    break

                else:
                    print("Invalid choice.")

            else:
                print("Invalid admin password.")

      else:
        print("Invalid user role.")

    elif choice == '3':
      break

    else:
      print("Invalid choice.")


def find_account(account_number):
  for user in users:
    if user.account_number == account_number:
      return user
  return None

if __name__ == "__main__":
  main()
