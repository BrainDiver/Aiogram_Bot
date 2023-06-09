from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float

class User(TimedBaseModel):
    __tablename__ = "users"
    user_id= Column(BigInteger, primary_key= True)
    first_name= Column(String(200))
    last_name= Column(String(50))
    username= Column(String(50))
    status= Column(String(50))
    referral_id= Column(BigInteger)
    balance= Column(Float)

    query: sql.select
