import numpy as np

class Agent:
    def __init__(self, K, X, T):
        self.K = K
        self.X = X
        self.T = T
        self.x = np.ones(K + 1)
        self.V = np.zeros((K+1, X+1))
        self.dec = np.zeros((K+1, X+1))
        self.u = np.zeros(K)

    def cost(self, k, x):
        return np.exp(-x)
    def phi2(self, x , k):
        return x**2
    def phi1(self, x, k):
        return self.T*np.sqrt(k) - self.cost(k, x)


    #  function to calculate sortest path
    def calculate(self):
        for k in range(self.K-1, -1, -1):
            for j in range(1, min(self.X, k+1)):
                if j == self.X:
                    theta = self.cost(j, k)
                else:
                    theta = 0
                Vkeep = self.phi2(j, k) + self.V[k+1, j+1]
                Vreplace = self.phi1(j, k) + self.V[k+1, 1]
                if Vkeep < Vreplace:
                    self.V[k,j] = Vkeep
                    self.dec[k,j] = 0
                else:
                    self.V[k,j] = Vreplace
                    self.dec[k,j] = 1
            # Vmin = np.argmin(self.V[:, k])
            # self.u[k] = self.dec[Vmin, k]
        print(self.u)
        # for i in range(0, self.K-1):
        #     if self.u[i] == 0:
        #         self.u[i+1] = self.dec[i+1][i+1]
        #     else:
        #         self.u[i+1] = self.dec[i+1, 1]
        print(self.V)
        print(self.dec)
        print(self.u)



def menu():
    K = int(input('Time Horizon :'))
    X = int(input('Maximum age of machine :'))
    T = int(input('Cost of the machine'))
    return K, X, T



if __name__ == '__main__':
        # K, X, T = menu()
        agent = Agent(5, 4, 10)
        agent.calculate()






