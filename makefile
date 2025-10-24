# Команда для установки зависимостей и синхронизации пакета
install:
	uv sync

# Команда для проверки качества кода
init:
	uv run ruff check brain_games

# Команда для запуска программы
brain-games:
	uv run brain_games

# Команда для сборки пакета
build:
	uv build

# Команда для установки собранного пакета в систему
package-install:
	uv tool install dist/*.whl
