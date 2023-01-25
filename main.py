from fastapi import FastAPI
import uvicorn

from contas_a_pagar_e_receber_router.routers import contas_a_pagar_e_receber_router


app = FastAPI()


app.include_router(contas_a_pagar_e_receber_router.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
