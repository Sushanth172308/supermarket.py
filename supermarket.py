from datetime import datetime

name = input('Enter your name:')
# LISTS of items
lists = '''
Rice    Rs 25/Kg
sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Pannier  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Colgate Rs 85/each
'''
#Declaration
price = 0
pricelist=[]
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {'Rice': 25, 'Sugar': 30, 'Salt': 20, 'Oil': 80,
         'Pannier': 120, 'Maggi': 50, 'Boost': 90, 'Colgate': 85}
option = int(input('For list of items press 1:'))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input('if you want to buy press 1 or 2 to exit:'))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input('Enter your items:')
        quantity = int(input('Enter quantity:'))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item, quantity, items, price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice*5)/100
            finalamout = gst + totalprice
        else:
            print('Sorry, Entered item is not available')
    else:
        print('You entered wrong number')

    inp = input('Can i bill the items Yes/NO:')
    if inp =='Yes':
        pass
        if finalamout != 0:
            print(25*'=', 'Vic supermarket', 25*'=')
            print(28*'', 'Dam Square')
            print('Name:' ,name, 30*'', 'Date:', datetime.now())
            print(72*'-')
            print('sno', 8*'', 'items', 8*'', 'Quantity', 3*'', 'price')
            for i in range(len(pricelist)):
                print(i, 8*'', 5*'', ilist[i], 3*'', qlist[i], 8*'', plist[i])
            print(75*'-')
            print(50*'', 'TotalAmount:', 'Rs', totalprice)
            print('gst amount', 40*'', 'Rs', gst)
            print(75*'-')
            print(50*'', 'FinalAmount:', 'Rs', finalamout)
            print(75*'-')
            print(20*'', 'Thanks for visiting us')
            print(75*'-')






