import requests, pytest

BASE = "https://pokeapi.co/api/v2"

@pytest.mark.parametrize("name_or_id,expected_code,expected_name,expected_ability", [
    ("pikachu", 200, "pikachu", "static"),
    ("1", 200, "bulbasaur", None),
    ("not-a-pokemon", 404, None, None)
])
def test_get_pokemon_status_and_basic_fields(name_or_id, expected_code, expected_name, expected_ability):
    r = requests.get(f"{BASE}/pokemon/{name_or_id}")
    assert r.status_code == expected_code

    if expected_code == 200:
        data = r.json()
        # Schema check
        assert "name" in data
        assert "abilities" in data

        # Value check
        assert data["name"] == expected_name
        if expected_ability:  # only check if provided
            assert any(a["ability"]["name"] == expected_ability for a in data["abilities"])

def test_pokemon_species_has_expected_fields():
    r = requests.get(f"{BASE}/pokemon-species/25")  # Pikachu species
    assert r.status_code == 200
    j = r.json()
    assert "names" in j and isinstance(j["names"], list)
    # Example value check
    english_names = [n["name"] for n in j["names"] if n["language"]["name"] == "en"]
    assert "Pikachu" in english_names
