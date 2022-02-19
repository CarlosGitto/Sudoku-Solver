from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get_sudoku import get_sudoku
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sudoku/new_sudoku/{difficulty}", tags=["Sudoku"])
async def get_new_sudoku(difficulty: str):
    sudoku = get_sudoku()
    return sudoku


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1",
                port=8000, log_level="info")
