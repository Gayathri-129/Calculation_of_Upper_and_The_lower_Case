def my_fun(word):
    upper=0
    lower=0
    for i in word:
        if i.isupper():
           upper+=1
        elif i.islower():
            lower+=1
    print('No. of Upper case characters:',upper)
    print('No. of Lower case characters:',lower)

word = input("Sample String:")
my_fun(word)