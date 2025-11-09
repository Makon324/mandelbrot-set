import numpy as np
import matplotlib.pyplot as plt
import argparse


X_MIN = -2
X_MAX = 2
Y_MIN = -2
Y_MAX = 2


def mandelbrot_iterate(c: complex, max_iter: int) -> int:
    """Mandelbrot iteration function - returns number of iterations to escape range 2 circle."""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter


def mandelbrot_set(width: int, height: int, max_iter: int) -> np.array:
    """Generate mandelbrot set using mandelbrot_iterate for each point."""
    x_linspace = np.linspace(X_MIN, X_MAX, width)
    y_linspace = np.linspace(Y_MIN, Y_MAX, height)
    mset = np.zeros([height, width])

    for x in range(width):
        for y in range(height):
            c = complex(x_linspace[x], y_linspace[y])
            mset[y][x] = mandelbrot_iterate(c, max_iter)

    return mset


def visualize(mset: np.array) -> None:
    """Visualize mandelbrot set using matplotlib."""
    plt.imshow(mset, extent=(X_MIN, X_MAX, Y_MIN, Y_MAX), cmap="hot", origin="lower")

    plt.colorbar()
    plt.title("Mandelbrot Set Visualization")
    plt.xlabel("Re(x)")
    plt.ylabel("Re(y)")

    plt.show()


def parse_args():
    p = argparse.ArgumentParser(description="Mandelbrot set visualizer (square image).")
    p.add_argument(
        "--size",
        "-s",
        type=int,
        default=2048,
        help="Image width and height in pixels (width = height). Default: %(default)s",
    )
    p.add_argument(
        "--max-iter",
        "-m",
        type=int,
        default=128,
        help="Maximum iterations for escape. Higher -> more detail (slower). Default: %(default)s",
    )
    return p.parse_args()


def main():
    args = parse_args()

    mset = mandelbrot_set(args.size, args.size, args.max_iter)

    visualize(mset)


if __name__ == "__main__":
    main()
