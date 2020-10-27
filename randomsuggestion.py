import random

city = input('台北指南按1，台中指南按2: ')
awards = input('星級餐廳推薦按1，必比登或餐盤推薦等級按2: ')

suggestionPool1 = []
if city == '1':
    for i in result:
        if i.get('Location') == '台北':
            suggestionPool1.append(i)
else:
    for i in result:
        if i.get('Location') == '台中':
            suggestionPool1.append(i)
suggestionPool2 = []
if awards == '1':
    for i in suggestionPool1:
        if i.get('Awards') == '米其林一星' or i.get('Awards') == '米其林二星' or i.get('Awards') == '米其林三星':
            suggestionPool2.append(i)
else:
    for i in suggestionPool1:
        if i.get('Awards') == '必比登推薦' or i.get('Awards') == '餐盤推薦':
            suggestionPool2.append(i)

a = random.randint(0,(len(suggestionPool2)-1))
print('\n\n******{}******\n餐廳名稱: {} ({})\n\n{}\n\n地址: {}'.format(
    suggestionPool2[a].get('Awards'),
    suggestionPool2[a].get('Name'),
    suggestionPool2[a].get('Type'),
    suggestionPool2[a].get('Comment'),
    suggestionPool2[a].get('Address')
))
