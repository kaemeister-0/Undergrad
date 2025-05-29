#wholesale price of those 60 books

base_price = 24.95 
#for first copy(24.95+3)
#for rest of the copies (24.95+(0.75*59))

total_price = ((24.95+3)+(24.95+(0.75*59)))

#bookstore gets 60% off , so 0.6 is multiplicated with total_price
wholesale_price = total_price*0.6

print(wholesale_price)