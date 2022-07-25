from collections.abc import Generator, Iterable, Sequence
import random
import numpy as np


class SimpleMarkovChain:
    def __init__(self, N: int) -> None:
        self.__n = N
        self.BOC = N    # Begin of Chain
        self.EOC = N+1  # End of Chain
        self.__weights = np.zeros(shape=(N+2, N+2), dtype=np.uint32)

    def fit(self, X: Iterable[Sequence[int]]):
        for x in X:
            self.__weights[self.BOC, x[0]] += 1
            for i in range(1, len(x)):
                self.__weights[x[i-1], x[i]] += 1
            self.__weights[x[-1], self.EOC] += 1

    def generate(self, start: int = None) -> Generator[int, None, None]:
        state = self.BOC if start == None else start
        while True:
            # 何こいつキモ
            nstate, *_ = random.choices(range(self.__n+2),
                                        weights=self.__weights[state], k=1)
            if nstate == self.EOC:
                return
            else:
                yield nstate
            state = nstate
