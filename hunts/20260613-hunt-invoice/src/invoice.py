"""
Module de facturation.
Calcule les totaux, applique les remises et la TVA sur des lignes de facture.
"""

TAX_RATE = 0.20  # TVA à 20%


class InvoiceError(ValueError):
    """Levée quand une ligne de facture est invalide."""
    pass


def calculate_line_total(quantity: int, unit_price: float) -> float:
    """
    Calcule le total HT d'une ligne (quantité × prix unitaire).
    Lève InvoiceError si la quantité ou le prix est négatif ou nul.
    """
    if quantity <= 0 or unit_price <= 0:
        raise InvoiceError("La quantité et le prix doivent être positifs.")
    return quantity * unit_price


def apply_discount(total: float, discount_rate: float) -> float:
    """
    Applique une remise en pourcentage sur un total.
    Ex : apply_discount(100.0, 0.10) → 90.0
    Lève InvoiceError si le taux est hors de [0, 1].
    """
    if not 0 <= discount_rate <= 1:
        raise InvoiceError("Le taux de remise doit être entre 0 et 1.")
    return total * (1 - discount_rate)


def add_tax(total: float) -> float:
    """
    Ajoute la TVA (20%) au total HT.
    Ex : add_tax(100.0) → 120.0
    """
    return total * (1 + TAX_RATE)


def compute_invoice(lines: list[dict], discount_rate: float = 0.0) -> dict:
    """
    Calcule la facture complète à partir d'une liste de lignes.

    Chaque ligne est un dict {"quantity": int, "unit_price": float}.
    Retourne un dict :
      {
        "subtotal": float,     # total HT avant remise
        "discount": float,     # montant de la remise
        "total_ht": float,     # total HT après remise
        "tax": float,          # montant de la TVA
        "total_ttc": float,    # total TTC
      }
    """
    subtotal = sum(calculate_line_total(l["quantity"], l["unit_price"]) for l in lines)
    discounted = apply_discount(subtotal, discount_rate)
    discount_amount = subtotal - discounted
    tax_amount = discounted * TAX_RATE
    total_ttc = add_tax(discounted)

    return {
        "subtotal": subtotal,
        "discount": discount_amount,
        "total_ht": discounted,
        "tax": tax_amount,
        "total_ttc": total_ttc,
    }
