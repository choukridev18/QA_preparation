from dataclasses import dataclass


@dataclass
class Product:
    """Représente un article en stock."""
    name: str
    price: float
    quantity: int


def calculate_stock_value(products: list[Product]) -> float:
    """Retourne la valeur totale du stock (prix unitaire × quantité, pour tous les produits)."""
    return sum(p.price * p.quantity for p in products)


def get_low_stock_products(products: list[Product], threshold: int) -> list[Product]:
    """Retourne les produits dont la quantité est inférieure ou égale au seuil donné.
    L'ordre de la liste retournée correspond à l'ordre de la liste d'entrée.
    """
    return [p for p in products if p.quantity <= threshold]


def apply_discount(price: float, discount_pct: float) -> float:
    """Applique un pourcentage de remise sur un prix.
    Lève ValueError si discount_pct n'est pas dans [0, 100].
    """
    if not (0 <= discount_pct <= 100):
        raise ValueError(f"Remise invalide : {discount_pct}. Doit être entre 0 et 100.")
    return price * (1 - discount_pct / 100)


def get_most_expensive(products: list[Product]) -> Product:
    """Retourne le produit avec le prix unitaire le plus élevé.
    Lève TypeError si la liste est vide.
    """
    if not products:
        raise TypeError("La liste de produits est vide.")
    return max(products, key=lambda p: p.price)


def total_units(products: list[Product]) -> int:
    """Retourne le nombre total d'unités en stock (somme des quantités)."""
    return sum(p.quantity for p in products)
