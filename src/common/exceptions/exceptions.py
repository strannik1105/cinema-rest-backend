from fastapi import HTTPException

HTTPNotFoundError = HTTPException(status_code=404, detail="Item not found")

UnauthorizedError = HTTPException(
    status_code=401, detail="invalid username or password"
)

ImageUploadError = HTTPException(
    status_code=403, detail="Some troubles with image uploading"
)

AlreadyBookedError = HTTPException(status_code=403, detail="This time range is already booked")
