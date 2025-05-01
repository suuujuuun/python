brand = 'apple'

exchangeRate = 1.232344234

message = [1,2]

message[0] = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR'%(brand,1299,exchangeRate)

message[1] = ('the price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f}'\
              ' USD to 1 EUR'.format('apple',1299,1.23234234234))

print(message[0])
print(message[1])
