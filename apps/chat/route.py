from fastapi import APIRouter
from pydantic import BaseModel
from apps.chat.utils import generate_itr_advice

router = APIRouter()

class ITRRequest(BaseModel):
    income_sources: str
    deductions: str

class ITRResponse(BaseModel):
    advice: str

@router.post("/advice", response_model=ITRResponse)
def get_tax_advice(request: ITRRequest):
    """Endpoint for generating tax filing advice"""
    advice = generate_itr_advice(
        income_sources=request.income_sources,
        deductions=request.deductions
    )
    return {"advice": advice}