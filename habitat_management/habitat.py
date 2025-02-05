from typing import Any, List, Optional

from wildlife_tracker.animal_management.animal import Animal

class Habitat:

    def __init__(self,
                habitat_id: int,
                geographic_area: str,
                size: int,
                environment_type: str,
                animals: Optional[List[int]] = None) -> None:
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        # this is Pythonic for
        # if animals is not None:
        #   self.animals = animals
        # else:
        #   self.animals = []
        self.animals = animals or []

    def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
        pass

    def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
        pass

    def get_animals_in_habitat(self) -> List[Animal]:
        pass

