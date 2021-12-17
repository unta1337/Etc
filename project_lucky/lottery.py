import random as rand

from lottery_number_history import *

def main():
    print('# 고른 분포')
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(3, 3, number_history)
    print()

    print('# 홀수 편향')
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(4, 2, number_history)
    print()

    print('# 짝수 편향')
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(2, 4, number_history)
    print()

    print('# 대조군')
    pick_numbers(0, 6, number_history)
    pick_numbers(1, 5, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(5, 1, number_history)
    pick_numbers(6, 0, number_history)
    pick_numbers(0, 6, number_history)
    pick_numbers(1, 5, number_history)
    pick_numbers(2, 4, number_history)
    pick_numbers(3, 3, number_history)
    pick_numbers(4, 2, number_history)
    pick_numbers(5, 1, number_history)
    pick_numbers(6, 0, number_history)
    print()

def pick_numbers(odd_count, even_count, number_history):
    lucky_numbers = number_phile(odd_count, even_count)
    count = lucky_numbers.get_count_max(number_history)
    print(f'{lucky_numbers.numbers} : {count}')

class number_phile:
    def __init__(self, odd_max, even_max):
        self.numbers = []

        self.odd_max = odd_max
        self.even_max = even_max

        self.odd_count = 0
        self.even_count = 0

        for _ in range(6):
            self.next_number()
        self.numbers.sort()

    # 실제 번호화 일치도 반환. (특정 조합)
    def get_count(self, number_history):
        count = 0
        for i in self.numbers:
            if i in number_history:
                count += 1

        return count

    # 실제 번호화 일치도 반환. (최댓값)
    def get_count_max(self, number_history):
        count = 0
        count_max = 0
        for numbers in number_history:
            for i in self.numbers:
                if i in numbers:
                    count += 1

            if count > count_max:
                count_max = count
            count = 0

        return count_max

    # 숫자 뽑기.
    def next_number(self):
        if len(self.numbers) == 6:
            print('done')
            return

        if self.odd_count == self.odd_max:
            self.numbers.append(self.next_even(1, 45))
        elif self.even_count == self.even_max:
            self.numbers.append(self.next_odd(1, 45))
        else:
            self.numbers.append(self.next_odd(1, 45))

    # 랜덤 홀수 뽑기.
    def next_odd(self, start, end):
        ret = rand.randint(start, end)
        while ret % 2 != 0 or ret in self.numbers:
            ret = rand.randint(start, end)

        self.odd_count += 1
        return ret

    # 랜덤 짝수 뽑기.
    def next_even(self, start, end):
        ret = rand.randint(start, end)
        while ret % 2 != 1 or ret in self.numbers:
            ret = rand.randint(start, end)

        self.even_count += 1
        return ret

if __name__ == '__main__':
    main()
