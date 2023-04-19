from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


"""
    For PlayingCard to use this sort index for comparisons, we need to add a field .sort_index to the class. 
    However, this field should be calculated from the other fields .rank and .suit automatically. 
    This is exactly what the special method .__post_init__() is for. 
    It allows for special processing after the regular .__init__() method is called.
    
    Note that .sort_index is added as the first field of the class. 
    That way, the comparison is first done using .sort_index and only if there are ties are the other fields used.
"""


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f"{self.suit}{self.rank}"


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    """
        Note the !s specifier in the {c!s} format string. It means that we explicitly want to 
        use the str() representation of each PlayingCard. With the new .__repr__(), 
        the representation of Deck is easier on the eyes
    """

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


print(PlayingCard("A", "♠"))
print(Deck())


"""
    Be aware though that if your data class contains mutable fields, those might still change. 
    This is true for all nested data structures in Python.
    Even though both ImmutableCard and ImmutableDeck are immutable, 
    the list holding cards is not. You can therefore still change the cards in the deck:
"""


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str


@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]
