# Бот загадывает число от 1 до 100 (сообщить об этом пользователю). Запрашивать от пользователя число до тех пор, пока оно не будет равно числу, которое загадал бот. Если число пользователя меньше или больше загаданного, то сообщить об этом пользователю. В конце поблагодарить пользователя за игру.
# После правильного ответа спросить пользователя, хочет ли он продолжить играть или нет. Если да, то бот загадывает новое число, иначе завершить игру.
# Создать игровой объект Player с свойствами «имя» и «счет». Реализовать регистрацию участников. Запросить количество участников и заполнить список игроками. В игре реализовать поочередное отгадывание числа. Если игрок угадает число, то его рейтинг увеличивается на N очков. Далее спросить каждого игрока, хочет ли он продолжить играть. Если кто-то не хочет, то завершить игру.
from player import Player
import random
if __name__ == "__main__":
    wanna_play = True
    while wanna_play:
        bot_number = random.randrange(1, 100)
        print("Бот задал число")
        while True:
            user_number = int(input("Введите ваше число: "))
            if bot_number > user_number:
                print("Ваше число меньше")
            elif user_number > bot_number:
                print("Ваше число больше")
            else:
                print("Отгадано правильно! Спасибо за игру!")
                wanna_play = True if input(
                    "Вы хотите играть дальше? (Да/нет)?").lower() == "да" else False
                break
