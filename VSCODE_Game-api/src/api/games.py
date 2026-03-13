from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from src.models.game import GameCreate, GameResponse, GameUpdate, GameService, get_game_service

router = APIRouter()

@router.post("/games", response_model=GameResponse, status_code=201)
def create_game(game: GameCreate, service: GameService = Depends(get_game_service)):
    return service.create_game(game)

@router.get("/games", response_model=List[GameResponse])
def get_games(service: GameService = Depends(get_game_service)):
    return service.get_games()

@router.get("/games/{game_id}", response_model=GameResponse)
def get_game(game_id: UUID, service: GameService = Depends(get_game_service)):
    game = service.get_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.put("/games/{game_id}", response_model=GameResponse)
def update_game(game_id: UUID, game_data: GameUpdate, service: GameService = Depends(get_game_service)):
    game = service.update_game(game_id, game_data)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.delete("/games/{game_id}", status_code=204)
def delete_game(game_id: UUID, service: GameService = Depends(get_game_service)):
    deleted = service.delete_game(game_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Game not found")
    return None