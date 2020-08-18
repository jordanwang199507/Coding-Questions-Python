class BankAccount:
	def __init__(self, name, accountNumber, balance):
		self.name = name
		self.accountNumber = accountNumber
		self.balance = balance

	def getBalance(self):
		print("The account balance is: $"+self.balance)

	def getAccountName(self):
		print("The account name is: "+self.name)

	def getAccountNumber(self):
		print("The account number is: "+self.accountNumber)
	
	def deposit(self, money):
		self.balance = int(self.balance) + int(money)
		print ("The account balance is: $" + str(self.balance))

	def withdraw(self, money):
		self.balance = int(self.balance) - int(money)
		print("The account blance is: $" + str(self.balance))

number_of_account = int(input("Enter the number of accounts wish to open: "))
BankAccounts = [] 
for i in range(number_of_account+1): 
	if (i == 0):
		person_name = "none"
		person_number = 0000
		person_balance = 00
		BankAccounts.append(BankAccount(person_name, person_number, person_balance))
	else:	
		print("Account {}".format(i))
		person_name = input("Enter account holder's name: ")
		person_number = input("Enter account number: ")
		person_balance = input("Enter account balance: ")
		BankAccounts.append(BankAccount(person_name, person_number, person_balance))
		print()

account_access = int(input("Enter the account number to access: "))
print("select operation.")
print("1. Get Account Name")
print("2. Get Account Number")
print("3. Get Balance")
print("4. Get All Information")
choice = input("Enter choice(1/2/3/4): ")
if choice == '1':
	BankAccounts[account_access].getAccountName()
elif choice == '2':	
	BankAccounts[account_access].getAccountNumber()
elif choice == '3':
	BankAccounts[account_access].getBalance()
elif choice == '4':
	BankAccounts[account_access].getAccountName()
	BankAccounts[account_access].getAccountNumber()
	BankAccounts[account_access].getBalance()
else :
	print ("Invalid Input")

print("To Deposit or Withdraw: ")
print("1. Deposit")
print("2. Withdraw")
choice = input("Enter choice(1/2): ")
if choice == '1':
	money = input("Please enter the amount to deposit: $")
	BankAccounts[account_access].deposit(money)
elif choice == '2':
	money = input("Please enter the amount to withdraw: $")
	BankAccounts[account_access].withdraw(money)
else:
	print("Invalid Input")
