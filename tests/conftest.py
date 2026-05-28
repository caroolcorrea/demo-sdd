"""
conftest.py — Fixtures globais para todos os testes.
"""

import pytest
from hypothesis import settings as hypothesis_settings, HealthCheck

# --- Hypothesis profiles ---
hypothesis_settings.register_profile(
    "demo",
    max_examples=50,
    suppress_health_check=[HealthCheck.too_slow],
)
hypothesis_settings.register_profile(
    "ci",
    max_examples=20,
    suppress_health_check=[HealthCheck.too_slow],
)
hypothesis_settings.load_profile("demo")
