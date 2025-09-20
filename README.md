⚙️ Setup Instructions
1. Clone repo
git clone <your-api-repo-url>
cd home-test-api

2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Running Tests
Run all API tests
python -m pytest tests/api -v

Run a single test file
python -m pytest tests/api/test_pokeapi.py -v

Generate HTML report
python -m pytest --html=report.html --self-contained-html -v

| Test ID | Endpoint                | Input           | Expected Status | Validations                                                                         |
| ------- | ----------------------- | --------------- | --------------- | ----------------------------------------------------------------------------------- |
| 1       | `/pokemon/{name}`       | `pikachu`       | 200             | Schema: `name`, `abilities` <br> Value: `name == pikachu`, ability `static` present |
| 2       | `/pokemon/{id}`         | `1` (Bulbasaur) | 200             | Schema: `name`, `abilities` <br> Value: `name == bulbasaur`                         |
| 3       | `/pokemon/{name}`       | `not-a-pokemon` | 404             | Negative case – invalid Pokémon returns 404                                         |
| 4       | `/pokemon-species/{id}` | `25` (Pikachu)  | 200             | Schema: `names` list exists <br> Value: English names include `Pikachu`             |

