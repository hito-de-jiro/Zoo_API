#! Python3
# zoo_API.py -- скрапер сайту https://www.zooplus.de/
# отримує доступ до API, та робить парсинг отриманих даних
# дані зберігаються у CSV-файл
import csv
import json
import requests


def get_json():
    """Отримує доступ до API сайту та повертає дані у форматі списку"""
    page = 3  # Кількість сторінок для скрепінга
    i = 1
    res_num = 0
    json_data = []
    sess = requests.Session()  # створення сессії
    # цикл отримання токена для доступу до API
    while i <= page:
        api_url = 'https://www.zooplus.de/tierarzt/api/v2/token?debug=authReduxMiddleware-tokenIsExpired'
        api_headers = {
            "accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        res_api = sess.get(url=api_url, headers=api_headers)
        api_token = json.loads(res_api.text)
        # Створення запиту для отримання доступу
        url = f"https://www.zooplus.de/tierarzt/api/v2/results?animal_99=true&page={str(i)}&from={str(res_num)}&size=20"
        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "authorization": f"Bearer {api_token['token']}",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "x-api-authorization": f"{api_token['token']}"
        }
        # Отримання даних у форматі JSON
        res = sess.get(url=url, headers=headers)
        json_data.append(res.json())
        i += 1
        res_num += 20
    with open('raw_data.json', 'w') as f:  # Збереження даних у форматі JSON
        json.dump(json_data, f)
    print('Done!')
    return json_data  # Дані у форматі списку


def get_data(all_data_json):
    """Отримання даних з файлу JSON"""
    for data in all_data_json:
        for data_dict in data['results']:
            name = data_dict['name']
            review_score = f"{data_dict['avg_review_score']} stars in Google"
            recommendations = f"{data_dict['count_reviews']} recommendations"
            try:
                description = data_dict['subtitle']
            except KeyError:
                description = ''
            address = data_dict['address']
            zip_code = data_dict['zip']
            city = data_dict['city']
            full_address = f'{address}, {city}, {zip_code}'
            open_time = data_dict['open_time']
            working_hours = opening_hours(open_time)
            # Створення словника для запису готових даних
            all_data_dict = {'name': name, 'rating': review_score, 'recommendations': recommendations,
                             'description': description, 'address': full_address, 'working_hours': working_hours}
            csv_writer(all_data_dict.values())  # Передача значень для запису в CSV-файл


def opening_time_format(open_time):
    """Форматування отриманих даних про час роботи у формат 'день: час роботи'"""
    open_days = {'mo': [], 'di': [], 'mi': [], 'do': [], 'fr': [], 'sa': [], 'so': []}
    for days in open_time:
        for v in days.values():
            if days['day'] == 1 and len(str(v)) > 1:
                open_days['mo'].append(v)
            elif days['day'] == 2 and len(str(v)) > 1:
                open_days['di'].append(v)
            elif days['day'] == 3 and len(str(v)) > 1:
                open_days['mi'].append(v)
            elif days['day'] == 4 and len(str(v)) > 1:
                open_days['do'].append(v)
            elif days['day'] == 5 and len(str(v)) > 1:
                open_days['fr'].append(v)
            elif days['day'] == 6 and len(str(v)) > 1:
                open_days['sa'].append(v)
            elif days['day'] == 7 and len(str(v)) > 1:
                open_days['so'].append(v)
    return open_days


def opening_hours(open_time):
    """Кінцеве форматування данних та вивід у вигляді рядка"""
    open_days = opening_time_format(open_time)
    working_hours = []  # -- робочий час у тижні
    for k, v in open_days.items():
        if len(v) == 4:
            first = f"{k}: {str(v[0]).replace('00', ':00')}-{str(v[1]).replace('00', ':00')}"
            second = f"/{str(v[2]).replace('00', ':00')}-{str(v[3]).replace('00', ':00')}"
            working_hours.append(first + second)
        elif len(v) == 2:
            first = f"{k}: {str(v[0]).replace('00', ':00')}-{str(v[1]).replace('00', ':00')}"
            working_hours.append(first)
    hours = ', '.join(working_hours)  # створення рядка
    return hours


def csv_writer(data_dict):
    """Створення та запис CSV-файлу"""
    data_csv = open('csv_data.csv', 'a', newline='', encoding='utf-8')
    csv_dict_writer = csv.writer(data_csv)  # create headers in CSV-document
    csv_dict_writer.writerow(data_dict)  # write to CSV
    data_csv.close()


def main():
    """Головна функція"""
    get_data(get_json())


if __name__ == "__main__":
    main()
