class EvaluationResult:
    def __init__(self) -> None:
        self.ratings_count: dict[int, int] = {}
        self.ratings: dict[int, float] = {}

    def update(self) -> None:
        """
        update calculations of all properties
        """
        self._ratings()

    def _ratings(self) -> None:
        """
        calculate ratings
        """
        total = sum(self.ratings_count.values())

        for surface, count in self.ratings_count.items():
            self.ratings[surface] = count / total