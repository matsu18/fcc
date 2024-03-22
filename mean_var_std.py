import numpy as np

def calculate(list):
    try: 
        arr = np.array(list)
        arr.shape
        arr = arr.reshape(3,3)
        calculations = {}
        calculations["mean"] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()]
        calculations["variance"] = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var()]
        calculations["standard deviation"] = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std()]
        calculations["max"] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()]
        calculations["min"] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()]
        calculations["sum"] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()]
        return calculations
    except Exception:
        raise ValueError('List must contain nine numbers.')


    