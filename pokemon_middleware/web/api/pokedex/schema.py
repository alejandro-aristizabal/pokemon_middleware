from pydantic import BaseModel


class DataResource(BaseModel):
    """Pokemon name model."""

    pokemon_name: str


class PokemonId(BaseModel):
    """Pokemon id model."""

    pokemon_id: int
