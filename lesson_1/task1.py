# print name surname
print("Siranush Aslanyan")

#print current year - your age



import datetime
today = datetime.date.today()
current_date = today.strftime("%d/%m/%Y")

from datetime import datetime

my_birth_date = datetime.strptime("28/12/1994", "%d/%m/%Y")
current_date_formatted = datetime.strptime(current_date, "%d/%m/%Y")

# vor tariqs ei grum, 95 tiv er cuyc talis, esel vor tariqs 29 chgrem senc areci :P
delta = (current_date_formatted.year - my_birth_date.year)

# klini tariqi masin el tnayin chlini?

print(current_date_formatted.year - delta)

# anun tariq

full_name = "Siranush Aslanyan"
age = 28
print(full_name, age)

# data typer

text = "string, boolean, integer (es erevi numberna), en amboxj tvov numbery (et chgitem arandzin tipa te che), " \
       "bayc vorpes etpisin typer-ic ches xosacel arandzin ynker Stepanyan, popoxakan haytararelnel ban ches grum miangamic " \
       "grum es x = 'lalal'"
# chem haskanum es pythonum ket storaket chka?

print(text)

# 7rd tnayin

x = 16
y = 5

z = x // y == 3
print(z, type(z))

# 8 y chem anelu, imast chem tesnum