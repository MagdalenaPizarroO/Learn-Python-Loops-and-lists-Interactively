names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
names[1] = 'Steven'
names[-1] = 'Pepe'
names[0] = names[2]+names[4]

for i in range(len(names) - 1, -1 , -1):
    print(names[i])

#esto también sirve pero no pasa el test:
# i = len(names) - 1

# while i >= 0:
#     print(names[i])
#     i -= 1