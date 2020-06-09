skor_computer = 0
skor_pemain = 0

rps = ['rock','paper','scissors']
comp_choice = random.randint(0,2)
player_choice = input('rock,paper,scisors?')
player_choice = player_choice.lower()

def check menang(computer_choice, player_choice):
    if