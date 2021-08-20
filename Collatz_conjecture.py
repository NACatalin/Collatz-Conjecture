import matplotlib.pyplot as plt
x=input('Enter your number:')
number=int(eval(x))
count=0
number_gen=list()

while number!=1:

    if number % 2 == 0:
        number = int(number / 2)
        number_gen.append(number)
    elif number % 2 != 0:
        number = int(3 * number + 1)
        number_gen.append(number)


    count=count+1

x_points=list(range(count))
print('Step number:',count)
try:
    print('Maximum  value:',max(number_gen))
except:
    print('Maximum value: 1')
fig, ax = plt.subplots()
ax.plot(x_points,number_gen,marker='o', color='black')
ax.grid()
ax.minorticks_on()
ax.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.3)
ax.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()

