# Практическая работа (90 минут) — Linux (bash)
## Тема: GitHub Actions CI — автозапуск pytest при push/PR

### 0–10 мин: старт + Git
```bash
cd ci_actions_lab
git init
git add .
git commit -m "init: starter ci project"
```

### 10–20 мин: локально тесты должны быть зелёные
```bash
python3 -m pip install --user pytest
python3 -m pytest -q
```

### 20–35 мин: GitHub repo + push
1) GitHub -> New repository (НЕ добавляй README).
2) Добавь remote и запушь:
```bash
git remote add origin <URL>
git push -u origin main 2>/dev/null || git push -u origin master
```

### 35–55 мин: workflow есть, но он сломан специально
Открой `.github/workflows/tests.yml`.
Сейчас в Actions pytest не установлен, поэтому запуск падает.
Исправь: добавь шаг установки pytest через pip.

Делай это в отдельной ветке:
```bash
git switch -c ci/fix
# исправь файл tests.yml
git add .github/workflows/tests.yml
git commit -m "ci: install pytest in workflow"
git push -u origin ci/fix
```

### 55–75 мин: Pull Request
- Открой PR из `ci/fix` в main
- Дождись зелёного Actions
- Merge

### 75–90 мин: tag + отчёт
```bash
git switch main 2>/dev/null || git switch master
git pull
git tag v0.4
git push --tags
```
Заполни REPORT.md, закоммить и запушь.

### Что показать преподавателю
- зелёный статус Actions в PR
- `python3 -m pytest -q`
- `git log --oneline --decorate --graph --all`
- `git tag`
