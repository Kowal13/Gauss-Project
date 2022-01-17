import matplotlib.pyplot as plt

plt.ion()


def score_plot(score, iteration):
    plt.clf()
    if len(score) == 1:
        plt.scatter(iteration, score)
    else:
        plt.plot(iteration, score)
    plt.ylabel("Score")
    plt.xlabel("Iteration")
    plt.show()
    plt.pause(.1)
