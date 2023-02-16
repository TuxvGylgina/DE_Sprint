
s = input()
stack = []
skobka = True

for i in s:
    if i in '([{':
       stack.append(i)
    elif i in ')]}':

        if not stack:
            skobka = False
            break

        open_skobka = stack.pop()

        if open_skobka == '(' and i ==')':
            continue
        if open_skobka == '[' and i ==']':
            continue
        if open_skobka == '{' and i =='}':
            continue

        skobka = False
        break

if skobka and len(stack)==0:
    print('Yes')
else:
    print('No')
