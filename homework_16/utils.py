def prepare_table_for_rendering(airports: list[str]) -> list[list[str]]:
    result = []
    for airport in airports:
        element = [airport]
        result.append(element)
    return result
