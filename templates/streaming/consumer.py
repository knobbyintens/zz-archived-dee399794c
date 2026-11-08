"""Streaming consumer template."""

import json


def handle(event):
    record = json.loads(event)
    return {"id": record.get("id"), "ok": True}
