from sqlalchemy import select
stmt = select(User).where(User.email == email)
user = session.execute(stmt).scalar_one_or_none()