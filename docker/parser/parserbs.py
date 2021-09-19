from bs4 import BeautifulSoup
import requests
from requests import Request, Session
import pandas as pd

def data_updater():
    data = pd.read_excel('НКО_благонадежность_tilda5408099.xlsx') #Сюда сслылка на таблицу с НКО
    data['Маил Добро'] = ''
    data['Маил Добро ссылка'] = ''
    data['Ссылка на сайт'] = ''
    data['Нужна помощь'] = ''
    data['Нужна помощь Описание'] = ''
    data['Нужна помощь Ссылка'] = ''
    data['Нужна помощь Фонд'] = 0
    for j in range(data.shape[0]):
        po = data['Наименование'][j]
        if '"' in po:
            po = po.split('"')[1]
            po = po.replace('"', '')
            try:
                po = po.split('«')[1]
                po = po.replace('«', '')
                po = po.replace('»', '')
            except:
                ...
        poisk = po
        print(poisk)
        po = po.replace(' ', '+')
        urls = f'https://dobro.mail.ru/funds/search/?query={po}&recipient=all&city=any'
        response = requests.get(urls)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_='cols__column cols__column_small_percent-100 cols__column_medium_percent-50 cols__column_large_percent-50')
        print('===========================https://dobro.mail.ru/funds===========================')
        if len(quotes) != 0:
            for i in range(len(quotes)):
                name = str(quotes[i].find('span', 'link__text'))
                name = name.replace('<span class="link__text">', '')
                name = name.replace('</span>', '')

                url = str(quotes[i].find('a', 'link link_font_large margin_bottom_10 link-holder'))
                url = url.replace('<a class="link link_font_large margin_bottom_10 link-holder" href="', 'https://dobro.mail.ru')
                url = url.split('"')[0]

                city = str(quotes[i].find('div', 'p-fund__city margin_bottom_5'))
                city = city.replace('<div class="p-fund__city margin_bottom_5">', '')
                city = city.replace('</div>', '')

                responses = requests.get(url)
                soups = BeautifulSoup(responses.text, 'lxml')

                site = soups.find_all('div', class_='p-fund-detail__info-row')
                try:
                    if str(site[0].find('a', 'link')) == None:
                        site = str(site[0].find('a', 'link'))
                        site = site.replace('<span class="link__text">', '')
                        site = site.replace('</span>', '')
                    else:
                        try:
                            site = str(site[1].find('a', 'link'))
                            site = site.replace('<span class="link__text">', '')
                            site = site.split('"')[3]
                        except:
                            site = 'Нет'
                except:
                    site = 'Нет'
                        
                data['Маил Добро'][j] = name
                data['Маил Добро ссылка'][j] = url
                data['Ссылка на сайт'][j] = site
                

                print(name + '\n' + city + '\n' + url + '\n' + site + '\n')
        else:
            print('Нет')


        url = 'https://nuzhnapomosh.ru/wp-content/plugins/nuzhnapomosh/funds.php'
        typ = 'POST'
        req = Request(typ, url, files = {'np_name': (None, poisk)}).prepare()
        s = Session()
        respo = s.send(req)
        respo.text
        soup2 = BeautifulSoup(respo.text, 'lxml')
        quotes2 = soup2.find_all('div', class_='np-card__inner')
        print('===========================https://nuzhnapomosh.ru/===========================')
        if len(quotes2) != 0:
            for i in range(len(quotes2)):
                name = str(quotes2[i].find('h4', 'np-card__title'))
                name = name.replace('<h4 class="np-card__title">', '')
                name = name.replace('</h4>', '')

                descr = str(quotes2[i].find('p', 'np-card__descr'))
                descr = descr.replace('<p class="np-card__descr">', '')
                descr = descr.replace('</p>', '')

                money = str(quotes2[i].find('li', 'np-card__row'))
                money = money.split('<span>')[1]
                money = money.replace('</li>', '')
                money = money.replace(' ₽</span>', '')
                money = money.replace('\n', '')
                money = money.replace(' ', '')

                site = str(quotes2[i].find('a', 'np-card__link'))
                site = site.replace('<a class="np-card__link" href="', '')
                site = site.split('"')[0]
                
                data['Нужна помощь'][j] = name
                data['Нужна помощь Описание'][j] = descr
                data['Нужна помощь Ссылка'][j] = float(money)
                data['Нужна помощь Фонд'][j] = 'https://nuzhnapomosh.ru' + site

                print(name + '\n' + descr + '\n' + 'Деньги в фонде: ' + money + ' Рублей' + '\n' + 'https://nuzhnapomosh.ru' + site + '\n')
        else:
            print('Нет')
        print('\n'+'============================' + str(j) + '======================================'+'\n')


