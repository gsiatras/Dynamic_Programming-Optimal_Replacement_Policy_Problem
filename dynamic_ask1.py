import numpy as np

class Agent:
    def __init__(self, K, X, T):
        self.K = K                       # time horizon
        self.X = X                       # max age of machine
        self.T = T                       # cost of machine
        self.x = np.ones(K)              # array to store machines age
        self.V = np.zeros((K+1, X+1))    # dynamic programming array to store costs
        self.dec = np.zeros((K+1, X+1))  # array to store decision to keep or not at each step
        self.u = np.zeros(K)             # array to store optimal decisions
        self.c = np.zeros(K)          # array to store optimal costs

    def cost(self, x, k):
        return np.exp(-x)
    def phi2(self, x , k):
        return x**2
    def phi1(self, x, k):
        return self.T*np.sqrt(k) - self.cost(x, k)

    # function to calculate optimal policy
    def calculate(self):
        for k in range(self.K - 1, -1, -1):                         # iterate backwards for each time stem in K
            for j in range(1, min(self.X, k) + 1):                  # iterate through all the possible ages at time k
                if j == self.X:                                     # if we reach max age add the theta factor
                    theta = -self.cost(j, k)
                    Vkeep = self.phi2(j, k)
                    Vreplace = self.phi1(j, k) + self.V[k + 1, 1] + self.phi2(j, k)
                    self.V[k, j] = min(Vkeep, Vreplace)
                    self.dec[k, j] = int(Vreplace < Vkeep)
                else:
                    theta = 0
                    Vkeep = self.phi2(j, k) + self.V[k + 1, j + 1]  # choose between Vreplace and Vkeep
                    Vreplace = self.phi1(j, k) + self.V[k + 1, 1] + self.phi2(j, k)
                    if j >= self.X - 1 or Vreplace < Vkeep:
                        self.V[k, j] = Vreplace
                        self.dec[k, j] = 1
                    else:
                        self.V[k, j] = Vkeep
                        self.dec[k, j] = 0
        # print(self.V)
        # print(self.dec)

        # calculate the optimal decisions
        j = 0
        for i in range(0, self.K-1):
            if self.dec[i, j] == 0:
                j += 1
            else:
                j = 1
            self.u[i + 1] = self.dec[i + 1, j]
            self.c[i+1] = self.V[i+1, j]
        # print('Path:')
        # print(self.u)

        # calculate the age
        for i in range(0, self.K-1):
            self.x[i+1] = self.x[i]*(1-self.u[i]) + 1
        # print(self.x)
        self.printer()

    def printer(self):
        print('=================Optimal Policy For K=%d, X=%d, T=%d=================' %(self.K, self.X, self.T))
        print('Time:\t Decision:\t Age:\t Cost:')
        for i in range(0, self.K):
            print('%d\t\t %d\t\t\t %d\t\t %d' % (i, self.u[i], self.x[i], self.c[i]))



def menu():
    K = int(input('Time Horizon: '))
    X = int(input('Maximum age of machine: '))
    T = int(input('Cost of the machine: '))
    return K, X, T


if __name__ == '__main__':
        K, X, T = menu()
        agent = Agent(K, X, T)
        agent.calculate()






