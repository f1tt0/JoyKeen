import fastapi as FastAPI
from src.api import games
from src.middlewares import error_handler

app = FastAPI.FastAPI(title="Game API")

# Підключаємо глобальний обробник помилок
app.add_middleware(error_handler.ErrorHandlerMiddleware)
error_handler.setup_exception_handlers(app)

# Підключаємо роутер для games
app.include_router(games.router, prefix="/api")