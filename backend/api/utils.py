from urllib.parse import urljoin


def join_url(*parts: str) -> str:
    """Join URL path parts without using OS-specific filesystem rules."""

    base, *path_parts = parts
    path = "/".join(part.strip("/") for part in path_parts)
    return urljoin(base.rstrip("/") + "/", path)
