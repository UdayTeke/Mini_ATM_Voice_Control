class ZeroBalanceError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return(repr(self.value))
def amt_error():
    try:
        amount=int(input('Enter amount to withdraw'))
        if amount<500:
            raise(ZeroBalanceError(amount))
        else:
            pass
    except ZeroBalanceError as error:
        print("Please! Keep minimum Rs.500 balance",error.value)
