#!/usr/bin/env python3
"""
Script de teste para verificar a lógica do Weekend Blocker sem o Anki.
Útil para testar a detecção de fins de semana.
"""

import datetime


def is_weekend() -> bool:
    """Check if today is Saturday (5) or Sunday (6)."""
    today = datetime.datetime.now().weekday()
    return today in [5, 6]


def get_day_name() -> str:
    """Get the current day name in Portuguese."""
    days = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    return days[datetime.datetime.now().weekday()]


def test_weekend_logic():
    """Test the weekend detection logic."""
    print("=" * 50)
    print("Weekend Blocker - Teste de Lógica")
    print("=" * 50)
    print()

    today = datetime.datetime.now()
    day_name = get_day_name()
    is_weekend_today = is_weekend()

    print(f"📅 Data atual: {today.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📆 Dia da semana: {day_name}")
    print(f"🏖️  É fim de semana? {'Sim' if is_weekend_today else 'Não'}")
    print()

    if is_weekend_today:
        print("✅ Ação esperada: BLOQUEAR novos cards (limite = 0)")
    else:
        print("✅ Ação esperada: PERMITIR novos cards (restaurar limites)")

    print()
    print("=" * 50)
    print("Simulação da semana:")
    print("=" * 50)
    print()

    # Simular a semana inteira
    for day_offset in range(7):
        test_date = today + datetime.timedelta(days=day_offset)
        test_weekday = test_date.weekday()
        test_day_name = {
            0: "Segunda-feira",
            1: "Terça-feira",
            2: "Quarta-feira",
            3: "Quinta-feira",
            4: "Sexta-feira",
            5: "Sábado",
            6: "Domingo"
        }[test_weekday]

        is_weekend_day = test_weekday in [5, 6]
        action = "🚫 BLOQUEAR" if is_weekend_day else "✅ PERMITIR"

        print(f"{test_date.strftime('%Y-%m-%d')} | {test_day_name:15} | {action}")

    print()
    print("=" * 50)


if __name__ == "__main__":
    test_weekend_logic()
