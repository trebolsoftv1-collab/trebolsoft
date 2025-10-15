
from sqlalchemy import Column, DateTime, Numeric, Integer, Boolean, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .base import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(UUID(as_uuid=True), primary_key=True)
    full_name = Column(Text, nullable=False)
    document = Column(Text)
    phone = Column(Text)
    status = Column(Text, nullable=False, default="activo")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True))

class Address(Base):
    __tablename__ = "addresses"
    id = Column(UUID(as_uuid=True), primary_key=True)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    address_line = Column(Text)
    lat = Column(Numeric(10,6))
    lng = Column(Numeric(10,6))
    zone = Column(Text)
    primary = Column(Boolean, default=False)

class Loan(Base):
    __tablename__ = "loans"
    id = Column(UUID(as_uuid=True), primary_key=True)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    principal = Column(Numeric(14,2), nullable=False)
    rate_daily = Column(Numeric(6,4), nullable=False)
    insurance = Column(Numeric(14,2), default=0)
    term_days = Column(Integer, nullable=False)
    start_date = Column(DateTime(timezone=False), nullable=False)
    status = Column(Text, nullable=False, default="vigente")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True))

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(UUID(as_uuid=True), primary_key=True)
    loan_id = Column(UUID(as_uuid=True), ForeignKey("loans.id"), nullable=False)
    due_date = Column(DateTime(timezone=False), nullable=False)
    amount_due = Column(Numeric(14,2), nullable=False)
    paid = Column(Boolean, default=False)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(UUID(as_uuid=True), primary_key=True)
    loan_id = Column(UUID(as_uuid=True), ForeignKey("loans.id"), nullable=False)
    schedule_id = Column(UUID(as_uuid=True), ForeignKey("schedules.id"))
    collector_id = Column(UUID(as_uuid=True))
    pay_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    amount_paid = Column(Numeric(14,2), nullable=False)
    method = Column(Text)
    receipt_number = Column(Text)

class Route(Base):
    __tablename__ = "routes"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(Text)
    zone = Column(Text)
    date = Column(DateTime(timezone=False))
    status = Column(Text, default="planificada")

class RouteStop(Base):
    __tablename__ = "route_stops"
    id = Column(UUID(as_uuid=True), primary_key=True)
    route_id = Column(UUID(as_uuid=True), ForeignKey("routes.id"), nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    sequence = Column(Integer)
    planned_lat = Column(Numeric(10,6))
    planned_lng = Column(Numeric(10,6))
    notes = Column(Text)
    visited = Column(Boolean, default=False)
    visited_at = Column(DateTime(timezone=True))

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(UUID(as_uuid=True), primary_key=True)
    route_id = Column(UUID(as_uuid=True), ForeignKey("routes.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    assigned_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class CashSession(Base):
    __tablename__ = "cash_sessions"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    opened_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    closed_at = Column(DateTime(timezone=True))
    opening_cash = Column(Numeric(14,2))
    closing_cash = Column(Numeric(14,2))
    difference = Column(Numeric(14,2))

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(UUID(as_uuid=True), primary_key=True)
    entity = Column(Text, nullable=False)
    entity_id = Column(UUID(as_uuid=True), nullable=False)
    action = Column(Text, nullable=False)
    user_id = Column(UUID(as_uuid=True))
    at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    before = Column(Text)
    after = Column(Text)
