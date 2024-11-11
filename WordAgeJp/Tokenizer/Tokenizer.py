from MeCab import Tagger
from WordAgeJp.Tokenizer.TokenizedData import TokenizedData


class Tokenizer:
    """
    Tokenizing texts
    """

    def __init__(self) -> None:
        self.stopwords = set(["", "。", "、"])
        self.tagger = Tagger()

    def tokenize(self, text: str) -> TokenizedData:
        """
        Tokenize text
        """
        
        node = self.tagger.parseToNode(text)
        tokenized_data = TokenizedData()
        while node:
            surface = node.surface

            # skip stopwords
            if surface in self.stopwords:
                node = node.next
                continue

            tokenized_data.infinitives.append(surface)
            node = node.next

        return tokenized_data


if __name__ == "__main__":
    text = "私はPythonが好きです。"
    tokenized_data = Tokenizer().tokenize(text)
    print(tokenized_data.infinitives)
