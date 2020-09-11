import matplotlib.pyplot as plt
import numpy as np


class line:
    def line1(self):
        if (12 + (column - 2) * 15) <= 42:
            print("=" * 42)
        else:
            print("=" * (12 + (column - 2) * 15))

    def line2(self):
        print("-" * 27)

    def line3(self):
        print("-" * 42)

    def line4(self):
        print("-" * (12 + (column - 2) * 15))

    def line5(self):
        if (12 + (column - 2) * 15) <= 42:
            print("-" * 42)
        else:
            print("-" * (12 + (column - 2) * 15))


def argand(complex_number):

    y = complex_number

    plt.style.use("seaborn-whitegrid")
    plt.plot(
        np.real(y),
        np.imag(y),
        "x",
        markersize=15,
        markeredgecolor=color,
        markeredgewidth=3,
    )
    plt.ylabel("Im(Roots) j")
    plt.xlabel("Re(Roots)")
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")


class rhsc:
    def calculation(self):

        print()
        print("  Routh Hurwitz Stability Criteria")
        print()

        coefficients = []
        coefficients = [
            int(item)
            for item in input(
                "  Enter the coefficients of the characteristic equation in descending order of s : \n\n  "
            ).split()
        ]

        order = len(coefficients) - 1
        polynomial = np.poly1d(coefficients, variable="s")
        roots = polynomial.r

        global color

        RHS = []
        LHS = []
        OIA = []

        for root in roots:
            if np.around(np.real(root), 3) > 0:
                RHS.append(root)
                color = "red"
                argand(root)
            elif np.around(np.real(root), 3) < 0:
                LHS.append(root)
                color = "green"
                argand(root)
            else:
                OIA.append(root)
                color = "blue"
                argand(root)

        matrix = []
        row1 = []
        row2 = []
        e = 0

        for coefficient in coefficients:

            if e % 2 == 0:
                row1.append(coefficient)
            else:
                row2.append(coefficient)

            e += 1

        global column

        if order % 2 == 0:
            column = (order + 6) // 2
            row1.extend([0, 0])
            row2.extend([0, 0, 0])
        else:
            column = (order + 5) // 2
            row1.extend([0, 0])
            row2.extend([0, 0])

        matrix.append(row1)
        matrix.append(row2)

        u = 12 + (column - 2) * 15

        if len(RHS) != 0:

            if order == 1:
                spaces = " " * ((42 - 27) // 2)
            elif order == 0:
                spaces = " " * ((42 - 27) // 2)
            else:
                spaces = " " * ((u - 27) // 2)

            y = "Hence, System is Unstable !"
            plt.title("Unstable System")

        elif len(OIA) != 0:

            if order == 1:
                spaces = " " * ((42 - 36) // 2)
            elif order == 0:
                spaces = " " * ((42 - 36) // 2)
            else:
                spaces = " " * ((u - 36) // 2)

            y = "Hence, System is Marginally Stable !"
            plt.title("Marginally Stable System")

        else:

            if order == 1:
                spaces = " " * ((42 - 25) // 2)
            elif order == 0:
                spaces = " " * ((42 - 25) // 2)
            else:
                spaces = " " * ((u - 25) // 2)

            y = "Hence, System is Stable !"
            plt.title("Stable System")

        for i in range(order - 1):

            row = []

            for j in range(column - 1):

                z = (
                    matrix[i][j + 1] * matrix[i + 1][0]
                    - matrix[i][0] * matrix[i + 1][j + 1]
                ) / matrix[i + 1][0]

                if np.around(z, 3) == 0:
                    z = 1e-30
                row.append(z)

            row.append(0)
            matrix.insert(abs(i + 2), row)

            s = 0

            for j in row:
                if int(j) == 0:
                    s += 1

            if s == column:

                matrix.pop(i + 2)
                t = []
                product = []

                for j in range(order - i - 1, -1, -2):
                    t.append(j)

                if len(t) != column:
                    for j in range(column - len(t)):
                        t.append(0)

                for n1, n2 in zip(matrix[i + 1], t):
                    product.append(n1 * n2)

                matrix.insert(i + 2, product)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        line.line1(u)
        print()
        print("  Characteristic Equation :")
        print()
        print(polynomial)
        print()
        print("  Roots  s :    Re(Roots) +    Im(Roots) j")
        print()
        line.line1(u)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        print("  Table  1 :")
        print()
        line.line2(u)
        print("| Location |    No. Roots |")
        line.line2(u)
        print("|      RHS | %12d " % len(RHS) + "|")
        print("|      LHS | %12d " % len(LHS) + "|")
        print("|      OIA | %12d " % len(OIA) + "|")
        line.line2(u)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        print("  Table  2 :")
        print()
        line.line3(u)
        print("| Location |    Re(Roots) |    Im(Roots) |")
        line.line3(u)

        if len(RHS) != 0:
            for root in RHS:
                print(
                    "|      RHS | %12.2f " % np.around(np.real(root), 2)
                    + "| %12.2f " % np.around(np.imag(root), 2)
                    + "|"
                )

        if len(LHS) != 0:
            for root in LHS:
                print(
                    "|      LHS | %12.2f " % np.around(np.real(root), 2)
                    + "| %12.2f " % np.around(np.imag(root), 2)
                    + "|"
                )

        if len(OIA) != 0:
            for root in OIA:
                print(
                    "|      OIA | % 12.2f " % np.around(np.real(root), 2)
                    + "| %12.2f " % np.around(np.imag(root), 2)
                    + "|"
                )
        line.line3(object)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        print("  Table  3 : RH Table")
        print()
        line.line4(object)
        print("| Equation ", end="|")

        for i in range(column - 2):
            print("    Column %2d " % (i + 1), end="|")

        print()
        line.line4(object)

        for i in matrix:

            print("|      s%2d " % order, end="| ")
            order -= 1

            for j in range(column - 2):

                if abs(int(i[j])) > 1e09:

                    if int(i[j]) / abs(int(i[j])) == 1:
                        print("    Positive", end=" | ")
                    else:
                        print("    Negative", end=" | ")

                else:
                    print("%12.2f" % i[j], end=" | ")

            print()

        line.line4(object)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        line.line3(object)
        print(
            "|                    Here |              |\n|         In first column |              |\n|  Number of sign changes : %2d           "
            % len(RHS)
            + "|"
        )
        line.line3(object)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        line.line3(object)
        print(
            "|                   Hence |              |\n|In right hand side plane |              |\n|         Number of roots : %2d           "
            % len(RHS)
            + "|"
        )
        line.line3(object)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        line.line5(object)
        print(spaces + y)
        line.line5(object)

        # --------------------------------------------------------------------------------------------------------------------------------------

        print()
        plt.show()

        # --------------------------------------------------------------------------------------------------------------------------------------


while True:
    rhsc.calculation(object)
