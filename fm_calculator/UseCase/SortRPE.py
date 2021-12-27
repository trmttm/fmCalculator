def get_sorted_rpes(rpes: dict, order_of_calculation: tuple, direct_links: tuple) -> dict:
    sorted_rpes = {}
    tos = direct_links_destination = tuple(to for (f, to, s) in direct_links)
    froms = tuple(f for (f, to, s) in direct_links)
    tos_to_froms = dict(zip(tos, froms))

    for account in order_of_calculation:
        if account in rpes:
            rpe = rpes[account]
            sorted_rpes[account] = rpe
        elif account in direct_links_destination:
            sorted_rpes[account] = (tos_to_froms[account],)
    return sorted_rpes
