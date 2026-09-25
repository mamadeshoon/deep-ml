def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if not samples:
        return []
        
    counts = {}

    for value in samples:
        counts[value] = counts.get(value, 0) + 1

    n = len(samples)

    return [(value, counts[value] / n) for value in sorted(counts)]