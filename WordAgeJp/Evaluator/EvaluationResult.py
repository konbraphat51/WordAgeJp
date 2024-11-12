from __future__ import annotations
import matplotlib.pyplot as plt

class EvaluationResult:
    def __init__(self) -> None:
        self.ratings_count: dict[int, int] = {}
        self.ratings: dict[int, float] = {}

    def update(self) -> None:
        """
        update calculations of all properties
        """
        self._update_ratings()

    def plot_ratio(results: list[EvaluationResult]) -> None:
        """
        plot several rating ratio bar in a single graph
        """

        # create stacked bar chart
        x = [cnt for cnt in range(len(results))]
        y_sum = [0.0]*len(results)
        for rating in range(1, 7):
            y = [result.ratings[rating] for result in results]
            plt.bar(x, y, bottom=y_sum, width=0.4)
            y_sum = [y_sum[cnt] + y[cnt] for cnt in range(len(results))]
        plt.tight_layout()
        plt.show()


    def _update_ratings(self) -> None:
        """
        calculate ratings
        """
        total = sum(self.ratings_count.values())

        for surface, count in self.ratings_count.items():
            self.ratings[surface] = count / total