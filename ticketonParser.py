import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def get_films():
    try:
        cookies = {
            '_ym_uid': '1694439152375035746',
            '_ym_d': '1694439152',
            '_gcl_au': '1.1.1472638931.1704255366',
            '_gid': 'GA1.2.1415576106.1704255367',
            'sc': '3E576D12-E373-A45F-1AD5-EF9E1E89A8A0',
            '_ym_isad': '1',
            '_tt_enable_cookie': '1',
            '_ttp': 'BnrR0tpeGMzkwcPAYwUhZjmf9gw',
            '_ym_visorc': 'b',
            'supportOnlineTalkID': 'AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt',
            '_ga_MJKVR7DKT0': 'GS1.2.1704255368.1.1.1704255390.38.0.0',
            'PHPSESSID': 'nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70',
            '_ga': 'GA1.3.145911633.1704255367',
            '_gid': 'GA1.3.1415576106.1704255367',
            '_dc_gtm_UA-29592875-1': '1',
            '_dc_gtm_UA-29592875-8': '1',
            '_ga': 'GA1.2.145911633.1704255367',
            '_ga_MJKVR7DKT0': 'GS1.3.1704255368.1.1.1704255709.52.0.0',
            '_ga_61RK6KN747': 'GS1.2.1704255368.1.1.1704255709.53.0.0',
            '_ga_78C77YB2FT': 'GS1.1.1704255367.1.1.1704255714.47.0.0',
        }

        headers = {
            'authority': 'm.ticketon.kz',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
            'cache-control': 'max-age=0',
            # 'cookie': '_ym_uid=1694439152375035746; _ym_d=1694439152; _gcl_au=1.1.1472638931.1704255366; _gid=GA1.2.1415576106.1704255367; sc=3E576D12-E373-A45F-1AD5-EF9E1E89A8A0; _ym_isad=1; _tt_enable_cookie=1; _ttp=BnrR0tpeGMzkwcPAYwUhZjmf9gw; _ym_visorc=b; supportOnlineTalkID=AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt; _ga_MJKVR7DKT0=GS1.2.1704255368.1.1.1704255390.38.0.0; PHPSESSID=nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70; _ga=GA1.3.145911633.1704255367; _gid=GA1.3.1415576106.1704255367; _dc_gtm_UA-29592875-1=1; _dc_gtm_UA-29592875-8=1; _ga=GA1.2.145911633.1704255367; _ga_MJKVR7DKT0=GS1.3.1704255368.1.1.1704255709.52.0.0; _ga_61RK6KN747=GS1.2.1704255368.1.1.1704255709.53.0.0; _ga_78C77YB2FT=GS1.1.1704255367.1.1.1704255714.47.0.0',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        }

        response = requests.get('https://m.ticketon.kz/astana/cinema', cookies=cookies, headers=headers)

        src = response.text
        soup = BeautifulSoup(src, 'html.parser')

        titles_date = soup.find_all('span', class_='b-list__item-grid__info-date')
        links1 = soup.find_all('a', class_='popular')
        links2 = soup.find_all('a', class_='recommended')
        links3 = soup.find('br').find_next_sibling().find_all('a', class_='')
        



        titles = []
        dates = []
        all_links = []

        for i in range(1, len(titles_date), 2):
            titles.append(titles_date[i].text)
            # print(titles_date[i].text)
            dates.append(titles_date[i-1].text)

        for i in range(len(links1)):
            all_links.append('https://m.ticketon.kz' + links1[i].get('href'))

        for i in range(len(links2)):
            all_links.append('https://m.ticketon.kz' + links2[i].get('href'))

        for i in range(len(links3)):
            all_links.append('https://m.ticketon.kz' + links3[i].get('href'))

        # def get_cinema_list(all_links):
        cookies_cinema = {
            '_ym_uid': '1694439152375035746',
            '_ym_d': '1694439152',
            '_gcl_au': '1.1.1472638931.1704255366',
            '_gid': 'GA1.2.1415576106.1704255367',
            'sc': '3E576D12-E373-A45F-1AD5-EF9E1E89A8A0',
            '_ym_isad': '1',
            '_tt_enable_cookie': '1',
            '_ttp': 'BnrR0tpeGMzkwcPAYwUhZjmf9gw',
            'supportOnlineTalkID': 'AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt',
            'PHPSESSID': 'nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70',
            '_ga': 'GA1.3.145911633.1704255367',
            '_gid': 'GA1.3.1415576106.1704255367',
            'dsq__': '3toevj325138ra',
            '_ga_61RK6KN747': 'GS1.3.1704271441.2.1.1704271498.3.0.0',
            '_ga_MJKVR7DKT0': 'GS1.2.1704276640.3.0.1704276640.60.0.0',
            '_ym_visorc': 'b',
            'XSRF-TOKEN': 'eyJpdiI6InRxUUJ6QTIrZUsvV0twdkUwSjVzV1E9PSIsInZhbHVlIjoiMTlNN2ZNS29aMURkTWE2R0pwUWM3emJPZGs0VThQMk91ZUdBdlJjMXN2c1ZCQUdkZ0xQR1kvcGYrWjlKa0xoTTJxYndaNExNUmZQNjNSZ3Y5S282SnZGUUJpaTJXRHdxSnNxUkE2T2RrczVKZzNoNWRCU2dhcWlEOG9xRXpCaU4iLCJtYWMiOiIwMWRkYmIzNDE1MDY1Zjc1N2I1NTE3YjBjNTNhN2U2N2E3M2I4MjYzNTUyZTg5ZmUzOGNhOWYwYmZmODlmNTQ1IiwidGFnIjoiIn0%3D',
            'front_content_main_session': 'eyJpdiI6IklUTFltNm9lOWZ5RnFTT3VPaE5TWVE9PSIsInZhbHVlIjoiTktlZVBCM1U2UlIwZDVOT0NZVjhFQ0c1eHhrai9Hd0hQL3IvZHBweE1YUkJKdDhoWE4raXl3cktOKzRWWXZleWc5Tzg4aVlnbng4anJsdHZyUEswNFpNV2VoTGl0VWdLY0dtemlSQVZZUmR5eDR2cVBVR0JNdEdtUEpvdk9FYVUiLCJtYWMiOiJkYjNlMGZhNjJhNTFlNGIxNWRhMzAwYzMxZjQ5YjBlMmIwZTZhODI2ZjliOWNiYjMyYjM3NzMxZjhlZmQ3ZmViIiwidGFnIjoiIn0%3D',
            '_ga_78C77YB2FT': 'GS1.1.1704283107.5.1.1704283137.30.0.0',
            '_ga': 'GA1.2.145911633.1704255367',
            '_ga_MJKVR7DKT0': 'GS1.3.1704283110.5.1.1704283138.32.0.0',
            '_ga_61RK6KN747': 'GS1.2.1704271441.2.1.1704283138.32.0.0',
        }

        headers_cinema = {
            'authority': 'm.ticketon.kz',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
            'cache-control': 'max-age=0',
            # 'cookie': '_ym_uid=1694439152375035746; _ym_d=1694439152; _gcl_au=1.1.1472638931.1704255366; _gid=GA1.2.1415576106.1704255367; sc=3E576D12-E373-A45F-1AD5-EF9E1E89A8A0; _ym_isad=1; _tt_enable_cookie=1; _ttp=BnrR0tpeGMzkwcPAYwUhZjmf9gw; supportOnlineTalkID=AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt; PHPSESSID=nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70; _ga=GA1.3.145911633.1704255367; _gid=GA1.3.1415576106.1704255367; dsq__=3toevj325138ra; _ga_61RK6KN747=GS1.3.1704271441.2.1.1704271498.3.0.0; _ga_MJKVR7DKT0=GS1.2.1704276640.3.0.1704276640.60.0.0; _ym_visorc=b; XSRF-TOKEN=eyJpdiI6InRxUUJ6QTIrZUsvV0twdkUwSjVzV1E9PSIsInZhbHVlIjoiMTlNN2ZNS29aMURkTWE2R0pwUWM3emJPZGs0VThQMk91ZUdBdlJjMXN2c1ZCQUdkZ0xQR1kvcGYrWjlKa0xoTTJxYndaNExNUmZQNjNSZ3Y5S282SnZGUUJpaTJXRHdxSnNxUkE2T2RrczVKZzNoNWRCU2dhcWlEOG9xRXpCaU4iLCJtYWMiOiIwMWRkYmIzNDE1MDY1Zjc1N2I1NTE3YjBjNTNhN2U2N2E3M2I4MjYzNTUyZTg5ZmUzOGNhOWYwYmZmODlmNTQ1IiwidGFnIjoiIn0%3D; front_content_main_session=eyJpdiI6IklUTFltNm9lOWZ5RnFTT3VPaE5TWVE9PSIsInZhbHVlIjoiTktlZVBCM1U2UlIwZDVOT0NZVjhFQ0c1eHhrai9Hd0hQL3IvZHBweE1YUkJKdDhoWE4raXl3cktOKzRWWXZleWc5Tzg4aVlnbng4anJsdHZyUEswNFpNV2VoTGl0VWdLY0dtemlSQVZZUmR5eDR2cVBVR0JNdEdtUEpvdk9FYVUiLCJtYWMiOiJkYjNlMGZhNjJhNTFlNGIxNWRhMzAwYzMxZjQ5YjBlMmIwZTZhODI2ZjliOWNiYjMyYjM3NzMxZjhlZmQ3ZmViIiwidGFnIjoiIn0%3D; _ga_78C77YB2FT=GS1.1.1704283107.5.1.1704283137.30.0.0; _ga=GA1.2.145911633.1704255367; _ga_MJKVR7DKT0=GS1.3.1704283110.5.1.1704283138.32.0.0; _ga_61RK6KN747=GS1.2.1704271441.2.1.1704283138.32.0.0',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        }

        

        for i in range(len(titles)):
            print(f'{i+1}. {titles[i]}')

        linker = int(input('Which film: '))
        if 'nothing' in str(linker):
            exit(1)
        

        response_cinema = requests.get(all_links[linker-1], cookies=cookies_cinema, headers=headers_cinema)

        soup_cinema = BeautifulSoup(response_cinema.text, 'html.parser')
        cinema = soup_cinema.find_all('h3', class_='header_3')
        times = soup_cinema.find_all('td', {'style': 'font-size: 20px'})
        
        khan = False
        mega = False

        for c in cinema:
            
            if 'Chaplin Khan Shatyr Астана (Нур-Султан)' in c.text:
                khan = True
            elif 'Chaplin Mega Silk Way (Астана)' in c.text:
                mega = True
        if mega:
            time_mega = soup_cinema.find('a', string='Chaplin Mega Silk Way (Астана)').find_parent().find_parent().find_all('time')
            tickets = soup_cinema.find('a', string='Chaplin Mega Silk Way (Астана)').find_parent().find_parent().find_all('a', class_='b-button_buy-small')

            cookies_mega = {
                '_ym_uid': '1694439152375035746',
                '_ym_d': '1694439152',
                '_gcl_au': '1.1.1472638931.1704255366',
                '_gid': 'GA1.2.1415576106.1704255367',
                'sc': '3E576D12-E373-A45F-1AD5-EF9E1E89A8A0',
                '_ym_isad': '1',
                '_tt_enable_cookie': '1',
                '_ttp': 'BnrR0tpeGMzkwcPAYwUhZjmf9gw',
                'supportOnlineTalkID': 'AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt',
                'PHPSESSID': 'nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70',
                '_ga': 'GA1.3.145911633.1704255367',
                '_gid': 'GA1.3.1415576106.1704255367',
                'dsq__': '3toevj325138ra',
                '_ga_MJKVR7DKT0': 'GS1.2.1704276640.3.0.1704276640.60.0.0',
                '_ga_61RK6KN747': 'GS1.3.1704271441.2.1.1704285060.60.0.0',
                '_ym_visorc': 'b',
                '_dc_gtm_UA-29592875-8': '1',
                'XSRF-TOKEN': 'eyJpdiI6IncxOHh0b29nV3NGSDU4eVFKQWVZQlE9PSIsInZhbHVlIjoiSUFVYjQxYXVxSytzb3lFOER0NzVzL1Z2WjZVQlN6czdRT2JQZFJtTytXVkorU0FsT2U0emxlK1FJV0JrNExBSUhsbGlKelBmNGhjVXZkMzljWVNEN1pyVk9ualk2NjhXZlZLU3UrdkZJUmE3UTNyWXhVeFpIRnhpWkhUQktKZUQiLCJtYWMiOiI5NDcyMGExODU3ODNkNGY5NTE2ZTc0ZjE2ZDhmN2QwZDRkMDI5YmU5MGRjNGI0NWI3MmRhOTM3N2U2Y2I2MjA2IiwidGFnIjoiIn0%3D',
                'front_content_main_session': 'eyJpdiI6ImNJbDBycFpZdEw3UDJPVDJHTUxRWHc9PSIsInZhbHVlIjoiUTFJTnFwU2VlRkFHNnRNWThSb3JJejVDcFpXTmZqSjVqT0g1bDFVYmFqcElFa1YxNVBjaEpHOHlZc3U3amNtQjdFRVI0YmFJN3dKOFRoTEVBRm82Sk1NN3ZONVdadTlienByWTJRdlZxMUNMcGU4eU8zc3I3ZGxoZ0d0c2hnMWQiLCJtYWMiOiIzYWYxY2NlNjg2NGNkZDY3Y2U3YWUyYjlhOTcxOTI1ZWEwYzRhMWQ1MTE1NDEzZjZiMWFmMjFkOTQ0M2VkZGYwIiwidGFnIjoiIn0%3D',
                '_dc_gtm_UA-29592875-1': '1',
                '_ga': 'GA1.1.145911633.1704255367',
                '_ga_78C77YB2FT': 'GS1.1.1704304528.12.1.1704305234.41.0.0',
                '_ga_MJKVR7DKT0': 'GS1.3.1704304530.12.1.1704305235.60.0.0',
                '_ga_61RK6KN747': 'GS1.2.1704271441.2.1.1704305235.41.0.0',
            }

            headers_mega = {
                'authority': 'm.ticketon.kz',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
                'cache-control': 'max-age=0',
                # 'cookie': '_ym_uid=1694439152375035746; _ym_d=1694439152; _gcl_au=1.1.1472638931.1704255366; _gid=GA1.2.1415576106.1704255367; sc=3E576D12-E373-A45F-1AD5-EF9E1E89A8A0; _ym_isad=1; _tt_enable_cookie=1; _ttp=BnrR0tpeGMzkwcPAYwUhZjmf9gw; supportOnlineTalkID=AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt; PHPSESSID=nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70; _ga=GA1.3.145911633.1704255367; _gid=GA1.3.1415576106.1704255367; dsq__=3toevj325138ra; _ga_MJKVR7DKT0=GS1.2.1704276640.3.0.1704276640.60.0.0; _ga_61RK6KN747=GS1.3.1704271441.2.1.1704285060.60.0.0; _ym_visorc=b; _dc_gtm_UA-29592875-8=1; XSRF-TOKEN=eyJpdiI6IncxOHh0b29nV3NGSDU4eVFKQWVZQlE9PSIsInZhbHVlIjoiSUFVYjQxYXVxSytzb3lFOER0NzVzL1Z2WjZVQlN6czdRT2JQZFJtTytXVkorU0FsT2U0emxlK1FJV0JrNExBSUhsbGlKelBmNGhjVXZkMzljWVNEN1pyVk9ualk2NjhXZlZLU3UrdkZJUmE3UTNyWXhVeFpIRnhpWkhUQktKZUQiLCJtYWMiOiI5NDcyMGExODU3ODNkNGY5NTE2ZTc0ZjE2ZDhmN2QwZDRkMDI5YmU5MGRjNGI0NWI3MmRhOTM3N2U2Y2I2MjA2IiwidGFnIjoiIn0%3D; front_content_main_session=eyJpdiI6ImNJbDBycFpZdEw3UDJPVDJHTUxRWHc9PSIsInZhbHVlIjoiUTFJTnFwU2VlRkFHNnRNWThSb3JJejVDcFpXTmZqSjVqT0g1bDFVYmFqcElFa1YxNVBjaEpHOHlZc3U3amNtQjdFRVI0YmFJN3dKOFRoTEVBRm82Sk1NN3ZONVdadTlienByWTJRdlZxMUNMcGU4eU8zc3I3ZGxoZ0d0c2hnMWQiLCJtYWMiOiIzYWYxY2NlNjg2NGNkZDY3Y2U3YWUyYjlhOTcxOTI1ZWEwYzRhMWQ1MTE1NDEzZjZiMWFmMjFkOTQ0M2VkZGYwIiwidGFnIjoiIn0%3D; _dc_gtm_UA-29592875-1=1; _ga=GA1.1.145911633.1704255367; _ga_78C77YB2FT=GS1.1.1704304528.12.1.1704305234.41.0.0; _ga_MJKVR7DKT0=GS1.3.1704304530.12.1.1704305235.60.0.0; _ga_61RK6KN747=GS1.2.1704271441.2.1.1704305235.41.0.0',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            }
            
            # mega_prices = []
            # mega_student = []
            print(Fore.GREEN + "    Chaplin Mega Silk Way (Астана)")
            for i in range(len(time_mega)):
                hreff = str('https://m.ticketon.kz' + tickets[i].get('href'))
                ticket_resp = requests.get(hreff, cookies=cookies_mega, headers=headers_mega)
                soup_ticket = BeautifulSoup(ticket_resp.text, 'html.parser')
                prices = soup_ticket.find_all('a', class_='b-hall__seat-dropdown__link')
                if len(prices) == 2:
                    # khan_student.append(prices[1].text.strip())
                    print(f"        {time_mega[i].text.strip()} // {prices[0].text.strip()} // {prices[1].text.strip()}")
                elif len(prices) == 3:
                    print(f"        {time_mega[i].text.strip()} // {prices[0].text.strip()} // {prices[1].text.strip()} // {prices[2].text.strip()}")
                elif len(prices) == 4:
                    print(f"        {time_mega[i].text.strip()} // {prices[0].text.strip()} // {prices[1].text.strip()} // {prices[2].text.strip()} // {prices[3].text.strip()}")
                elif len(prices) == 1:
                    print(f"        {time_mega[i].text.strip()} // {prices[0].text.strip()}")
            
                

        if khan:
            time_khan = soup_cinema.find("a", string="Chaplin Khan Shatyr Астана (Нур-Султан)").find_parent().find_parent().find_all("time")
            tickets = soup_cinema.find("a", string="Chaplin Khan Shatyr Астана (Нур-Султан)").find_parent().find_parent().find_all('a', class_='b-button_buy-small')

            cookies_khan = {
                '_ym_uid': '1694439152375035746',
                '_ym_d': '1694439152',
                '_gcl_au': '1.1.1472638931.1704255366',
                '_gid': 'GA1.2.1415576106.1704255367',
                'sc': '3E576D12-E373-A45F-1AD5-EF9E1E89A8A0',
                '_ym_isad': '1',
                '_tt_enable_cookie': '1',
                '_ttp': 'BnrR0tpeGMzkwcPAYwUhZjmf9gw',
                'supportOnlineTalkID': 'AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt',
                'PHPSESSID': 'nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70',
                '_ga': 'GA1.3.145911633.1704255367',
                '_gid': 'GA1.3.1415576106.1704255367',
                'dsq__': '3toevj325138ra',
                '_ga_MJKVR7DKT0': 'GS1.2.1704276640.3.0.1704276640.60.0.0',
                '_ga_61RK6KN747': 'GS1.3.1704271441.2.1.1704285060.60.0.0',
                '_ym_visorc': 'b',
                '_dc_gtm_UA-29592875-8': '1',
                'XSRF-TOKEN': 'eyJpdiI6IncxOHh0b29nV3NGSDU4eVFKQWVZQlE9PSIsInZhbHVlIjoiSUFVYjQxYXVxSytzb3lFOER0NzVzL1Z2WjZVQlN6czdRT2JQZFJtTytXVkorU0FsT2U0emxlK1FJV0JrNExBSUhsbGlKelBmNGhjVXZkMzljWVNEN1pyVk9ualk2NjhXZlZLU3UrdkZJUmE3UTNyWXhVeFpIRnhpWkhUQktKZUQiLCJtYWMiOiI5NDcyMGExODU3ODNkNGY5NTE2ZTc0ZjE2ZDhmN2QwZDRkMDI5YmU5MGRjNGI0NWI3MmRhOTM3N2U2Y2I2MjA2IiwidGFnIjoiIn0%3D',
                'front_content_main_session': 'eyJpdiI6ImNJbDBycFpZdEw3UDJPVDJHTUxRWHc9PSIsInZhbHVlIjoiUTFJTnFwU2VlRkFHNnRNWThSb3JJejVDcFpXTmZqSjVqT0g1bDFVYmFqcElFa1YxNVBjaEpHOHlZc3U3amNtQjdFRVI0YmFJN3dKOFRoTEVBRm82Sk1NN3ZONVdadTlienByWTJRdlZxMUNMcGU4eU8zc3I3ZGxoZ0d0c2hnMWQiLCJtYWMiOiIzYWYxY2NlNjg2NGNkZDY3Y2U3YWUyYjlhOTcxOTI1ZWEwYzRhMWQ1MTE1NDEzZjZiMWFmMjFkOTQ0M2VkZGYwIiwidGFnIjoiIn0%3D',
                '_dc_gtm_UA-29592875-1': '1',
                '_ga': 'GA1.1.145911633.1704255367',
                '_ga_78C77YB2FT': 'GS1.1.1704304528.12.1.1704305234.41.0.0',
                '_ga_MJKVR7DKT0': 'GS1.3.1704304530.12.1.1704305235.60.0.0',
                '_ga_61RK6KN747': 'GS1.2.1704271441.2.1.1704305235.41.0.0',
            }

            headers_khan = {
                'authority': 'm.ticketon.kz',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
                'cache-control': 'max-age=0',
                # 'cookie': '_ym_uid=1694439152375035746; _ym_d=1694439152; _gcl_au=1.1.1472638931.1704255366; _gid=GA1.2.1415576106.1704255367; sc=3E576D12-E373-A45F-1AD5-EF9E1E89A8A0; _ym_isad=1; _tt_enable_cookie=1; _ttp=BnrR0tpeGMzkwcPAYwUhZjmf9gw; supportOnlineTalkID=AWPD7BCCv9BTfFbtOmK8C5h2sJ5hcUWt; PHPSESSID=nclfCN6lMhbD1pFprC-Z3KJdl5ef7bW64%2CwRkRLuLCz1ISDlND1AgoGhxi7Fhp6Up1JyGVe4qI1EzSBl%2CQ9L70; _ga=GA1.3.145911633.1704255367; _gid=GA1.3.1415576106.1704255367; dsq__=3toevj325138ra; _ga_MJKVR7DKT0=GS1.2.1704276640.3.0.1704276640.60.0.0; _ga_61RK6KN747=GS1.3.1704271441.2.1.1704285060.60.0.0; _ym_visorc=b; _dc_gtm_UA-29592875-8=1; XSRF-TOKEN=eyJpdiI6IncxOHh0b29nV3NGSDU4eVFKQWVZQlE9PSIsInZhbHVlIjoiSUFVYjQxYXVxSytzb3lFOER0NzVzL1Z2WjZVQlN6czdRT2JQZFJtTytXVkorU0FsT2U0emxlK1FJV0JrNExBSUhsbGlKelBmNGhjVXZkMzljWVNEN1pyVk9ualk2NjhXZlZLU3UrdkZJUmE3UTNyWXhVeFpIRnhpWkhUQktKZUQiLCJtYWMiOiI5NDcyMGExODU3ODNkNGY5NTE2ZTc0ZjE2ZDhmN2QwZDRkMDI5YmU5MGRjNGI0NWI3MmRhOTM3N2U2Y2I2MjA2IiwidGFnIjoiIn0%3D; front_content_main_session=eyJpdiI6ImNJbDBycFpZdEw3UDJPVDJHTUxRWHc9PSIsInZhbHVlIjoiUTFJTnFwU2VlRkFHNnRNWThSb3JJejVDcFpXTmZqSjVqT0g1bDFVYmFqcElFa1YxNVBjaEpHOHlZc3U3amNtQjdFRVI0YmFJN3dKOFRoTEVBRm82Sk1NN3ZONVdadTlienByWTJRdlZxMUNMcGU4eU8zc3I3ZGxoZ0d0c2hnMWQiLCJtYWMiOiIzYWYxY2NlNjg2NGNkZDY3Y2U3YWUyYjlhOTcxOTI1ZWEwYzRhMWQ1MTE1NDEzZjZiMWFmMjFkOTQ0M2VkZGYwIiwidGFnIjoiIn0%3D; _dc_gtm_UA-29592875-1=1; _ga=GA1.1.145911633.1704255367; _ga_78C77YB2FT=GS1.1.1704304528.12.1.1704305234.41.0.0; _ga_MJKVR7DKT0=GS1.3.1704304530.12.1.1704305235.60.0.0; _ga_61RK6KN747=GS1.2.1704271441.2.1.1704305235.41.0.0',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            }

            print(Fore.GREEN + "    Chaplin Khan Shatyr Астана (Нур-Султан)")
            for i in range(len(time_khan)):
                ticket_resp = requests.get(str('https://m.ticketon.kz' + tickets[i].get('href')), cookies=cookies_khan, headers=headers_khan)
                soup_ticket = BeautifulSoup(ticket_resp.text, 'html.parser')
                prices = soup_ticket.find_all('a', class_='b-hall__seat-dropdown__link')
                if len(prices) == 2:
                    print(f"        {time_khan[i].text.strip()} // {prices[0].text.strip()} // {prices[1].text.strip()}")
                elif len(prices) == 3:
                    print(f"        {time_khan[i].text.strip()} // {prices[0].text.strip()} // {prices[1].text.strip()} // {prices[2].text.strip()}")
                elif len(prices) == 4:
                    print(f"        {time_khan[i].text.strip()} // {prices[0].text.strip()} // {prices[1].text.strip()} // {prices[2].text.strip()} // {prices[3].text.strip()}")
                elif len(prices) == 1:
                    print(f"        {time_khan[i].text.strip()} // {prices[0].text.strip()}")

                    


        



        elif not khan and not mega:
            print('no suitable cinema for you, sir')

        # inp = str(input('Which film do you want to open: '))
        # inp = inp.lower()
        # if 'nothing' in inp or 'no' in inp:
        #     exit(1)
        # else:
        #     driver = webdriver.Chrome()
        #     driver.get(url=all_links[int(inp)-1])
        #     t = str(input('Do you want to stop: '))
        #     exit(1)
            

    except Exception as ex:
        print(ex)
        
        


get_films()
