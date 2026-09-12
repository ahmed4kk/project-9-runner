"""Project 9 public runner gateway.

The runner contains no Lotus business logic. It only exposes health/dispatch
operations and executes the private Core after GitHub Actions checks it out.
"""
import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Project 9 Runner", version="1.0.0")

class DispatchRequest(BaseModel):
    task_id: str

def _check_secret(value: str | None):
    expected = os.getenv("RUNNER_SHARED_SECRET")
    if not expected or value != expected:
        raise HTTPException(status_code=401, detail="unauthorized")

@app.get("/health")
def health():
    return {"status": "ok", "service": "project-9-runner"}

@app.post("/dispatch")
def dispatch(req: DispatchRequest, x_runner_secret: str | None = Header(default=None)):
    _check_secret(x_runner_secret)
    # Dispatch is intentionally delegated to the GitHub Actions workflow.
    # The public runner never executes proprietary logic from the HTTP process.
    return {"accepted": True, "task_id": req.task_id, "mode": "github_actions"}
