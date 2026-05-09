from datetime import date

# Creating a birthday object (Year, Month, Day)
birthday = date(1995, 9, 20)

print(f"Stored Birthday: {birthday}")
print(f"Year: {birthday.year}, Month: {birthday.month}, Day: {birthday.day}")

from datetime import datetime

date_string = "20/02/2002"
# Use format codes: %d (day), %m (month), %Y (4-digit year)
bday_object = datetime.strptime(date_string, "%d/%m/%Y").date()

print(f"Converted Object: {bday_object}")

birthdays = {
    "Alice": date(1990, 5, 12),
    "Bob": date(1985, 11, 30)
}
print(f"Alice's Birthday: {birthdays['Alice']}")
print(f"Bob's Birthday: {birthdays['Bob']}")