def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
        # print("I am always executed")


x = func1()
print(x)
# te print ko statement nai chalato jawa function return karales tikawaaste hame finally clause 
# ko use karsan
#agar konsa bhi ek topic mein hame return galya te function tach khatm hos aglyang nai jato 
