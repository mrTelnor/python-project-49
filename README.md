[![Actions Status](https://github.com/mrTelnor/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/mrTelnor/python-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mrTelnor_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mrTelnor_python-project-49)

## Description
It is a collection of 5 math-related games designed to challenge and improve your arithmetic skills. The games include:

- Providing the result of a calculation (multiplication, addition, subtraction);
- Answering if a number is even;
- Finding the greatest common divisor of two numbers;
- Checking if a number is prime;
- Inserting a number into an arithmetic progression;

## Installation

Use this commands to install games:
1. Install dependencies: 
```
make install
```
2. Build the package: 
```
make build
```
3. Install the package globally:
```
make package-install
```

After this step, the games will be available as standalone CLI commands, no need to use uv run.

Welcome message:
```
brain-games
```
Simple arithmetic calculator:
```
brain-calc
```
Check if a number is even:
```
brain-even
```
Find the greatest common divisor:
```
brain-gcd
```
Check if a number is prime:
```
brain-prime
```
Guess the missing number in a progression:
```
brain-progression
```

## Demonstrations

```
brain-games
```
<img src="https://asciinema.org/a/tM8ggrnP6lD12mc8JrjX7SRZa.svg" width="200"/>