def isValid(s: str) -> bool:
    
    stack = []  # 括弧を格納するスタック
    
    # 閉じ括弧に対応する開き括弧のマップ
    bracket_map = {
        ')': '(',   #key : value
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in bracket_map.values():  # 開き括弧の場合
            stack.append(char)

        elif char in bracket_map.keys():  # 閉じ括弧の場合

            if not stack or stack[-1] != bracket_map[char]: # スタックが空、または対応する開き括弧がない

                return False
            
            stack.pop()  # 対応する開き括弧をスタックから取り除く

      

    return not stack  # スタックが空であればTrue、そうでなければFalse


s = '()' 
print(isValid(s)) # True 

s = "({)}" 
print(isValid(s)) # false 
