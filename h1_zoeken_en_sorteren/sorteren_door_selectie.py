def selection_sort_vooraan(a):
   
    n = len(a)
    
    for i in range(n - 1):
        index_klein = i
        
        for j in range(i + 1, n):
            if a[j] < a[index_klein]:
                j = index_klein
            
        a[i], a[index_klein] = a[index_klein], a[i]
   
   
   
   
   

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    selection_sort_vooraan(a)

