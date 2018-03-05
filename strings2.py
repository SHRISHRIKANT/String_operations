print("I bought %d Euro worth of %s!" %(200, 'cookies'))
print("I bought {0} Euro worth of {1}!".format(200,'cookies')) #Accessing values by position
print('{:#<10}'.format('Cake')) #Left aligment for word 'Cake' according to right alignment, gaps filled with '#'
print('{:#^10}'.format('Cake')) #Centre aligment for word 'Cake' according to right alignment, gaps filled with '#'
print('{:#>10}'.format('Cake'))

for num in range(1,10):
        print('{0:{width}}'.format(num, width=5), end=' ')
