"""empty message

Revision ID: aa27cce0ac92
Revises: 
Create Date: 2018-04-28 17:46:17.522091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa27cce0ac92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.String(length=128), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('target', sa.String(length=128), nullable=False),
    sa.Column('timestamp', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('transaction_id'),
    sa.UniqueConstraint('transaction_id')
    )
    op.create_table('users',
    sa.Column('userID', sa.String(length=128), nullable=False),
    sa.Column('identifier', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('seed', sa.String(length=120), nullable=False),
    sa.Column('is_authenticated', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_anonymous', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('userID'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('seed'),
    sa.UniqueConstraint('userID')
    )
    op.create_index(op.f('ix_users_identifier'), 'users', ['identifier'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_identifier'), table_name='users')
    op.drop_table('users')
    op.drop_table('transactions')
    # ### end Alembic commands ###
