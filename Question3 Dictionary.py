def even_to_odd_sum(numbers):
    even_sum = sum(numb for numb in numbers if numb % 2 == 0)
    odd_sum =  sum (numb for numb in numbers if numb % 2 != 0)
    return (even_sum,odd_sum)
numbers = [1,2,3,4,5,6,7] 
result = even_to_odd_sum(numbers)    
print(result)
        
    
    
