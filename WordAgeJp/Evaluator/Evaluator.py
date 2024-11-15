from __future__ import annotations
from pathlib import Path
from WordAgeJp.Evaluator.EvaluationResult import EvaluationResult


class Evaluator:
    def __init__(self, data_path: Path = None) -> None:

        if data_path == None:
            self.data_path = (
                Path(__file__).parent.parent / "Assets" / "goi.csv"
            )

        self.ratings = self.get_ratings(self.data_path)

    def get_ratings(self, data_path: str) -> dict[str, int]:
        """
        prepare ratings dictionary for evaluation

        :param data_path: path to the csv file
        :return: dictionary of ratings. key: surface, value: rating
        """

        #read csv
        with open(data_path, "r", encoding="shift_jis") as f:
            lines_raw = f.read().splitlines()
        lines = []
        for line in lines_raw:
            lines.append(line.split(","))

        #surface -> rating
        ratings = {}
        for line in lines[1:]:
            # get only difficulty number
            ratings[line[1]] = int(line[3][0])

        return ratings

    def process(self, infinitives: list[str]) -> EvaluationResult:
        """
        receive surfaces data and process them
        """

        result = EvaluationResult()

        for infinitive in infinitives:
            if infinitive in self.ratings:
                rating = self.ratings[infinitive]
                result.ratings_count[rating] = result.ratings_count.get(rating, 0) + 1

        result.update()

        return result

if __name__ == "__main__":
    instance = Evaluator()