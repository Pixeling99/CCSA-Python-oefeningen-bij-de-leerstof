def zoek_binair(zoekItem,rij):
    l = 0;
    r = len(rij) - 1;
    
    while l <= r:
        m = (l + r) // 2;
        print("l = ", l, "r = ", r, "m = ", m, "rij[m] = ", rij[m])
        
        if rij[m] == zoekItem:
            print("Gevonden op index ", m)
            return m
        
        if rij[m] < zoekItem:
            l = m + 1
        
        elif rij[m] > zoekItem:
            r = m - 1
        
        else:
            m = -1
        
        

index = zoek_binair(70, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"index = {index}")
