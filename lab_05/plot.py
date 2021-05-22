import matplotlib.pyplot as plt
import settings

def get_label(n, m, md1, md2) -> str:
    return f'N, M, Методы: ({n} : {m} : {md1}-{md2})'


def plot(values, all_n, all_m, methods1, methods2):

    plt.clf()

    plt.xlabel("Tao")
    plt.ylabel("Eps(Tao)")
    plt.grid(which='minor', color='k', linestyle=':')
    plt.grid(which='major', color='k')

    for i in range(len(values)):
        x, y = [], []
        j = settings.TAU_START
        while j < settings.TAU_END:
            x.append(j)
            y.append(values[i](j))
            j += settings.TAU_STEP

        plt.plot(x, y, label=get_label(all_n[i], all_m[i], methods1[i], methods2[i]))

    plt.legend()
    plt.savefig('points.png')
    plt.show()