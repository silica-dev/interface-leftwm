#!/bin/python3

from astral import moon
import datetime
from datetime import timedelta


def moon_phase_to_inacurate_code(phase):
    """Converts moon phase code to inacurate code."""
    phase = int(phase)
    value = None
    if phase == 0:
        value = 0
    elif 0 < phase < 7:
        value = 1
    elif phase == 7:
        value = 2
    elif 7 < phase < 14:
        value = 3
    elif phase == 14:
        value = 4
    elif 14 < phase < 21:
        value = 5
    elif phase == 21:
        value = 6
    else:
        value = 7
    return value


def get_phase(time):
    MOON_PHASES = ["🌕", "🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔"]
    phase_today = moon.phase(date=time)
    code_today = moon_phase_to_inacurate_code(phase_today)

    phase_yesterday = moon.phase(time - timedelta(days=1))
    code_yesterday = moon_phase_to_inacurate_code(phase_yesterday)

    if (code_today - code_yesterday) % 8 > 1:
        return MOON_PHASES[(code_today - 1) % 8]

    if code_today % 2 != 0:
        return MOON_PHASES[code_today]

    if code_today == code_yesterday:
        return MOON_PHASES[(code_today + 1) % 8]

    return MOON_PHASES[code_today]


if __name__ == "__main__":
    print(get_phase(datetime.datetime.now()))
