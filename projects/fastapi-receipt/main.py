cat > main.py << 'PY'
from enum import Enum
from typing import List, Optional, Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Receipt Demo API")

# ---- Модели входных данных ----
class TicketKind(str, Enum):
    passenger = "passenger"
    baggage = "baggage"

class Ticket(BaseModel):
    kind: TicketKind
    price: float
    refund_amount: Optional[float] = None  # для возврата

class Cashier(BaseModel):
    name: str = "Demo Cashier"

class Buyer(BaseModel):
    email: str = "user@example.com"

class IncomeRequest(BaseModel):
    request_id: int
    tickets: List[Ticket]
    cashier: Cashier = Cashier()
    buyer: Buyer = Buyer()

class RefundRequest(BaseModel):
    request_id: int
    tickets: List[Ticket]
    cashier: Cashier = Cashier()
    buyer: Buyer = Buyer()

# ---- Вспомогалки ----
def build_income_payload(req: IncomeRequest) -> Dict:
    passenger = [t for t in req.tickets if t.kind == TicketKind.passenger]
    baggage = [t for t in req.tickets if t.kind == TicketKind.baggage]

    # группируем пассажирские по цене
    price_to_qty: Dict[float, int] = {}
    for t in passenger:
        price_to_qty[t.price] = price_to_qty.get(t.price, 0) + 1

    items = []
    for price, qty in price_to_qty.items():
        items.append({
            "Description": "Билет на автобус",
            "Price": int(round(price * 100)),
            "Qty": qty,
            "Tax": 0,
            "PaymentItem": 4,
            "PaymentType": 4,
        })

    if baggage:
        items.append({
            "Description": "Багажный билет",
            "Price": int(round(baggage[0].price * 100)),
            "Qty": len(baggage),
            "Tax": 0,
            "PaymentItem": 4,
            "PaymentType": 4,
        })

    return {
        "requestId": req.request_id,
        "method": "income",
        "params": {
            "Cashier": {"Name": req.cashier.name},
            "Persona": {"Email": req.buyer.email},
            "SendCheck": "Email",
            "DocItems": items,
            "SumTypePayment": 2,
        },
    }

def build_refund_payload(req: RefundRequest) -> Dict:
    passenger = [t for t in req.tickets if t.kind == TicketKind.passenger]
    baggage = [t for t in req.tickets if t.kind == TicketKind.baggage]

    # группируем по refund_amount (только его!)
    refund_to_qty: Dict[float, int] = {}
    for t in passenger:
        amt = float(t.refund_amount or 0.0)
        refund_to_qty[amt] = refund_to_qty.get(amt, 0) + 1

    items = []
    for refund_amount, qty in refund_to_qty.items():
        items.append({
            "Description": "Билет на автобус",
            "Price": int(round(refund_amount * 100)),
            "Qty": qty,
            "Tax": 0,
            "PaymentItem": 4,
            "PaymentType": 4,
        })

    if baggage:
        items.append({
            "Description": "Багажный билет",
            "Price": int(round(float(baggage[0].refund_amount or 0.0) * 100)),
            "Qty": len(baggage),
            "Tax": 0,
            "PaymentItem": 4,
            "PaymentType": 4,
        })

    return {
        "requestId": req.request_id,
        "method": "income_return",
        "params": {
            "Cashier": {"Name": req.cashier.name},
            "Persona": {"Email": req.buyer.email},
            "SendCheck": "Email",
            "DocItems": items,
            "SumTypePayment": 2,
        },
    }

# ---- Эндпоинты ----
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/receipt/income")
def income(req: IncomeRequest):
    return build_income_payload(req)

@app.post("/receipt/refund")
def refund(req: RefundRequest):
    return build_refund_payload(req)

@app.get("/receipt/status/{request_id}")
def status(request_id: int):
    # демо-ответ статуса
    return {"requestId": request_id, "status": "COMPLETED"}
PY
