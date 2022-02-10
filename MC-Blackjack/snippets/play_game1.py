class game():
    def __init__(self, cards, dealer, player):
        self.cards = cards()
        self.dealer = dealer
        self.player = player
        self.reward = {'win':1, 'lose':-1, 'push':0}
 
    def win_or_lose(self):  # Rule of the game
        dealer_handsum = sum(self.dealer.hand)
        player_handsum = sum(self.player.hand)
        print("Player:",player_handsum, "Dealer:",dealer_handsum)
        if player_handsum > 21:  # Player busted
            if dealer_handsum > 21: return self.reward['push']
            else: return self.reward['lose']
        else:   # Player not busted
            if player_handsum == 21 or len(self.player.hand) >= 5:  # Special ocassion (bj & charles 5)
                if dealer_handsum == 21: return self.reward['push']
                else: return self.reward['win']
            else:  
            # Normal rules
                # Bust
                if dealer_handsum > 21: return self.reward['win']
                else:
                # Under 21 compare
                    if player_handsum <= dealer_handsum: return self.reward['lose']
                    else: return self.reward['win']