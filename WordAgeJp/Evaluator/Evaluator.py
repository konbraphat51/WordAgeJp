from __future__ import annotations
from pathlib import Path

class Evaluator:
    def __init__(self,
                 data_path: Path = None
                 ) -> None:
        
        if data_path == None:
            self.data_path = Path(__file__).parent.parent / "Assets" / "goi.csv"

        self.prepare_dictionary(self.data_path)        

    def prepare_dictionary(self, data_path: str) -> None:
        """
        prepare dictionary for evaluation
        """
        

    def process(self, surfaces: list[str]) -> None:
        """
        receive surfaces data and process them
        """

