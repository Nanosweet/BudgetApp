from datetime import datetime

def waliduj_wiersz(row):
    try:
        datetime.strptime(row['data'], '%Y-%m-%d')
        float(row['kwota'])
        assert row['typ'] in ['wydatek', 'przychod']
        return True
    except (ValueError, AssertionError, KeyError):
        return False