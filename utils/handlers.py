from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb
import utils.ailfunc as Ai
class Params(StatesGroup):
    phys_params = State()
    magic_params = State()
    pvp = State()
    pvp_enemy = State()
    pvm = State()
    pvm_enemy = State()
    mvm = State()
    mvm_enemy = State()
    chance = State()

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
  await message.answer("Ну, привет... Выбирай быстрее...",
                       reply_markup=kb.main)

@router.message(F.text == "Показатели игрока")
async def reqPparams(message: Message, state: FSMContext):
    await state.set_state(Params.phys_params)
    await message.answer("Введи ваши показатели в следующем порядке:\n\n"
                         "1) сила\n"
                         "2) ловкость\n"
                         "3) выносливость\n"
                         "4) реакция\n"
                         "5) магия\n"
                         "6) урон_оружия(необязательно)\n"
                         "7) показатель_щита(необязательно)\n"
                         "Например: 2 4 1 8 1 2")

@router.message(Params.phys_params)
async def getPparams(message: Message, state: FSMContext):
    await state.update_data(phys_params=message.text)
    data = await state.get_data()
    try:
        data = list(map(int, data["phys_params"].split()))
        await message.answer(Ai.getStrFromDict(Ai.getMyParams(*data)), reply_markup=kb.main)
        await state.clear()
    except:
        await message.answer("Введи данные нормально! Давай всё сначала!", reply_markup=kb.main)
        await state.clear()

@router.message(F.text == "Показатели магии")
async def reqMparams(message: Message, state: FSMContext):
    await state.set_state(Params.magic_params)
    await message.answer("Введи ваши показатели в следующем порядке:\n\n"
                         "1) сила\n"
                         "2) скорость\n"
                         "3) прочность\n"
                         "Например: 2 4 2")

@router.message(Params.magic_params)
async def getMparams(message: Message, state: FSMContext):
    await state.update_data(magic_params=message.text)
    data = await state.get_data()
    try:
        data = list(map(int, data["magic_params"].split()))
        await message.answer(Ai.getStrFromDict(Ai.getMyMagic(*data)), reply_markup=kb.main)
        await state.clear()
    except:
        await message.answer("Введи данные нормально! Давай всё сначала!", reply_markup=kb.main)
        await state.clear()


@router.message(F.text == "Процентник")
async def reqChance(message: Message, state: FSMContext):
    await state.set_state(Params.chance)
    await message.answer("Сколько процентов? Вводи цифрой и всё!")

@router.message(Params.chance)
async def getChance(message: Message, state: FSMContext):
    await state.update_data(chance=message.text)
    data = await state.get_data()
    try:
        ans = Ai.getChance(float(data["chance"]))
        await message.answer(ans, reply_markup=kb.main)
        await state.clear()
    except:
        await message.answer("Введи данные нормально! Давай всё сначала!", reply_markup=kb.main)
        await state.clear()

#------------------------

@router.message(F.text == "Игрок vs Игрок")
async def reqPvPparams(message: Message, state: FSMContext):
    await state.set_state(Params.pvp)
    await message.answer("Введи ваши показатели в следующем порядке:\n\n"
                         "1) сила\n"
                         "2) ловкость\n"
                         "3) выносливость\n"
                         "4) реакция\n"
                         "5) магия\n"
                         "6) урон_оружия(необязательно)\n"
                         "7) показатель_щита(необязательно)\n"
                         "Например: 2 4 1 8 1 2")


@router.message(Params.pvp)
async def getPvPparams(message: Message, state: FSMContext):
    await state.update_data(p1=message.text)
    await state.set_state(Params.pvp_enemy)
    await message.answer("Введи в такой же форме показатели врага\n"
                         "Например: 2 1 4 3 1 1")

@router.message(Params.pvp_enemy)
async def getPvpresult(message: Message, state: FSMContext):
    await state.update_data(p2=message.text)
    data = await state.get_data()
    try:
        player_1 = list(map(int, data["p1"].split()))
        player_2 = list(map(int, data["p2"].split()))
        await message.answer(Ai.pvpSummary(player_1, player_2), reply_markup=kb.main)
        await state.clear()
    except:
        await message.answer("Введи данные нормально! Давай всё сначала!", reply_markup=kb.main)
        await state.clear()

#------------------------

@router.message(F.text == "Игрок vs Магия")
async def reqPvMparams(message: Message, state: FSMContext):
    await state.set_state(Params.pvm)
    await message.answer("Введи ваши показатели в следующем порядке:\n\n"
                         "1) сила\n"
                         "2) ловкость\n"
                         "3) выносливость\n"
                         "4) реакция\n"
                         "5) магия\n"
                         "6) урон_оружия(необязательно)\n"
                         "7) показатель_щита(необязательно)\n"
                         "Например: 2 4 1 8 1 2")


@router.message(Params.pvm)
async def getPvMparams(message: Message, state: FSMContext):
    await state.update_data(p1=message.text)
    await state.set_state(Params.pvm_enemy)
    await message.answer("Введи показатели магии в следующем порядке:\n\n"
                         "1) сила\n"
                         "2) скорость\n"
                         "3) прочность\n"
                         "Например: 2 4 2")

@router.message(Params.pvm_enemy)
async def getPvMresult(message: Message, state: FSMContext):
    await state.update_data(p2=message.text)
    data = await state.get_data()
    try:
        player_1 = list(map(int, data["p1"].split()))
        player_2 = list(map(int, data["p2"].split()))
        await message.answer(Ai.pvmSummary(player_1, player_2), reply_markup=kb.main)
        await state.clear()
    except:
        await message.answer("Введи данные нормально! Давай всё сначала!", reply_markup=kb.main)
        await state.clear()

#------------------------

@router.message(F.text == "Магия vs Магия")
async def reqMvMparams(message: Message, state: FSMContext):
    await state.set_state(Params.mvm)
    await message.answer("Введи показатели магии в следующем порядке:\n\n"
                         "1) сила\n"
                         "2) скорость\n"
                         "3) прочность\n"
                         "Например: 2 4 2")


@router.message(Params.mvm)
async def getMvMparams(message: Message, state: FSMContext):
    await state.update_data(p1=message.text)
    await state.set_state(Params.mvm_enemy)
    await message.answer("Введи в такой же форме показатели врага\n"
                         "Например: 2 1 4")

@router.message(Params.mvm_enemy)
async def getMvMresult(message: Message, state: FSMContext):
    await state.update_data(p2=message.text)
    data = await state.get_data()
    try:
        player_1 = list(map(int, data["p1"].split()))
        player_2 = list(map(int, data["p2"].split()))
        await message.answer(Ai.mvmSummary(player_1, player_2), reply_markup=kb.main)
        await state.clear()
    except:
        await message.answer("Введи данные нормально! Давай всё сначала!", reply_markup=kb.main)
        await state.clear()

