class Players:
    def __init__(self, player_name, position):
        self.player_name = player_name
        self.position = position
        
    def name_info(self):
        print(f'dane pilkarza: {self.player_name}')
        
    def position_info(self):
        print(f'pozycja na boisku: {self.position}')

    def text_info(self):
        print('chcesz wyszukac innego zawodnika lub klub?')
       
       
class Clubs(Players):
    def __init__(self, club_name, player_name, position):
        super().__init__(player_name, position)
        self.club_name = club_name

    def players_info(self):
        print(f'klub to: {self.club_name}, pilkarz to: {self.player_name}, rola to: {self.position}')

    def text_info(self):
        super().text_info()
        
        
club_info1 = Clubs('fc barcelona', 'leo messi', 'pomocnik')
club_info1.players_info()
club_info1.text_info()

club_info2 = Clubs('psg', 'neymar', 'napastnik')
club_info2.players_info()
club_info2.text_info()

player_info_1 = Players('ronaldo', 'napastnik')
player_info_1.name_info()
player_info_1.position_info()
player_info_1.text_info()
    