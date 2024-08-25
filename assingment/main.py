import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

import math

import os


class Tarea_Python:
    def __init__(self) -> None:
        self.ruta_archivo = os.getcwd()

    def __s1_punto_1(self, n: int) -> float:
        """

        n: numero en el que se quiere evaluar la serie matematica

        """

        s1 = lambda x: ((-1) ** x) * np.tanh(x)

        return sum([s1(i) for i in range(1, n)])

    def __s2_punto_1(self, n: int) -> float:
        """

        n: numero en el que se quiere evaluar la serie matematica

        """

        s2 = lambda x: ((np.arctan(x) ** 2) / ((x**2) + 1))

        return sum([s2(i) for i in range(1, n)])

    def __s3_punto_1(self, n: int) -> float:
        """

        n: numero en el que se quiere evaluar la serie matematica

        """

        s3 = lambda x: math.log(math.factorial(x), x) / (x**3)

        return sum([s3(i) for i in range(2, n)])

    def __s4_punto_2(self, n: int, theta: float) -> float:
        """

        n: numero en el que se quiere evaluar la serie matematica

        """

        s1 = lambda x, y: round((((-1) ** x) / math.factorial((2 * x) + 1)), 20) * (
            y ** ((2 * x) + 1)
        )

        return sum([s1(i, theta) for i in range(n)])

    def __grafico_series(
        self, s: list, numero_serie: int, leyenda: list = None
    ) -> None:
        """

        n: numero en el que se quiere evaluar la serie matematica

        serie: numero del 1 al 3 que hace refencia a cual de las series disponibles quiere evaluar

        """

        for serie in range(len(s)):
            if leyenda is not None:
                plt.plot(s[serie], label=leyenda[serie])

                plt.legend(
                    loc="upper center",
                    bbox_to_anchor=(0.5, -0.05),
                    fancybox=True,
                    shadow=True,
                    ncol=5,
                )

            else:
                plt.plot(s[serie])

        plt.title(f"Grafico serie {numero_serie}")

        plt.savefig(
            os.path.join(self.ruta_archivo, "assingment", f"serie {numero_serie}.png")
        )

        plt.clf()

    def punto_1(self, serie: int, n: int) -> float:
        """

        n: numero en el que se quiere evaluar la serie matematica

        serie: numero del 1 al 3 que hace refencia a cual de las series disponibles quiere evaluar

        """

        if serie == 1:
            s = [self.__s1_punto_1(i) for i in range(1, n)]

        elif serie == 2:
            s = [self.__s2_punto_1(i) for i in range(1, n)]

        elif serie == 3:
            s = [self.__s3_punto_1(i) for i in range(2, n)]

        self.__grafico_series([s], serie)

        if serie == 1:
            print(f"La serie 1 es periodica, por lo tanto no tiene convergencia")

        else:
            print(f"El resultado de la serie {serie} en {n=} es s={round(s[-1],4)}")

        return round(s[-1])

    def punto_2(self, n: int):
        """

        n: numero de valores de la funcion sen(x) y su serie equivalente

        """

        serie = [
            self.__s4_punto_2(150, (i * (np.pi / 180)) % (2 * np.pi))
            for i in range(0, n)
        ]

        seno = [np.sin(i * (np.pi / 180)) for i in range(0, n)]

        self.__grafico_series(
            [serie, seno], 4, ["Serie matematica", "Funcion matematica de Numpy"]
        )

        # self.__grafico_series([serie], 4, ["Funcion matematica de Numpy"])

        print(
            f"suma de un periodo [0,2*pi] de la serie matematica de la funcion Seno: {sum(serie)}, \nsuma de un periodo [0,2*pi] de la serie de Seno de numpy= {sum(seno)}"
        )

    def punto_3(self) -> None:
        df = pd.read_csv(
            "/workspaces/assingment-python-ederperez95/assingment/data.csv",
            sep="\t",
            header=None,
        )

        print(f"La suma de la segunda comulna es: {df.iloc[:,1].sum()}")

        df["letras"] = df.loc[:, 0]

        agrupadores_1 = df.groupby(by=[0]).count().letras

        agrupadores_1 = [
            str(i) + ", " + str(agrupadores_1.loc[i]) for i in agrupadores_1.index
        ]

        agrupadores_2 = df.groupby(by=[0]).sum().loc[:, 1]

        agrupadores_2 = [
            str(i) + ", " + str(agrupadores_2.loc[i]) for i in agrupadores_2.index
        ]

        print(f"\nEl conteo de la primera columna por letra es:")

        for i in agrupadores_1:
            print(i)

        print(f"\nLa suma de la segunda columna por letra es:")

        for i in agrupadores_2:
            print(i)


def main():
    Objeto_Tarea = Tarea_Python()

    print("\nAcontinuacion se presenta el resultado del punto 1")

    punto_1a = Objeto_Tarea.punto_1(1, 30)

    punto_1b = Objeto_Tarea.punto_1(2, 1000)

    punto_1c = Objeto_Tarea.punto_1(3, 1000)

    print("\nAcontinuacion se presenta el resultado del punto 2")

    punto_2 = Objeto_Tarea.punto_2(360)

    print("\nAcontinuacion se presenta el resultado del punto 3")

    punto_3 = Objeto_Tarea.punto_3()


if __name__ == "__main__":
    main()
