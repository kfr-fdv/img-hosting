import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs


class AppJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def get_query_params(path: str) -> dict[str, str]:
    parsed = parse_qs(urlparse(path).query)
    return {k: v[0] for k, v in parsed.items()}
    