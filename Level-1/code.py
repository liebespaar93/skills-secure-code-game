'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple



Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0
    integer = 0
    floater = 1.0
    
    for item in order.items:
        if item.type == 'payment':
            net += item.amount
            floater += int(item.amount) - (item.amount)
            integer += int(item.amount)
        elif item.type == 'product':
            net -= item.amount * item.quantity
            floater -= int(item.amount * item.quantity) - (item.amount * item.quantity)
            integer -= int(item.amount * item.quantity)
        else:
            return("Invalid item type: %s" % item.type)
        
        if floater > 2.0:
            integer += 1
            floater -= 1
        elif floater < 0.0:
            integer -= 1
            floater += 1
        # print(format(int(net), '#16x'))
        # print(integer, floater)
    if integer == 0 and abs(floater - 1) < 1e-15:
        return("Order ID: %s - Full payment received!" % order.id)
    else:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, integer + floater - 1))


# import unittest
# import code as c

# def main():
#     small_item = c.Item(type='product', description='accessory', amount=3.3, quantity=1)
#     payment_1 = c.Item(type='payment', description='invoice_5_1', amount=1.1, quantity=1)
#     payment_2 = c.Item(type='payment', description='invoice_5_2', amount=2.2, quantity=1)
#     order_5 = c.Order(id='5', items=[small_item, payment_1, payment_2])
#     print(c.validorder(order_5))
#     return 0


# def main():
#     tv = c.Item(type='product', description='tv', amount=1000.00, quantity=1)
#     payment = c.Item(type='payment', description='invoice_4', amount=1e19, quantity=1)
#     reimbursement = c.Item(type='payment', description='reimbursement_4', amount=-1e19, quantity=1)
#     order_4 = c.Order(id='4', items=[payment, tv, reimbursement])
#     print(c.validorder(order_4))
#     return 0


if __name__ == '__main__':
    main()



