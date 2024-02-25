if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    print ([[i,j,k] for i in range(0,x + 1,x) for j in range(0,y + 1,y) for k in range(0,z+1,z) ])