import math


class PhysTools:

  def impact_damage(self, stren=1, dex=1, weapon=0) -> int:
    return int(((dex * 2 + stren * 4) + weapon * 2) * 2)

  def run_speed(self, stren=1, dex=1) -> int:
    return int((dex * 2 + stren) * 2)

  def attack_speed(self, stren=1, dex=1) -> int:
    return int(round((stren / 3 + dex * 4) / 2, 0))

  def health(self, stren=1, dex=1, con=1) -> int:
    return int(round((con * 3 + stren + dex / 2) * math.exp(1) * 2.5, 0))

  def def_dex(self, dex=1, reac=1) -> int:
    return int(round((dex + reac * 3) / 2.5, 0))

  def def_stren(self, stren=1, reac=1, shield=0) -> int:
    return int((round((stren + reac * 3) / 2.5, 0) + shield * 2) * 5)

  def def_mag(self, magic=1, reac=1) -> int:
    return int(round((magic * 2 + reac * 3) / 2.5, 0))


class MagTools:

  def impact_damage(self, stren=1, speed=1) -> int:
    return int(round((speed * 2 + stren * 4) * math.exp(1), 0))

  def mag_speed(self, speed=1) -> int:
    return int(round((1 + speed * 5) / 2, 0))

  def durability(self, dur=1) -> int:
    return int(round(dur * math.exp(1), 0) * 5)

  def heal_per_post(self, stren=1, speed=1) -> int:
    return int((speed + stren * 3))

  def heal(self, stren=1, speed=1) -> int:
    return int(round((speed + stren * 4) * math.exp(1), 0))

  def poison(self, stren=1, speed=1) -> int:
    return int((speed + stren * 4))