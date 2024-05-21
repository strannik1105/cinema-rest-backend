from fastapi import HTTPException

HTTPNotFoundError = HTTPException(status_code=404, detail="Item not found")

UnauthorizedError = HTTPException(status_code=401, detail="invalid username or password")
