def add_expense(expenses,amount,category):
    expenses.append({'amount':amount,'category':category})
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount :{expense['amount']}, Category:{expense['category']}')
def total_expenses(expenses):
    return sum(map(lambda expense:expense['amount'],expenses))
def filter_expenses_by_category(expenses,category):
    return filter(lambda expense:expense['category']==category ,expenses)
def main():
    expenses=[]
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice =input('Enter your choice: ')
        if choice =='1':
            amount=float(input('Enter amount'))
            category=input('Enter category: ')
            add_expense(expenses,amount,category)
        elif choice=='2':
            print_expenses(expenses)
        elif choice =='3':
            total_expense=total_expenses(expenses)
            print('Total expense:',total_expense)
        elif choice=='4':
            category=input('Enter category:')
            filtered_expenses=filter_expenses_by_category(expenses,filtered_expenses)
            print_expenses(filtered_expenses)
        else :
            print('Thanks for playing with me')
            break
main()