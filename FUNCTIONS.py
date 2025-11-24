import numpy as np

N = 100
m, q = [0.7, 3]

noise = np.random.normal(0, 1, N)
x1 = np.linspace(0, 10, N) # FEATURE
line = lambda x, m, q: m*x + q
y_gt = line(x1, m, q) # GROUND TRUTH
y = y_gt + noise # MEASURED SIGNAL
loss = lambda yhat: 1/N*np.sum(np.power(y - yhat, 2)) # MSE

def gradient(X, y, lr = 1e-3, steps = 15000):
	werr = [0] * steps
	w = np.array([0, 0])
	for i in range(len(werr)):
		step = lr * 2 / N*X.T@(X@w - y)
		w = w - step
		werr[i] = loss(line(x1,*w))
	return w, werr