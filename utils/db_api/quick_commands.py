from utils.db_api.schemas.user import User
from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db

async def add_user(user_id:int, first_name: str, last_name: str, username:str, status:str, referral_id: int, balance: float ):
    try:
        user= User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status, referral_id=referral_id, balance=balance)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")

async def select_all_users():
    users= await User.query.gino.all()
    return users

async def count_users():
    count= await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user= await User.query.where(User.user_id== user_id).gino.first()
    return user

async def update_status(user_id, status):
    user= await select_user(user_id) #User.get(user_id)
    await user.update(status=status).apply()

async def check_args(args, user_id: int):
    if args=="":
        args="0"
        return args

    elif not args.isnumeric():
        args="0"
        return args

    elif args.isnumeric():

        if int(args)==user_id:
            args="0"
            return args
        elif await select_user(user_id=int(args)) is None:
            args="0"
            return args
        else:
            args=str(args)
            return args

    else:
        args="0"
        return args

async def count_ref(user_id):
    refs= await User.query.where(User.referral_id==user_id).gino.all()
    return len(refs)

async def change_balance(user_id:int, amount):
    user= await select_user(user_id)
    new_balance= user.balance + amount
    await user.update(balance=new_balance).apply()

async def check_balance(user_id:int, amount):
    user= await select_user(user_id)
    try:
        amount= float(amount)
        if user.balance + amount>=0:
            await change_balance(user_id, amount)
            return True
        elif user.balance + amount<0:
            return "no money"
    except Exception:
        return False
