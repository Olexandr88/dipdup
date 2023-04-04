# generated by datamodel-codegen:
#   filename:  Swap.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class Swap(BaseModel):
    class Config:
        extra = Extra.forbid

    sender: str
    recipient: str
    amount0: int
    amount1: int
    sqrtPriceX96: int
    liquidity: int
    tick: int
