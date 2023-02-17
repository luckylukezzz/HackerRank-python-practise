#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()
    
    x=[]
    for i in range(5):
        x.append(False)
    for i in s:
        if x[0]!=True:
            x[0] =i.isalnum() #check if it has alphanumeric characters.
        if x[1]!=True:
            x[1]= i.isalpha() #any alphabetical characters
        if x[2] !=True :
            x[2]=i.isdigit() #any digits
        if x[3]!=True:
            x[3]=i.islower() #any lowercase characters.
        if x[4]!=True:
            x[4]=i.isupper() #any uppercase characters

    for i in x:
        print(i)
