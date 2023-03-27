from datetime import date

again = 1
while int(again) == 1:
    today = date.today()

    # dd/mm/YY
    d = today.strftime("%d/%m/%Y")

    entry = input("Write your entry")
    diary = d , entry

    print(str(diary))
    f = open("DiaryEntry.txt","a")
    f.write(str(diary))
    f.close

    again = input("Press 1 to enter again")
