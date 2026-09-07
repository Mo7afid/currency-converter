import requests
import sys
import time
# main function
def main() :
    try :
        data1,data2 = api()
    except requests.exceptions.RequestException:
        print("Connection error. Please try again.")
        sys.exit()
    while True :
        print('enter your choice number')
        print('1:View exchange rates')
        print('2:Convert currency ')
        print('3:exit')
        try :
           choice = int(input('your choice: '))
        except ValueError :
             continue
        if choice == 1 :
           print_rates(data1,data2)
           time.sleep(5)
        elif choice == 2:
               print('enter your choice number')
               print('1:from euro to mad')
               print('2:from usd to mad ')
               print('3:from mad to euro')
               print('4:from mad to usd')
               while True :
                  try :
                      choice = int(input('your choice: '))
                      break
                  except ValueError :
                      continue
               if choice == 1:
                   amount = float(input("Enter the amount of money: "))
                   result = euro_to_mad(data1,amount)
                   print(f'{amount} euro = {result} dh')
                   time.sleep(5)
               elif choice == 2:
                   amount = float(input("Enter the amount of money: "))
                   result = usd_to_mad(data2,amount)
                   print(f'{amount} usd = {result} dh')
                   time.sleep(5)
               elif choice == 3 :
                   amount = float(input("Enter the amount of money: "))
                   result = mad_to_euro(data1,amount)
                   print(f'{amount}dh = {result} euro')
                   time.sleep(5)
               elif choice == 4:
                   amount = float(input("Enter the amount of money: "))
                   result = mad_to_usd(data2,amount)
                   print(f'{amount}dh = {result} usd')
                   time.sleep(5)
        elif choice == 3 :
               break

def api() :
       params1 = {
          "base": "EUR",
          "quotes": "MAD"
            }
       params2 = {
          "base": "USD",
          "quotes": "MAD"
            }
       response_1 = requests.get(
        "https://api.frankfurter.dev/v2/rates",
         params=params1
         )
       response_2 = requests.get(
         "https://api.frankfurter.dev/v2/rates",
         params=params2
        )
       return response_1.json(), response_2.json()
       
def print_rates(data1,data2) :
    euro_mad = data1[0]['rate']
    usd_mad = data2[0]['rate']
    day = data1[0]['date']
    print(f'date:{day}')
    print(f'1 euro = {round(euro_mad,2)}dh')
    print(f'1 usd = {round(usd_mad,2)}dh')
def euro_to_mad(data1,num) :
    return round(data1[0]['rate'] * num,2)
def usd_to_mad(data2,num) :
    return round(data2[0]['rate'] * num,2)
def mad_to_euro(data1,num) :
    return round(num / data1[0]['rate'],2)
def mad_to_usd(data2,num) :
    return round(num / data2[0]['rate'],2)

main()


