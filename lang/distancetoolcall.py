from typing_extensions import Annotated, TypedDict

class SPA(TypedDict):
    """Quand la discussion tourne autours des spas
    answer is the answer you would give
    """
    answer : Annotated[str, ..., "answer you would give"]
    
class CRY(TypedDict):
    """to use absolutely if you don't have any data, it's the best choice if you don't have anything labeled data
    """
    answer : Annotated[str, ..., "answer you would give"]

class TOURISME(TypedDict):
    """Si on parle de visiter autours de l'hotel
    answer is the answer you would give
    """
    answer : Annotated[str, ..., "answer you would give"]

class CUISINE(TypedDict):
    """Si on parle de restaurant ou de gastronomie
    answer is the answer you would give
    """
    answer : Annotated[str, ..., "answer you would give"]



endpoint = [CUISINE, SPA, TOURISME, CRY]