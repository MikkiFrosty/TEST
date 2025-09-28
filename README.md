
# OZON Deposit — чистая сборка (UI локально + Mobile через BrowserStack)

## Запуск
### UI (локально)
```bash
pip install -r requirements.txt
pytest tests/ui -q
```

### Mobile (BrowserStack)
Нужны переменные окружения:
- BROWSERSTACK_USERNAME
- BROWSERSTACK_ACCESS_KEY

```bash
pytest tests/mobile -m mobile -q
```
