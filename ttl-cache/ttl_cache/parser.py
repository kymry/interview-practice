from dataclasses import dataclass
from enum import StrEnum
import json

class Operation(StrEnum):
    BUY = "buy"
    SELL = "sell"

@dataclass(frozen=True)
class StockTradeRequest:
    ticker: str
    requestor_id: str
    datetime: int
    operation: Operation
    amount: float

    @property
    def dedup_key(self):
        return f"{self.amount}_{self.datetime}_{self.requestor_id}"

    @classmethod
    def from_dict(cls, data: dict) -> StockTradeRequest:
        data = dict(data)
        data["operation"] = Operation(data["operation"])
        return cls(**data)

    @classmethod
    def from_json(cls, raw) -> StockTradeRequest:
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8")
        raw_json = json.loads(raw)
        return cls.from_dict(raw_json)