def get_info(NKO_T):
    data = {'Маил Добро': '', 'Маил Добро ссылка': '', 'Ссылка на сайт': '', 'Нужна помощь': '', 'Нужна помощь Описание': '', 'Нужна помощь Ссылка': '', 'Нужна помощь Фонд': 0}
    po = NKO_T
    if '"' in po:
        po = po.split('"')[1]
        po = po.replace('"', '')
        try:
            po = po.split('«')[1]
            po = po.replace('«', '')
            po = po.replace('»', '')
        except:
            ...
    poisk = po
    print(poisk)
    po = po.replace(' ', '+')
    urls = f'https://dobro.mail.ru/funds/search/?query={po}&recipient=all&city=any'
    response = requests.get(urls)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='cols__column cols__column_small_percent-100 cols__column_medium_percent-50 cols__column_large_percent-50')
    print('===========================https://dobro.mail.ru/funds===========================')
    if len(quotes) != 0:
        for i in range(len(quotes)):
            name = str(quotes[i].find('span', 'link__text'))
            name = name.replace('<span class="link__text">', '')
            name = name.replace('</span>', '')

            url = str(quotes[i].find('a', 'link link_font_large margin_bottom_10 link-holder'))
            url = url.replace('<a class="link link_font_large margin_bottom_10 link-holder" href="', 'https://dobro.mail.ru')
            url = url.split('"')[0]

            city = str(quotes[i].find('div', 'p-fund__city margin_bottom_5'))
            city = city.replace('<div class="p-fund__city margin_bottom_5">', '')
            city = city.replace('</div>', '')

            responses = requests.get(url)
            soups = BeautifulSoup(responses.text, 'lxml')

            site = soups.find_all('div', class_='p-fund-detail__info-row')
            try:
                if str(site[0].find('a', 'link')) == None:
                    site = str(site[0].find('a', 'link'))
                    site = site.replace('<span class="link__text">', '')
                    site = site.replace('</span>', '')
                else:
                    try:
                        site = str(site[1].find('a', 'link'))
                        site = site.replace('<span class="link__text">', '')
                        site = site.split('"')[3]
                    except:
                        site = 'Нет'
            except:
                site = 'Нет'
                    
            data['Маил Добро'] = name
            data['Маил Добро ссылка'] = url
            data['Ссылка на сайт'] = site
            

            print(name + '\n' + city + '\n' + url + '\n' + site + '\n')
    else:
        print('Нет')

    url = 'https://nuzhnapomosh.ru/wp-content/plugins/nuzhnapomosh/funds.php'
    typ = 'POST'
    req = Request(typ, url, files = {'np_name': (None, poisk)}).prepare()
    s = Session()
    respo = s.send(req)
    respo.text
    soup2 = BeautifulSoup(respo.text, 'lxml')
    quotes2 = soup2.find_all('div', class_='np-card__inner')
    print('===========================https://nuzhnapomosh.ru/===========================')
    if len(quotes2) != 0:
        for i in range(len(quotes2)):
            name = str(quotes2[i].find('h4', 'np-card__title'))
            name = name.replace('<h4 class="np-card__title">', '')
            name = name.replace('</h4>', '')

            descr = str(quotes2[i].find('p', 'np-card__descr'))
            descr = descr.replace('<p class="np-card__descr">', '')
            descr = descr.replace('</p>', '')

            money = str(quotes2[i].find('li', 'np-card__row'))
            money = money.split('<span>')[1]
            money = money.replace('</li>', '')
            money = money.replace(' ₽</span>', '')
            money = money.replace('\n', '')
            money = money.replace(' ', '')

            site = str(quotes2[i].find('a', 'np-card__link'))
            site = site.replace('<a class="np-card__link" href="', '')
            site = site.split('"')[0]
            
            data['Нужна помощь'] = name
            data['Нужна помощь Описание'] = descr
            data['Нужна помощь Ссылка'] = float(money)
            data['Нужна помощь Фонд'] = 'https://nuzhnapomosh.ru' + site

            print(name + '\n' + descr + '\n' + 'Деньги в фонде: ' + money + ' Рублей' + '\n' + 'https://nuzhnapomosh.ru' + site + '\n')
    else:
        print('Нет')
    return data
