"""empty message

Revision ID: 431a5a6e0b2d
Revises: 36b93d81ad60
Create Date: 2015-03-02 14:07:45.164719

"""

# revision identifiers, used by Alembic.
revision = '431a5a6e0b2d'
down_revision = '36b93d81ad60'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('card_number', sa.String(length=32), nullable=True))
    op.create_index('ix_users_card_number', 'users', ['card_number'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_card_number', table_name='users')
    op.drop_column('users', 'card_number')
    ### end Alembic commands ###
