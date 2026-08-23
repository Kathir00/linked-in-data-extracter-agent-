from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.profile import router as profile_router


app = FastAPI(
    title="LinkedIn Profile Agent",
    version="1.0.0",
    description=(
        "Agent that extracts first name, last name, "
        "role and company from LinkedIn profiles."
    ),
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
        "https://agent-data-extracter-linkedin.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(profile_router)


@app.get("/")
def root():

    return {
        "message": "LinkedIn Profile Agent API is running."
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }