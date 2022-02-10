       
    def play_1round(self):
        player_action = dealer_action = "Hit"
        while player_action=="Hit":
            player_action = self.player.player_decide(self.get_game_state())
            if player_action=="Hit": self.player.hand.append(self.cards.get_card())
        while dealer_action == "Hit":
            dealer_action = self.dealer.dealer_decide()
            if dealer_action=="Hit": self.dealer.hand.append(self.cards.get_card())
