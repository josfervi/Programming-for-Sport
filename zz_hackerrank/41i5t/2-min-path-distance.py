def answer(rows):
    
    nr = len(rows)
    for r in range(nr):
        nc = len(rows[r])
        for c in range(nc):
            
            if r == 0:
                # no parents
                continue
            
            if c == 0:
                # no left parent
                right_paren = rows[r-1][c]
                me = rows[r][c]
                rows[r][c] += right_paren + me
                continue
            
            if c == nc - 1:
                # no right parent
                left_paren = rows[r-1][c-1]
                me = rows[r][c]
                rows[r][c] = left_paren + me
                continue
            
            left_paren = rows[r-1][c-1]
            right_paren = rows[r-1][c]            
            me = rows[r][c]
            rows[r][c] = min(left_paren, right_paren) + me
    
    return min(rows[-1])

rows = [[1], [1,2], [1,2,3], [1,2,3,4]]
print answer(rows)