import numpy as np
import pandas as pd
import itertools

#Define state space and probabilities
states =['sleeping','eating','pooping']
hidden_states=['healthy','sick']
pi=[0.5,0.5]

#Initial state distribution
state_space=pd.Series(pi,index=hidden_states,name='states')
print("Initial Probabilities:\n",state_space,"\n")

#Transition probabilities(hidden->hidden)
a_df=pd.DataFrame(columns=hidden_states,index=hidden_states)
a_df.loc['healthy']=[0.7,0.3]
a_df.loc['sick']=[0.4,0.6]
print("Transition Probabilities:\n",a_df,"\n")

#Emission probabilities
b_df=pd.DataFrame(columns=states,index=hidden_states)
b_df.loc['healthy']=[0.2,0.6,0.2]
b_df.loc['sick']=[0.4,0.1,0.5]
print("Emission Probabilities:\n",b_df,"\n")

def forward_algorithm(obs_seq,a_df,b_df,pi,hidden_states):
    total_prob=0
    all_state_path=list(itertools.product(hidden_states,repeat=len(obs_seq)))

    for path in all_state_path:
        prob=pi[hidden_states.index(path[0])]*b_df.loc[path[0],obs_seq[0]]
        for t in range(1,len(obs_seq)):
            prev_state=path[t-1]
            curr_state=path[t]
            prob*=a_df.loc[prev_state,curr_state]*b_df.loc[curr_state,obs_seq[t]]
        total_prob+=prob
    return total_prob
def viterbi_algorithm(obs_seq,a_def,b_df,pi,hidden_states):
    max_prob=0
    best_path=None
    all_state_paths=list(itertools.product(hidden_states,repeat=len(obs_seq)))

    for path in all_state_paths:
        prob=pi[hidden_states.index(path[0])]*b_df.loc[path[0],obs_seq[0]]
        for t in range(1,len(obs_seq)):
            prev_state=path[t-1]
            curr_state=path[t]
            prob*=a_df.loc[prev_state,curr_state]*b_df.loc[curr_state,obs_seq[t]]
        if prob>max_prob:
            max_prob=prob
            best_path=path
    return max_prob,best_path

obsq=['pooping','pooping','pooping']

print("Forward(total probability):",forward_algorithm(obsq,a_df,b_df,pi,hidden_states))
v_prob,v_path=viterbi_algorithm(obsq,a_df,b_df,pi,hidden_states)
print("Viterbi(most probable state(path):",v_path)
print("Viterbi probability:",v_prob)
