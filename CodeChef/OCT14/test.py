for x in range(len(s)):
        for y in range(len(w)):
            if x==y:
                if s[x]!=w[y]:
                    
                    c += b
    if c>k:
        c = 0
        for z in range(len(s)):
            for z1 in range(len(w)):
                if z==z1:
                    if s[z]!=w[z1]:
                        #c = 0
                        c += a

            #if c>k and s[x]!=w[y] and x==y:
             #   c = 0
              #  c += a
