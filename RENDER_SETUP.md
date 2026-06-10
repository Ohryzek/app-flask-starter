# Nasazení aplikace na Render.com

Postupuj podle těchto kroků, aby jsi nasadil(a) Flask aplikaci na Render.com.

## Krok 1: Přihlášení na Render.com

1. Navštiv https://render.com
2. Klikni na "Sign In"
3. Přihlaš se přes **GitHub** (doporučuji) - to zjednoduší propojení s repozitářem

## Krok 2: Vytvoření nové webové služby

1. Po přihlášení budeš na Render Dashboard
2. Klikni na **"New+"** a vyber **"Web Service"**
3. Vyber **"Connect a repository"** a zvolí svůj GitHub repozitář (app-flask-starter)

## Krok 3: Konfigurace nasazení

Vyplň následující údaje:

| Pole | Hodnota |
|------|---------|
| **Name** | app-flask-starter |
| **Environment** | Python 3 |
| **Region** | Vybrat libovolný (např. Frankfurt nebo Frankfurt-EU) |
| **Branch** | main |
| **Root Directory** | ./ (nebo prázdné) |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

## Krok 4: Nastavení prostředí (volitelně)

Pokud chceš nastavit:
- Environment variables nejsou v našem případě potřeba
- Free tier je dostačující pro testování

## Krok 5: Nasazení

1. Klikni na **"Create Web Service"**
2. Čekej na nasazení (objeví se progress bar)
3. Po dokončení budeš mít URL aplikace, např: `https://app-flask-starter-xxxxx.onrender.com`

## Krok 6: Testování aplikace online

1. Otevři svou URL aplikace
2. Ověř, že funguje:
   - Hlavní stránka s GET parametry: `/pozdrav-post?name=Petr&surname=Svoboda`
   - POST formulář: `/pozdrav-post` s heslem `python123`
   - Validace: Zkus prázdné jméno nebo velmi dlouhé jméno

## Řešení problémů

### Aplikace se nespouští
- Zkontroluj Render Logs v dashboard - tam jsou chybové zprávy
- Ověř, že Build a Start command jsou správně nastaveny
- Zkontroluj, že requirements.txt obsahuje všechny potřebné balíčky

### Chyba 503
- Aplikace se ještě nasazuje, čekej pár minut
- Zkontroluj Build log

### Chyba "Module not found"
- Ověř, že requirements.txt je v kořenovém adresáři projektu
- Přidej chybějící balíček do requirements.txt a pushni změnu na GitHub

## Poznámka o free tier

Free tier Render.com má omezenou dobu nečinnosti - pokud aplikace není používána po dobu, vypršeí se. Při příštím přístupu se bude trvat chvíli znovu spustit.
