class Matriz(object):

    def matrix(self):
        matriz = [[0 for col in range(10)] for row in range(10)]
        for i in range(10):
            matriz[i][i]=1
        return matriz

if __name__ == '__main__':
    pass
