from utils.ailmath import PhysTools, MagTools
import random

p_tools = PhysTools()
m_tools = MagTools()

def getStrFromDict(dict):
    msg = ''
    for i, j in dict.items():
        msg += i + " - " + str(j) + "\n"
    return msg

def getChance(percent):
       if (percent/100 > random.random()):
              return "Удалось"
       else:
              return "Не удалось"
def getMyParams(p_str, p_dex, p_con, p_reac, p_mag, weap = 0, shield = 0):
    res = {"Урон от удара": p_tools.impact_damage(p_str, p_dex, weap),
           "Бег": p_tools.run_speed(p_str, p_dex),
           "Скорость Атак": p_tools.attack_speed(p_str, p_dex),
           "Здоровье": p_tools.health(p_str, p_dex, p_con),
           "Уворотливость": p_tools.def_dex(p_dex, p_reac),
           "Блок": p_tools.def_stren(p_str, p_reac, shield),
           "Чтение заклинаний": p_tools.def_mag(p_mag, p_reac)}
    return res

def getMyMagic(m_str, m_speed, m_dur):
       res = {"Урон заклинания": m_tools.impact_damage(m_str, m_speed),
              "Скорость заклинания": m_tools.mag_speed(m_speed),
              "Прочность заклинания": m_tools.durability(m_dur),
              "Хил/пост" : m_tools.heal_per_post(m_str, m_speed),
              "Хил": m_tools.heal(m_str, m_speed),
              "Яд/пост": m_tools.poison(m_str, m_speed)}
       return res

def getPvP(player_1, player_2):
       p1_stats = getMyParams(*player_1)
       p2_stats = getMyParams(*player_2)

       res = {"Уворотливость": getDexAdvice(p1_stats["Уворотливость"], p2_stats["Скорость Атак"]),
              "Блок": getStrAdvice(p1_stats["Блок"], p2_stats["Урон от удара"]),
              "Магия": getMagVSPhysAdvice(p1_stats["Чтение заклинаний"], p2_stats["Скорость Атак"])}

       return res

def getPvM(player_1, magic):
       p1_stats = getMyParams(*player_1)
       m_stats = getMyMagic(*magic)

       res = {"Уворотливость": getDexAdvice(p1_stats["Уворотливость"], m_stats["Скорость заклинания"]),
              "Блок": getStrAdvice(p1_stats["Блок"], m_stats["Урон заклинания"]),
              "Магия": getMagVSMagAdvice(p1_stats["Чтение заклинаний"], m_stats["Скорость заклинания"])}

       return res

def getDexAdvice(p1_ddef, p2_aspeed):
       if p1_ddef - p2_aspeed >= 0:
              return "вы без проблем увернетесь"
       elif p1_ddef - p2_aspeed >= -2:
              return "ваш шанс увернуться 80%"
       elif p1_ddef - p2_aspeed >= -4:
              return "ваш шанс увернуться 65%"
       elif p1_ddef - p2_aspeed >= -6:
              return "ваш шанс увернуться 50%"
       else:
              return "вы не можете увернуться"
def getStrAdvice(p1_sdef, p2_impact):
       if p1_sdef - p2_impact >= 0:
              return "вы полностью блокируете весь урон"
       else:
              return f"вы не можете полностью заблокировать {abs(p1_sdef - p2_impact)} урона"
def getMagVSPhysAdvice(p1_mdef, p2_aspeed):
       if p1_mdef - p2_aspeed >= 0:
              return "вы можете защититься магией от физ. атак"
       else:
              return "вы не можете защититься магией от физ. атак"

def getMagVSMagAdvice(p1_mdef, p2_aspeed):
       if p1_mdef - p2_aspeed >= 0:
              return "вы можете защититься магией от маг. атак"
       else:
              return "вы не можете защититься магией от маг. атак"

def pvpSummary(player_1, player_2):
       res = "Вы vs Соперник\n\n"
       p1 = getMyParams(*player_1)
       p2 = getMyParams(*player_2)

       for i, j in p1.items():
              if j > p2[i]:
                     res += i + ": " + str(j) + " > " + str(p2[i]) + "\n"
              elif j == p2[i]:
                     res += i + ": " + str(j) + " = " + str(p2[i]) + "\n"
              else:
                     res += i + ": " + str(j) + " < " + str(p2[i]) + "\n"

       res += "\n\n"
       res += "Советы:\n"+getStrFromDict(getPvP(player_1, player_2))

       return res

def pvmSummary(player, magic):
       res = "Вы vs Магия\n\nВаши показатели:\n\n"
       p = getMyParams(*player)
       m = getMyMagic(*magic)

       for i, j in p.items():
              res += i + ": " + str(j) + "\n"

       res += "---------------------\nМагия врага:\n\n"

       for i, j in m.items():
              res += i + ": " + str(j) + "\n"

       res += "\n\n"
       res += "Советы:\n" + getStrFromDict(getPvM(player, magic))

       return res

def mvmSummary(mag_1, mag_2):
       res = "Вы vs Соперник\n\n"
       m1 = getMyMagic(*mag_1)
       m2 = getMyMagic(*mag_2)

       for i, j in m1.items():
              if j > m2[i]:
                     res += i + ": " + str(j) + " > " + str(m2[i]) + "\n"
              elif j == m2[i]:
                     res += i + ": " + str(j) + " = " + str(m2[i]) + "\n"
              else:
                     res += i + ": " + str(j) + " < " + str(m2[i]) + "\n"
       return res

