import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("username", sqlalchemy.String),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    sqlalchemy.Column("update_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
)

item = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("title", sqlalchemy.String, index=True),
    sqlalchemy.Column("description", sqlalchemy.String, index=True),
    sqlalchemy.Column("owner_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
)

users_profils = sqlalchemy.Table(
    "users_profils",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False, unique=True),
    sqlalchemy.Column("next_report_date", sqlalchemy.DateTime),
    sqlalchemy.Column("reports_allowed", sqlalchemy.Integer),
    sqlalchemy.Column("ping_log_limit", sqlalchemy.Integer),
    sqlalchemy.Column("token", sqlalchemy.VARCHAR),
    sqlalchemy.Column("check_limit", sqlalchemy.Integer),
    sqlalchemy.Column("last_message", sqlalchemy.DateTime),
    sqlalchemy.Column("message_limit", sqlalchemy.Integer),
    sqlalchemy.Column("mwssage_sent", sqlalchemy.Integer)
)
