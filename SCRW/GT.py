import pickle, os, re

def load(path):
    with open('data/'+path, "rb") as f:
        r = pickle.load(f)
        return [i['id'] for i in r]

paths = [j.group() for j in [re.search(r'\d{5}X', i) for i in os.listdir("./data")] if j]
GT = []
for path in paths:
    res = load(path)
    print path,
    GT += res
    print len(res)

print len(GT),'\nsaving ...'
with open("data/GT", 'wr') as f:
    pickle.dump(GT, f, protocol=pickle.HIGHEST_PROTOCOL)

print "DONE"
