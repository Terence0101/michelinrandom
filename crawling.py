import requests
from pyquery import PyQuery as pq

result = []

for i in range (1,13):
    print('Loading...')
    res = requests.get('https://guide.michelin.com/tw/zh_TW/restaurants/page/{}'.format(i))
    content = pq(res.text)
    content.make_links_absolute(base_url=res.url)    
    for info in content('.js-restaurant__list_items > div.col-lg-6:nth-child(n)').items():
        infoDict = {}
        
        infoDict['Name'] = info('h5').text()
        infoDict['Type'] = info('div.card__menu-footer--price.pl-text').text()
        
        if info('div.card__menu-footer--location.flex-fill.pl-text').text() == 'Taipei':
            infoDict['Location'] = '台北'
        else:
            infoDict['Location'] = '台中'
        
        Awards = info('div.card__menu-content.js-match-height-content > div').text()
        if Awards[0] == 'o':
            infoDict['Awards'] = '米其林三星'
        elif Awards[0] == 'n':
            infoDict['Awards'] = '米其林二星'
        elif Awards[0] == 'm':
            infoDict['Awards'] = '米其林一星'
        elif Awards[0] == '=':
            infoDict['Awards'] = '必比登推薦'
        else:
            infoDict['Awards'] = '餐盤推薦'

        eachDetail = info('div.card__menu-content.js-match-height-content > h5 > a').attr('href')
        eachInfo = pq(eachDetail)
        infoDict['Address'] = eachInfo('div.restaurant-details__heading.d-none.d-lg-block         > ul > li:nth-child(1)').text()
        infoDict['Comment'] = eachInfo('.js-show-description > div').text()
        infoDict['priceRange'] = ((eachInfo('li.restaurant-details__heading-price').text()).split(' TWD'))[0]
        result.append(infoDict)
    print(res.url)
