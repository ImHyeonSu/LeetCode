import collections
from typing import List, re


class gg():
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph)
            .lower().split()
                    if word not in banned]
        print(words)
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


     