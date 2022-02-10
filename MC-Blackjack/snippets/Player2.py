    def learn(self, reward):
        ''' Core function that allows learner to update '''
        self.update_rewards(reward)
        self.update_values()
        self.update_policy()
        self.game_states = []   # finish episode
    
    def update_rewards(self, reward, gamma = 0.2):
        '''Save rewards to states occurred during the game:
        Method: 1 Step Forward
        gamma: discount factor '''
        reward_1step = [reward]
        if not len(self.game_states)>0: print("No game states"); return
        if self.debug: print(self.game_states)
        for n in range(len(self.game_states)-1):  # Loop for each step 
            state, action = self.game_states[n]
            next_state, _ = self.game_states[n+1]
            next_state_rewards = []
            [next_state_rewards+i for i in list(self.rewards[next_state].values())]
            reward_1step += map(lambda x:self.gamma*x, next_state_rewards)
            self.rewards[state][action] = self.rewards[state][action] + reward_1step
        # Last step
        if len(self.game_states)>0: 
            state, action = self.game_states[-1]
            self.rewards[state][action] = self.rewards[state][action] + [reward]
        
    def update_values(self):
        for s, sa in self.rewards.items():
            for action, rewards in sa.items():  # Iterate state-action pairs
                ## Update with the mean of all rewards for this state-action pair
                if len(rewards) != 0: 
                    # Update value with Mean of reward
                    self.values[s][action] = np.mean(rewards)  
        
    def update_policy(self):
        '''Update policy based on state-value pair'''
        def e_soft_policy_update(state, policy_SA):
            '''action_value: action-values Inner dictionary for each state'''
            action_values = self.values[state]
            # Determine optimal action by get max value action
            greedy_action = max(action_values, key=action_values.get)
            # Number of times the action has been taken
            A_taken_greedy = len(self.rewards[state][greedy_action])
            A_taken_nongreedy = len(np.array(list({k:v for k,v in self.rewards[state].items()
                                     if k!=greedy_action}.values())).ravel())
            for a in action_values.keys():  # loop over available actions
                if a == greedy_action:
                    policy_SA[a] = 1-self.epsilon+(self.epsilon/(A_taken_greedy+1))
                else: policy_SA[a] = self.epsilon/(A_taken_nongreedy+1)
                #print(policy_SA[a])
        ### Update Policy /state-action
        for s, a in self.policy.items():
            e_soft_policy_update(s,a)