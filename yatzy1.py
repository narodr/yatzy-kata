class YatzyConfig:
    def __init__(self, number_of_dice: int = 5, number_of_faces: int = 6):
        self.number_of_dice = number_of_dice
        self.number_of_faces = number_of_faces


class Yatzy(YatzyConfig): 
    def __init__(self, dice: list):
        super().__init__()
        self.dice = dice
        self.chance = self.chance()
        self.yazty = self.yazty()
        self.one_pair = self.one_pair()
        self.two_pair = self.two_pair()
        self.four_of_a_kind = self.four_of_a_kind()
        self.three_of_a_kind = self.three_of_a_kind()
        self.small_straight = self.small_straight()
        self.large_straight = self.large_straight()
        self.full_house = self.full_house()

    def __len__(self):
        return len(self.dice)
    
    @property
    def dice(self):
        return self._dice
    
    @dice.setter
    def dice(self, dice):
        if not isinstance(dice, list):
            raise TypeError("dice must be a list")
        if len(dice) != self.number_of_dice:
            raise ValueError("dice must be a list of length equal to {self.number_of_dice}")
        for die in dice:
            if not isinstance(die, int):
                raise TypeError("dice must be a list of integers")
            if die < 1 or die > self.number_of_faces:
                raise ValueError("dice must be a list of integers between 1 and {self.number_of_faces}")
        self._dice = dice

    def _frequency_of_number(self, number_to_check):
        count = 0
        for die in self.dice:
            if die == number_to_check:
                count += 1
        return count

    def chance(self):
        total = 0
        for die in self.dice:
            total += die
        return total

    def yazty(self):
        for face in range(self.number_of_faces, 0, -1):
            if (self._frequency_of_number(face) == len(self)):
                return 50
        return 0

    def sum_by_number(self, number_to_check):
        sum = 0
        for die in self.dice:
            if die == number_to_check:
                sum += number_to_check
        return sum

    def one_pair(self):
        for face in range(self.number_of_faces, 0, -1):
            if (self._frequency_of_number(face) == 2):
                return face * 2
        return 0

    def two_pair(self):
        n = 0
        score = 0
        for face in range(self.number_of_faces, 0, -1):
            if (self._frequency_of_number(face) >= 2):
                n += 1
                score += face * 2
        if (n == 2):
            return score
        else:
            return 0

    def four_of_a_kind(self):
        for face in range(self.number_of_faces, 0, -1):
            if (self._frequency_of_number(face) >= 4):
                return face * 4
        return 0

    def three_of_a_kind(self):
        for face in range(self.number_of_faces, 0, -1):
            if (self._frequency_of_number(face) >= 3):
                return face * 3
        return 0

    def small_straight(self):
        numbers = [1, 2, 3, 4, 5]
        for number in numbers:
            if self._frequency_of_number(number) != 1:
                return 0
        return 15            

    def large_straight(self):
        numbers = [2, 3, 4, 5, 6]
        for number in numbers:
            if self._frequency_of_number(number) != 1:
                return 0
        return 20

    def full_house(self):
        exists_three = False
        exists_pair = False
        for face in range(self.number_of_faces, 0, -1):
            if (self._frequency_of_number(face) == 3):
                exists_three = True
            if (self._frequency_of_number(face) == 2):
                exists_pair = True
        if (exists_pair and exists_three):
            return self.chance
        else:
            return 0