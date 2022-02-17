def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    return {c.lower(): k for k, v in legacy_data.items() for c in v}
