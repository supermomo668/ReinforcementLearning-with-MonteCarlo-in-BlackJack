class cards:
    def __init__(self):
        # Initialize deck condition: finite/infinite deck?
        pass ...
            
    def get_card(self):
        card = random.choices(list(self.card_probs.keys()), 
                              weights=self.card_probs.values(), k=1)[0]
        self.num_cards[card] -= 1; self.tot_cards -= 1
        if self.tot_cards == 0: 
            print("Out of cards! Restocking..."); self.stock_cards()
        self.update_card_prob()
        return card
    
    def starting_hand(self):
        return [self.get_card() for i in range(2)]