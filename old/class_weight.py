target = np.load('target.npy')
database = np.load('database.npy')

class_count = [0]*11

for idx in range(len(database)):
    class_count[target[idx]] += 1

class_weight_dict = {}
class_weights = np.array(class_count).astype(float)/sum(class_count)
for idx in range(len(class_count)):
    class_weight_dict[idx]=class_weights[idx]
