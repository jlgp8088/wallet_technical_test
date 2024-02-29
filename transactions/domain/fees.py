from transactions.models import FeesHistory
from decimal import Decimal

def calc_fees(object, user, amount):
  fee = user.fee_mode
  amount = Decimal(amount)
  total = 0

  trade = amount * ( fee.trade_fee_percentage / 100 )
  payment = amount * ( fee.payment_fee_percentage / 100 )
  blockchain = amount * ( fee.blockchain_fee_percentage / 100 )

  if(fee.instant_payment): 
    process_fee_trade(trade)
    process_fee_payment(payment)
    process_fee_blockchain(blockchain)
    total = amount - (payment + trade + blockchain)
  else:
    total = amount

  newFee = FeesHistory(
    payment_fee = payment,
    trade_fee = trade,
    blockchain_fee = blockchain,
    paid= fee.instant_payment,
    user=user
  )

  newFee.save()
  object.fees = newFee
  object.save()

  return total


def process_fee_trade(value):
  return True


def process_fee_payment(value):
  return True


def process_fee_blockchain(value):
  return True