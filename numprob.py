num = 1200
num_string = str(num) #conv num to string 1200
length = len(num_string) #length of num
num_list = [int(i) for i in num_string] #converting the num_string to an integer 
num_reverse = num_string[::-1] #reversing the num_string 0021
num_reverse_int = len(str(int(num_reverse))) #converting num_reverse to int --> 21 --> again to str (21) --> so length = 2
length -= num_reverse_int # 4 - 2
print(length) # 2
