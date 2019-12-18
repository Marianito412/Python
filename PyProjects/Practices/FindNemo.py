string = "Here is the greatest Nemo fish in the world"
def Find(st):
    return st.split().index("Nemo")+1
print(Find(string))
