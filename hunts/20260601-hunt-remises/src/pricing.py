def apply_discount(price: float, discount_rate: float) -> float:
    """
    Apply a discount to a price.

    Args:
        price: Original price (must be >= 0)
        discount_rate: Fraction to discount (must be between 0.0 and 1.0)

    Returns:
        Price after discount.

    Raises:
        ValueError: if discount_rate is not in [0, 1]
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError(f"discount_rate must be between 0 and 1, got {discount_rate}")
    return price * (1 - discount_rate)


def calculate_tva(price: float, tva_rate: float = 0.20) -> float:
    """
    Apply TVA (tax) to a price.

    Args:
        price: Price before tax
        tva_rate: TVA rate as a fraction (default 0.20 = 20%)

    Returns:
        Price including TVA.
    """
    return price * (1 + tva_rate)


def final_price(price: float, discount_rate: float, tva_rate: float = 0.20) -> float:
    """
    Compute the final price after discount and TVA.
    Discount is applied first, then TVA.

    Args:
        price: Original price
        discount_rate: Fraction to discount (0.0–1.0)
        tva_rate: TVA rate (default 0.20 = 20%)

    Returns:
        Final price after discount and TVA.
    """
    discounted = apply_discount(price, discount_rate)
    return calculate_tva(discounted, tva_rate)


def get_cheapest_items(prices: list, n: int) -> list:
    """
    Return the n cheapest prices from a list, sorted ascending.

    Args:
        prices: List of prices
        n: Number of items to return

    Returns:
        The n lowest prices, sorted from cheapest to most expensive.
    """
    return sorted(prices)[:n]


def validate_discount(discount_rate: float) -> None:
    """
    Validate that a discount rate is in [0, 1].

    Raises:
        ValueError: if discount_rate is outside [0, 1]
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError(f"Invalid discount rate: {discount_rate}")
