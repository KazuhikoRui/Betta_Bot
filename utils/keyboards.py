from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Показатели игрока")],
              [KeyboardButton(text="Показатели магии")],
              [KeyboardButton(text="Игрок vs Игрок")],
              [KeyboardButton(text="Игрок vs Магия")],
              [KeyboardButton(text="Магия vs Магия")],
              [KeyboardButton(text="Процентник")]],
resize_keyboard=True,
one_time_keyboard=True,
input_field_placeholder="Выберите одну из опций...")