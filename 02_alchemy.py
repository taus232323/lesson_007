# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return self._create_storm(other)
        elif isinstance(other, Fire):
            return self._create_vapour(other)
        elif isinstance(other, Ground):
            return self._create_dirt(other)
        elif isinstance(other, Iron):
            return self._create_rust(other)
        else:
            raise TypeError('Unsupported operand type(s)')

    def _create_storm(self, air):
        return Storm(water=self, air=air)

    def _create_vapour(self, fire):
        return Vapour(water=self, fire=fire)

    def _create_dirt(self, ground):
        return Dirt(water=self, ground=ground)

    def _create_rust(self, iron):
        return Rust(water=self, iron=iron)

class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Air):
            return self._create_lightning(other)
        elif isinstance(other, Ground):
            return self._create_vapour(other)
        elif isinstance(other, Iron):
            return self._create_tool(other)
        else:
            raise TypeError('Unsupported operand type(s)')

    def _create_lightning(self, air):
        return Lightning(fire=self, air=air)

    def _create_vapour(self, ground):
        return Lava(fire=self, ground=ground)

    def _create_tool(self, iron):
        return Tool(fire=self, iron=iron)

class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Ground):
            return self._create_dust(other)
        elif isinstance(other, Iron):
            return self._create_sound(other)
        else:
            print('Неизвестный элемент!')

    def _create_dust(self, ground):
        return Dust(air=self, ground=ground)

    def _create_sound(self, iron):
        return Sound(air=self, iron=iron)

class Ground:
    def __str__(self):
        return 'Ground'

    def __add__(self, other):
        if isinstance(other, Iron):
            return self._create_garden(other)
        else:
            raise TypeError('Unsupported operand type(s)')

    def _create_garden(self, iron):
        return Garden(ground=self, iron=iron)

class Iron:
    def __str__(self):
        return 'Iron'

class Dirt:
    def __init__(self, water, ground):
        self.water = water
        self.ground = ground

    def __str__(self):
        return 'I am Dirt I consist: ' + str(self.water) + ' и ' + str(self.ground)

class Storm:
    def __init__(self, water, air):
        self.water = water
        self.air = air

    def __str__(self):
        return 'I am Storm I consist: ' + str(self.water) + ' and ' + str(self.air)

class Vapour:
    def __init__(self, water, fire):
        self.water = water
        self.fire = fire

    def __str__(self):
        return 'I am Vapour I consist: ' + str(self.water) + ' and ' + str(self.fire)

class Lightning:
    def __init__(self, fire, air):
        self.fire = fire
        self.air = air

    def __str__(self):
        return 'I am Lightning I consist: ' + str(self.fire) + ' и ' + str(self.air)

class Dust:
    def __init__(self, air, ground):
        self.air = air
        self.ground = ground

    def __str__(self):
        return 'I am Dust I consist: ' + str(self.air) + ' и ' + str(self.ground)

class Lava:
    def __init__(self, fire, ground):
        self.fire = fire
        self.ground = ground

    def __str__(self):
        return 'I am Lava I consist: ' + str(self.fire) + ' и ' + str(self.ground)

class Rust:
    def __init__(self, water, iron):
        self.water = water
        self.iron = iron

    def __str__(self):
        return 'I am Rust I consist: ' + str(self.water) + ' и ' + str(self.iron)

class Sound:
    def __init__(self, air, iron):
        self.air = air
        self.iron = iron

    def __str__(self):
        return 'I am Sound I consist: ' + str(self.air) + ' и ' + str(self.iron)

class Tool:
    def __init__(self, fire, iron):
        self.fire = fire
        self.iron = iron

    def __str__(self):
        return 'I am Tool I consist: ' + str(self.fire) + ' и ' + str(self.iron)

class Garden:
    def __init__(self, ground, iron):
        self.ground = ground
        self.iron = iron

    def __str__(self):
        return 'I am Sound I consist: ' + str(self.ground) + ' и ' + str(self.iron)


iron = Iron()
water = Water()
air = Air()
fire = Fire()
ground = Ground()
storm = water + air
vapour = water + fire
dirt = water + ground
lightning = fire + air
lava = fire + ground
dust = air + ground
rust = water + iron
sound = air + iron
tool = fire + iron
garden = ground + iron
print(Water(), '+', Air(), '=', storm)
print(Water(), '+', Fire(), '=', vapour)
print(Water(), '+', Ground(), '=', dirt)
print(Fire(), '+', Air(), '=', lightning)
print(Fire(), '+', Ground(), '=', lava)
print(Air(), '+', Ground(), '=', dust)
print(Iron(), '+', Water(), '=', rust)
print(Iron(), '+', Air(), '=', sound)
print(Iron(), '+', Fire(), '=', tool)
print(Iron(), '+', Ground(), '=', garden)



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
