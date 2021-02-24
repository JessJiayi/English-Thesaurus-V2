import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
    )
cursor = con.cursor()
source = cursor.execute("SELECT Expression FROM Dictionary")
sources = cursor.fetchall()
expressions = []
for s in sources:
    s = str(s)
    expression = s.replace(')','')
    expression = expression.replace('(','')
    expression = expression.replace("'",'')
    expressions.append(expression.replace(',',''))

try:
    word = input("Enter a word：")
    word = word.lower()
    if word in expressions:
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %word)
        results = cursor.fetchall()
    elif len(get_close_matches(word,expressions)) > 0:
        close = (get_close_matches(word,expressions)[0])
        choice = input("Do You Mean " + close + "?/  Y/N ").upper()
        if choice == 'Y':
            query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %close)
            results = cursor.fetchall()
        elif choice == 'N':
            print('Oops! We Do Not Have This Information Yet!')
        else:
            print('Invalid Choice')
    else:
        print('Oops! We Do Not Have This Information Yet!')
    
    for result in results:
        print((result)[1])

except:
    print('Please Double Check What You Enter!')

   

    
  
