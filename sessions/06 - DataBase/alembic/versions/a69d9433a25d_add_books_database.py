"""add books database

Revision ID: a69d9433a25d
Revises: 
Create Date: 2017-01-19 22:38:26.148052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a69d9433a25d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('author', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
    )


def downgrade():
    op.drop_table('books')
