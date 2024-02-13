"""
Find the two number in the array that sum is equal to the given number - 
For Example - 
    a = [2,3,5,1,5,2,6]
    sum = 8 then number will be the 2,6
""" 





def find_main_function(a):
    # Sort the array then take one element and use BST to 
    # find the another element then it will take time - T(n) = O(nLogn)
    pass






    



def main():
    a = [2,3,5,1,5,2,6]
    X, Y = find_main_function(a)
    print("Pair are {} and {}".format(X,Y))

if __name__ == '__main__':
    main()