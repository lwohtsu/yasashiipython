from pybot_eto import eto_command
from pybot_random2 import choice_command, dice_command
from pybot_datetime2 import today_command, now_command, weekday_command
from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command


def heisei_command(command):
    heisei, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
        else:
            response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    else:
        response = '数値ヲ指定シテクダサイ'
    return response


def len_command(command):
    cmd, text = command.split(maxsplit=1)
    length = len(text)
    response = '文字列ノ長サハ {} 文字デス'.format(length)
    return response


def pybot(command):
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            break

    if '平成' in command:
        response = heisei_command(command)
    if '長さ' in command:
        response = len_command(command)
    if '干支' in command:
        response = eto_command(command)
    if '選ぶ' in command:
        response = choice_command(command)
    if 'さいころ' in command:
        response = dice_command()
    if '今日' in command:
        response = today_command()
    if '現在' in command:
        response = now_command()
    if '曜日' in command:
        response = weekday_command(command)
    if '天気' in command:
        response = weather_command()
    if '事典' in command:
        response = wikipedia_command(command)

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    return response


bot_dict = {}
command_file = open('pybot04.csv', encoding='utf-8')
raw_data = command_file.read()
for line in raw_data.splitlines():
    key, response = line.split(',')
    bot_dict[key] = response

while False:
    command = input('pybot> ')
    try:
        response = pybot(command)
        print(response)
        if 'さようなら' in command:
            break
    except Exception as e:
        print('予期セヌ エラーガ 発生シマシタ')
        print('* 種類:', type(e))
        print('* 内容:', e)
