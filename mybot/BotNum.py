from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from random import *

API_TOKEN: str = '5835824434:AAG8y6naYxcjTpnNH4Ao3ob685qnG6238GA'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)
user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0,
              'losing': 0}

phrases_too_much = ['Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
                    'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
phrases_too_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
                      'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!']
phrases_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
                  'Горячо!']
phrases_too_soon = ['Ого, так быстро еще никто не отгадывал!', 'Да ты волшебник! Ты угадал моё число',
                    'Скажи честно, ты подглядывал?',
                    'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']
too_little = ['Чуть меньше', 'Поменьше', 'Немного меньше']
too_much = ['Чуть Больше', 'Побольше', 'Немного больше']


def get_random_number() -> int:
    return randint(1, 100)


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру\n"Числовая угадайка"?\n\n'
                         'Чтобы получить правила игры и список доступных команд - отправьте команду /help')


@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\n'
                         f'Я загадываю число от 1 до 100, а ты попробуешь его отгадать.\n'
                         f'Доступные команды:\n/help - правила игры и список команд\n/cancel - выйти из игры'
                         f'\n/stat - посмотреть статистику\n\n'
                         f'Выбери уровень сложности и начинаем:\n'
                         f'/easy: 7 попыток;\n'
                         f'-----------------\n'
                         f'/normal: 6 попыток;\n'
                         f'-----------------\n'
                         f'/hard: 5 попыток;\n'
                         f'-----------------\n'
                         f'/harder: 3 попытки;\n'
                         f'-----------------\n'
                         f'/insane: 2 попытки;\n'
                         f'-----------------\n'
                         f'/demon: 1 попытка;\n\n'
                         )


@dp.message_handler(commands=['stat'])
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\nИгр выиграно: {user["wins"]}\n'
                         f'Игр проиграно: {user["losing"]}')


@dp.message_handler(commands=['cancel'])
async def process_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Ты вышел из игры. Если захочешь сыграть снова - напиши об этом')
        user['in_game'] = False
    else:
        await message.answer('А мы итак с тобой не играем. Может, сыграем разок?')


@dp.message_handler(commands=['easy'])
async def process_easy_answer(message: Message):
    if not user['in_game']:
        await message.answer('Думаю ты легко с этим справишься!😊 \n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 7
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(commands=['normal'])
async def process_normal_answer(message: Message):
    if not user['in_game']:
        await message.answer('Тут нужно подключить интуицию!😉\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 6
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(commands=['hard'])
async def process_hard_answer(message: Message):
    if not user['in_game']:
        await message.answer('Это сложней чем ты думаешь!😏\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 5
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(commands=['harder'])
async def process_harder_answer(message: Message):
    if not user['in_game']:
        await message.answer('Тут одним везением не отделаться!😳\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 3
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(commands=['insane'])
async def process_insane_answer(message: Message):
    if not user['in_game']:
        await message.answer('Это безумно!🤯\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 2
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(commands=['demon'])
async def process_demon_answer(message: Message):
    if not user['in_game']:
        await message.answer('Что ты такое?👹\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 1
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(Text(equals=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть'], ignore_case=True))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer(f'Выбери уровень сложности и начинаем:\n'
                             f'/easy: 7 попыток;\n'
                             f'-----------------\n'
                             f'/normal: 6 попыток;\n'
                             f'-----------------\n'
                             f'/hard: 5 попыток;\n'
                             f'-----------------\n'
                             f'/harder: 3 попытки;\n'
                             f'-----------------\n'
                             f'/insane: 2 попытки;\n'
                             f'-----------------\n'
                             f'/demon: 1 попытка;\n\n')

    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды '
            '/cancel и /stat')


@dp.message_handler(Text(equals=['Нет', 'Не', 'Не хочу'], ignore_case=True))
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer('Жаль :(\n\nЕсли захочешь поиграть - просто напиши об этом')
    else:
        await message.answer('Мы же играем в "Числовую угадайку". Присылай, пожалуйста, числа от 1 до 100')


@dp.message_handler(lambda x: x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer(f'{choice(phrases_too_soon)}\n\nМожет, сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            if abs(int(message.text) - user['secret_number']) < 5:
                await message.answer(f'{choice(too_little)}\n{choice(phrases_almost)}')
                user['attempts'] -= 1
            else:
                await message.answer(choice(phrases_too_much))
                user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            if abs(int(message.text) - user['secret_number']) < 5:
                await message.answer(f'{choice(too_much)}\n{choice(phrases_almost)}')
                user['attempts'] -= 1
            else:
                await message.answer(choice(phrases_too_little))
                user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(
                f'К сожалению, у тебя больше не осталось попыток.\nТы проиграл💀\n\nМое число было '
                f'{user["secret_number"]}\n\nЕсли хочешь еще испытать свою удачу выбери уровень?\n'
                f'-----------------\n'
                f'/easy: 7 попыток;\n'
                f'-----------------\n'
                f'/normal: 6 попыток;\n'
                f'-----------------\n'
                f'/hard: 5 попыток;\n'
                f'-----------------\n'
                f'/harder: 3 попытки;\n'
                f'-----------------\n'
                f'/insane: 2 попытки;\n'
                f'-----------------\n'
                f'/demon: 1 попытка;\n\n'
                f'Если желаешь закончить отправь команду /cancel'
            )
            user['in_game'] = False
            user['total_games'] += 1
            user['losing'] += 1
    else:
        await message.answer('Мы еще не играем. Желаешь сыграть?')


@dp.message_handler()
async def process_other_text_answers(message: Message):
    if user['in_game']:
        await message.answer('Мы же сейчас играем. Присылай, пожалуйста, числа от 1 до 100.\n'
                             'Если желаешь окончить игру, отправь команду /cancel')
    else:
        await message.answer('Если ты хочешь начать игру просто нажми /start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
