from typing import Any, Optional


class Animal:
    def __init__(self, animal_id: int, species: str, age: Optional[int] = None, health_status: Optional[str] = None, current_location: Optional[str] = None):
        self.animal_id: int
        self.species: str
        self.age: Optional[int] = None
        self.health_status: Optional[str] = None
        self.current_location: str

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

    
    