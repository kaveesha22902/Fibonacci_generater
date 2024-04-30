def fibonacci_generater(length):
    a,b = 0,1
    
    for _ in range(length):
        yield a
        a,b = b, a+b
        
        
def main():
    try:
        length = int(input("Enter the length of fibonacci sequnce : "))
        
        if length <= 0:
            print("length is not valid , try again..")
            return
        
        fibonacci_sequnce = list(fibonacci_generater(length))
        print("fibnacci_sequnce length", length,"is",fibonacci_sequnce)
        
    except ValueError:
        print("Invalid input..")
        
if __name__ =="__main__":
    main()
