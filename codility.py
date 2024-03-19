from datetime import datetime

def solution(A, D):
    total_income = 0
    total_card_payments = 0
    balance = 0
    
# Date for the Last Transcation
    last_date = None
    
    for amount, date_str in zip(A, D):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        
        if last_date is None or date.month != last_date.month:
# Deduct the card fee unless there were at least three card payments totaling at least 100
            if total_card_payments < 3 or total_card_payments < 100:
                balance -= 5
                
  # Reseting Card Payment for a new month
            total_card_payments = 0
        
#updating of the total income 
        if amount >= 0:
            total_income += amount
            balance += amount
        else:
            total_card_payments += 1
            balance += amount
        
#updating the Dates 
        last_date = date
    
# Deduction on card payment
    if total_card_payments < 3 or total_card_payments < 100:
        balance -= 5
    
    
    return balance

# Example 
A = [100, 100, 100, -10]
D = ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']
print(solution(A, D))  # Output: 230