# Команда для установки зависимостей и синхронизации пакета
install:
	uv sync

# Команда для проверки качества кода
init:
	uv run ruff check brain_games

# Команда для запуска программы
brain-games:
	uv run brain-games

# Команда для запуска отдельно brain_even
brain-even:
	uv run brain-even

# Команда для запуска отдельно brain_calc
brain-calc:
	uv run brain-calc

# Команда для запуска отдельно brain_gcd
brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

# Команда для сборки пакета
build:
	uv build

# Команда для установки собранного пакета в систему
package-install:
	uv tool install --force dist/*.whl