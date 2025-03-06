import pickle
from pathlib import Path
import streamlit_authenticator as sauth

names = ["Atharva Herekar", "Kartavya Gore", "Neeraj Gaikwad"]
usernames = ["athrv", "krtvya", "nrj"]
passwords = ["apass","kpass","npass"]

#   Using bcrypt hashing
hashed_passwords = sauth.Hasher(passwords).generate() 



file_path = Path(__file__).parent / "hashed_pw.pkl"
with open(file_path, "wb") as f:
    pickle.dump(hashed_passwords, f)
