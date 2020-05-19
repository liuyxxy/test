def square(x):
    return x * x

def main(): 
    for i in range(10):
        print(f"{i} squared is now {square(i)}")

#special syntax
if __name__ == "__main__":
    main()