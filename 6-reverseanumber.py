Number = int(input("Enter Number:"))
rev = 0
while(Number > 0):
    Reminder = Number %10
    rev = (rev *10) + Reminder
    Number = Number //10
print("\n rev of entered number is = %d" %rev)
