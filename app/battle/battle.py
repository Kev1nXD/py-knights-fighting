class Battle:

    @staticmethod
    def knight_equipped(knight):
        knight.power += knight.knights_weapon_equipped()
        if len(knight.armour) >= 1:
            knight.armour = knight.knights_armour_equipping()
        else:
            knight.armour = 0
        if knight.potion is not None:
            (extra_power,
             extra_hp,
             extra_protection) = knight.knights_potion_drinking()
            knight.power += extra_power
            knight.hp += extra_hp
            knight.armour += extra_protection

    @staticmethod
    def duel(first_duelist, second_duelist):
        first_duelist.hp -= second_duelist.power - first_duelist.armour
        second_duelist.hp -= first_duelist.power - second_duelist.armour
        if first_duelist.hp <= 0:
            first_duelist.hp = 0
        if second_duelist.hp <= 0:
            second_duelist.hp = 0
