from fastapi import HTTPException

HTTPNotFoundError = HTTPException(status_code=404, detail="Item not found")
