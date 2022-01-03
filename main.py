import numpy as np
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('This is a log message.')


def dp_variabel(var):
    logging.info(f"{var = }")


def rot_x(w):
    theta = np.radians(w)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((1, 0, 0),
                  (0, c, -s),
                  (0, c, s)))
    return R


def set_up_3d():
    ax.set_xlabel('x')
    plt.quiver(0,0,0,1,0,0,color="red")
    ax.set_ylabel('y')
    plt.quiver(0,0,0,0,1,0,color="green")
    ax.set_zlabel('z')
    plt.quiver(0,0,0,0,0,1,color="blue")
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1);
    plt.show()

def add_arrow(a,b):
    plt.quiver(a[0],a[1],a[2],b[0],b[1],b[2],color="black")

if __name__ == '__main__':
    print("start")
    ax = plt.figure().add_subplot(projection='3d')
    n = np.array([0,0,0])
    a = np.array([1,1,0])
    add_arrow(a,-a)
    b = np.array([4,5,6])
    aDOTb = np.dot(a,b)
    dp_variabel(aDOTb)

    aCROSSb = np.cross(a,b)
    dp_variabel(aCROSSb)

    ea = a / np.linalg.norm(a)
    dp_variabel(ea)

    ROTa = np.matmul(rot_x(90), a)
    dp_variabel(ROTa)

    set_up_3d()

