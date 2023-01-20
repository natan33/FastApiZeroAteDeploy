from decimal import Decimal
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/contas-a-pagar-e-receber")

# Classes para passar os parametros com o get para a APIRest
class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str # PAGAR, RECEBER

class ContasPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str # PAGAR, RECEBER

# Função que manda para a APIREST
@router.get("/",response_model=List[ContasPagarReceberResponse])
def listar_contas():
    return [
        ContasPagarReceberResponse(
            id = 1,
            descricao = "Aluguel",
            valor = 1110.50,
            tipo = "PAGAR"

        ),
        ContasPagarReceberResponse(
            id=2,
            descricao="Salario",
            valor=50000,
            tipo="RECEBER"

        )
    ]

@router.post("/", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta: ContasPagarReceberRequest):
    return ContasPagarReceberResponse(
        id=3,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )