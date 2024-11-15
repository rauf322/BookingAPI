from fastapi import HTTPException, status


UserAlreadyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail = "User already exist"
)

IncorrectLoginException= HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail = "Incorrect username or password"
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail = "Token expired"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail = "Token absence"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail = "Incorrect token format"
)

UserNotFoundException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail = "User not found"
)

RoomCantBeBookedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail = "Room is full"
)