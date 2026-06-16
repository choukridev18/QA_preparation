# ============================================================
# DRILL — pytest.mark.parametrize · exceptions personnalisées · dataclass
# ============================================================
# Contexte :
#   Tu travailles sur un module de tarification pour une plateforme SaaS.
#   Chaque abonnement a un plan, une durée et un code promo optionnel.
#   Le module calcule le prix final et lève des erreurs métier précises
#   quand les données sont invalides.
#
# Objectif :
#   Implémenter les fonctions ci-dessous pour que tous les tests passent.
#   Lance : pytest test_exercise.py -v
# ============================================================

from dataclasses import dataclass


# ------------------------------------------------------------
# Types
# ------------------------------------------------------------

PLANS: dict[str, float] = {
    "starter": 9.99,
    "pro": 29.99,
    "enterprise": 99.99,
}

PROMO_CODES: dict[str, float] = {
    "WELCOME10": 0.10,
    "SUMMER20": 0.20,
    "VIP50": 0.50,
}


@dataclass
class Subscription:
    plan: str
    months: int
    promo_code: str | None = None


class PricingError(ValueError):
    """Levée quand les données de tarification sont invalides."""

    pass


class UnknownPlanError(PricingError):
    """Levée quand le plan n'existe pas."""

    pass


class InvalidDurationError(PricingError):
    """Levée quand la durée est inférieure ou égale à 0."""

    pass


class InvalidPromoError(PricingError):
    """Levée quand le code promo est inconnu."""

    pass


# ------------------------------------------------------------
# TODO 1 — Prix de base
# ------------------------------------------------------------
# Entrée  : Subscription(plan="pro", months=3)
# Sortie  : 89.97   (29.99 × 3)
# Lève UnknownPlanError si le plan n'est pas dans PLANS.
# Lève InvalidDurationError si months <= 0.
# ------------------------------------------------------------
def base_price(sub: Subscription) -> float:
    if sub.months <= 0:
        raise InvalidDurationError()
    elif sub.plan not in PLANS:
        raise UnknownPlanError(sub.plan)
    else:
        return PLANS[sub.plan] * sub.months


# ------------------------------------------------------------
# TODO 2 — Taux de remise
# ------------------------------------------------------------
# Entrée  : "WELCOME10"
# Sortie  : 0.10
# Entrée  : None
# Sortie  : 0.0   (pas de promo = pas de remise)
# Lève InvalidPromoError si le code n'est pas None et n'est pas dans PROMO_CODES.
# ------------------------------------------------------------
def discount_rate(promo_code: str | None) -> float:
    if promo_code is None:
        return 0.0
    elif promo_code not in PROMO_CODES:
        raise InvalidPromoError(promo_code)
    else:
        return PROMO_CODES[promo_code]


# ------------------------------------------------------------
# TODO 3 — Prix final
# ------------------------------------------------------------
# Entrée  : Subscription(plan="pro", months=3, promo_code="WELCOME10")
# Sortie  : 80.973  (89.97 × (1 - 0.10))
# Utilise base_price() et discount_rate() — ne recalcule pas.
# ------------------------------------------------------------
def final_price(sub: Subscription) -> float:
    return base_price(sub) * (1 - discount_rate(sub.promo_code))


# ------------------------------------------------------------
# TODO 4 — Résumé de l'abonnement
# ------------------------------------------------------------
# Entrée  : Subscription(plan="starter", months=1, promo_code=None)
# Sortie  : "starter — 1 mois — 9.99€"
# Entrée  : Subscription(plan="pro", months=6, promo_code="SUMMER20")
# Sortie  : "pro — 6 mois — 143.95€"  (179.94 × 0.80, arrondi à 2 décimales)
# ------------------------------------------------------------


def summary(sub: Subscription) -> str:
    price = round(final_price(sub), 2)
    return f"{sub.plan} — {sub.months} mois — {price}€"
