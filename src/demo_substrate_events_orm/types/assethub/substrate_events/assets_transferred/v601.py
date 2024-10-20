# generated by DipDup 8.1.1

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field


class V601(BaseModel):
    """
    Some assets were transferred. [asset_id, from, to, amount]
    """

    asset_id: int = Field(..., description='U32')
    from_: str = Field(..., alias='from', description='AccountId')
    to: str = Field(..., description='AccountId')
    amount: int = Field(..., description='U128')
