import pandas as pd
import pickle

fname = 'triplets_1000.txt'
fnames = fname[:-4]

user_profiles = pd.read_csv(fname, sep='\t', names = ['userID','songID', 'play_count'])

user_profiles = user_profiles.pivot(index='userID', columns='songID', values='play_count')
user_profiles = user_profiles.fillna(0)
user_profiles = user_profiles.astype(pd.SparseDtype("int", 0))

with open(f"user_profiles_{fnames}.pkl", "wb") as f:
    pickle.dump(user_profiles, f)
