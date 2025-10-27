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

# Запуск игры калькулятор
brain-calc

Welcome to the Brain Games!
May I have your name? Bob
Hello, Bob!
What is the result of the expression?
Question: 2 + 2
Your answer: 3
'3' is wrong answer ;(. Correct answer was '4'.
Let's try again, Bob!

# Пример победы в игре
brain-calc

Welcome to the Brain Games!
May I have your name? Bob
Hello, Bob!
What is the result of the expression?
Question: 3 * 10
Your answer: 30
Correct!
Question: 20 - 20
Your answer: 0
Correct!
Question: 19 * 20
Your answer: 380
Correct!
Congratulations, Bob!

# Запуск игры наибольший общий делитель
brain-gcd

Welcome to the Brain Games!
May I have your name? Nik
Hello, Nik!
Find the greatest common divisor of given numbers.
Question: 11 100
Your answer: 4
'4' is wrong answer ;(. Correct answer was '1'.
Let's try again, Nik!

# Пример победы в игре
brain-gcd

Welcome to the Brain Games!
May I have your name? Nik
Hello, Nik!
Find the greatest common divisor of given numbers.
Question: 24 5
Your answer: 1
Correct!
Question: 12 16
Your answer: 4
Correct!
Question: 67 60
Your answer: 1
Correct!
Congratulations, Nik!

# Запуск игры арифметическая прогрессия
brain-progression

Welcome to the Brain Games!
May I have your name? Nik
Hello, Nik!
What number is missing in the progression?
Question: 5 10 15 20 .. 30 35 40 45 50
Your answer: 56
'56' is wrong answer ;(. Correct answer was '25'.
Let's try again, Nik!

# Пример победы в игре
brain-progression

Welcome to the Brain Games!
May I have your name? Nik
Hello, Nik!
What number is missing in the progression?
Question: 10 11 .. 13 14 15
Your answer: 12
Correct!
Question: 8 12 16 .. 24
Your answer: 20
Correct!
Question: 2 8 14 20 26 .. 38
Your answer: 32
Correct!
Congratulations, Nik!