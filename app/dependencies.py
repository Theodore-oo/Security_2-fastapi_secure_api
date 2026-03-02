from fastapi import Depends, HTTPException
from jose import JWSError, jwt 
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import User
from .auth import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
        db = SessionLocal()
        try:
                yield db
        finally:
                db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                username: str = payload.get("sub")
        except JWSError:
                raise HTTPException(status_code=401, detail="Invalid token")
        
        user = db.query(User).filter(User.username == username).first()
        if user in None:
                raise HTTPException(status_code=401, detail="User no found")
        return user