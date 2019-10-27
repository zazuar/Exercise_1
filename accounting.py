
def orders_log(path):
    orders_log = open(path)

    for line in orders_log:
        line = line.rstrip()
        words = line.split('|')

        melon= 1.00
        delivery_id = words[0]
        name = words[1]
        expected = words[2]
        paid = words[3]
        
        
        expected2 = float(expected)
        expected3 = format(expected2,'.2f')

        
        if paid != expected3:
            print(f"{name} paid {paid} expected {expected3}")


    orders_log.close()

    
orders_log('customer-orders.txt')

