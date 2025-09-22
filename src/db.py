from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
import json

Base = declarative_base()

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, autoincrement=True)
    goal = Column(String(256))
    plan_json = Column(Text)  # store full plan as JSON string
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine("sqlite:///plans.db")
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def save_plan(goal: str, plan: dict):
    session = SessionLocal()
    p = Plan(goal=goal, plan_json=json.dumps(plan))
    session.add(p)
    session.commit()
    session.refresh(p)
    session.close()
    return p.id

def get_plan(plan_id: int):
    session = SessionLocal()
    p = session.query(Plan).filter(Plan.id == plan_id).first()
    session.close()
    if p:
        return {"id": p.id, "goal": p.goal, "plan": json.loads(p.plan_json), "created_at": p.created_at}
    else:
        return None

def get_history():
    session = SessionLocal()
    plans = session.query(Plan).order_by(Plan.created_at.desc()).all()
    session.close()
    return [{"id": p.id, "goal": p.goal, "created_at": p.created_at} for p in plans]
