import numpy as np

class ScoreManager:
    def __init__(self, scores):
        self.data = np.array(scores)

    def get_total(self):
        return np.sum(self.data)
    
    def get_average(self):
        return np.average(self.data)
    
    def get_above(self, cutoff):
        return [int(score) for score in self.data if score > cutoff]
    
scores = [72, 88, 95, 61, 84, 77]
s1 = ScoreManager(scores)
print(f"합계: {s1.get_total()}")
print(f"평균: {s1.get_average():.1f}")
print(f"80점 초과: {s1.get_above(80)}")
    