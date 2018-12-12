from prometheus_client import Counter, Histogram


FLASK_REQUEST_LATENCY = Histogram(
    "flask_request_latency_seconds", "Flask Request Latency", ["method", "endpoint"]
)
FLASK_REQUEST_COUNT = Counter(
    "flask_request_count", "Flask Request Count", ["method", "endpoint", "http_status"]
)
