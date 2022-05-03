import sqlalchemy
from .base import metadata
import datetime

account_member = sqlalchemy.Table(
    "account_member",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False, index=True),
    sqlalchemy.Column("integration_id", sqlalchemy.ForeignKey("account_integrations.id"), index=True)
)

account_integrations = sqlalchemy.Table(
    "account_integrations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("owner_id", sqlalchemy.ForeignKey("users.id"), nullable=False, index=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("code", sqlalchemy.String),
    sqlalchemy.Column("api_key", sqlalchemy.String, index=True),
    sqlalchemy.Column("api_secret", sqlalchemy.String, index=True),
    sqlalchemy.Column("badge_key", sqlalchemy.String),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
