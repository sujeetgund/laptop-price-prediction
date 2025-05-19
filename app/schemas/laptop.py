from pydantic import BaseModel, Field
from typing import Literal
from app.core.constants import (
    CompanyEnum,
    TypeNameEnum,
    OpSysEnum,
    ResCategoryEnum,
    CpuCategoryEnum,
    GpuCategoryEnum,
)


class Laptop(BaseModel):
    Company: CompanyEnum
    TypeName: TypeNameEnum
    Inches: float = Field(..., gt=0)
    Ram: int = Field(..., gt=0)
    OpSys: OpSysEnum
    Weight: float = Field(..., gt=0)
    HasIpsPanel: Literal[0, 1]
    HasTouchScreen: Literal[0, 1]
    ResWidth: int = Field(..., gt=0)
    ResHeight: int = Field(..., gt=0)
    ResCategory: ResCategoryEnum
    Ppi: float = Field(..., gt=0)
    Ssd: int = Field(..., ge=0)
    Hdd: int = Field(..., ge=0)
    Flash: int = Field(..., ge=0)
    Hybrid: int = Field(..., ge=0)
    CpuCategory: CpuCategoryEnum
    CpuSpeedGhz: float = Field(..., gt=0)
    GpuCategory: GpuCategoryEnum


class PriceOutput(BaseModel):
    predicted_price: float
