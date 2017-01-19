"""add rating to book

Revision ID: 5c2adafa7171
Revises: a69d9433a25d
Create Date: 2017-01-19 22:58:10.864420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c2adafa7171'
down_revision = 'a69d9433a25d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('books', sa.Column('rating', sa.Integer))


def downgrade():
    op.drop_column('books', 'rating')
