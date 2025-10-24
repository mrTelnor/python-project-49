# Синхронизация проекта и установка зависимостей
make install

uv sync
Resolved 3 packages in 5ms
Audited 3 packages in 12ms

# Проверка качества кода
make init

uv run ruff check brain_games
All checks passed!
# (если ошибки есть, они выводятся здесь)

# Сборка пакета
make build

uv build
Building source distribution...
Building wheel from source distribution...
Successfully built dist/python_project_49-0.1.1.tar.gz
Successfully built dist/python_project_49-0.1.1-py3-none-any.whl

# Установка пакета в систему
make package-install

uv tool install --force dist/*.whl
Resolved 2 packages in 11ms
Prepared 1 package in 17ms
Uninstalled 1 package in 0.67ms
Installed 1 package in 3ms
 ~ python-project-49==0.1.1 (from file:///mnt/d/Python/Hexlet/python-project-49/dist/python_project_49-0.1.1-py3-none-any.whl)
Installed 2 executables: brain-even, brain-games

# Запуск основной игры
brain-games

Welcome to the Brain Games!
May I have your name? Kit
Hello, Kit!

# Запуск игры проверки чётности
brain-even

Welcome to the Brain Games!
May I have your name? Kit
Hello, Kit!
Answer "yes" if the number is even, otherwise answer "no".
Question: 31
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Kit!

# Пример победы в игре
brain-even

Welcome to the Brain Games!
May I have your name? Kit the Winner
Hello, Kit the Winner!
Answer "yes" if the number is even, otherwise answer "no".
Question: 51
Your answer: no
Correct!
Question: 79
Your answer: no
Correct!
Question: 97
Your answer: no
Correct!
Congratulations, Kit the Winner!