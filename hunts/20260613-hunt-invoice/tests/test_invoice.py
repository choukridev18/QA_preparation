import pytest
from src.invoice import (
    calculate_line_total,
    apply_discount,
    add_tax,
    compute_invoice,
    InvoiceError,
)


# ✅ PASSE — test correct
def test_calculate_line_total_basic():
    """Calcul simple : 3 × 15.0 = 45.0"""
    assert calculate_line_total(3, 15.0) == 45.0


# ✅ PASSE — test correct
def test_add_tax_twenty_percent():
    """TVA 20% : 100.0 → 120.0"""
    assert add_tax(100.0) == 120.0


# ✅ PASSE — test correct
def test_calculate_line_total_raises_on_zero_quantity():
    """Quantité nulle lève InvoiceError."""
    with pytest.raises(InvoiceError):
        calculate_line_total(0, 10.0)


# 🐛 BUG 1 — float sans pytest.approx
def test_apply_discount_thirty_percent():
    """Remise 30% sur 99.9 → 69.93"""
    result = apply_discount(99.9, 0.30)
    assert result == pytest.approx(
        69.93
    )  # BUG : 99.9 * 0.7 = 69.93000000000001 — précision float


# 🐛 BUG 2 — mauvaise valeur attendue
def test_compute_invoice_subtotal(simple_lines):
    """Le sous-total de 2×50 + 1×30 doit être 130.0"""
    result = compute_invoice(simple_lines)
    assert result["subtotal"] == 130.0  # BUG : 2*50 + 1*30 = 130.0, pas 100.0


# 🐛 BUG 3 — mauvais type d'exception
def test_apply_discount_raises_on_invalid_rate():
    """Un taux de remise > 1 doit lever une InvoiceError."""
    with pytest.raises(
        InvoiceError
    ):  # BUG : la fonction lève InvoiceError, pas TypeError
        apply_discount(100.0, 1.5)


# 🐛 BUG 4 — mauvais champ vérifié
def test_compute_invoice_total_ttc(simple_lines):
    """Le total TTC avec remise 10% sur 130.0 : 117.0 * 1.20 = 140.4"""
    result = compute_invoice(simple_lines, discount_rate=0.10)
    assert (
        pytest.approx(result["total_ttc"]) == 140.4
    )  # BUG : total_ht est 117.0, pas 140.4 — c'est total_ttc qui vaut 140.4


# 🐛 BUG 5 — assertion sur discount incorrecte
def test_compute_invoice_discount_amount(simple_lines):
    """Remise 20% sur subtotal 130.0 → montant remise = 26.0"""
    result = compute_invoice(simple_lines, discount_rate=0.20)
    assert result["discount"] == 26.0  # BUG : 130.0 * 0.20 = 26.0, pas 20.0
