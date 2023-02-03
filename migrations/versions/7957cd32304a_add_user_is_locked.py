"""add user.is_locked

Revision ID: 7957cd32304a
Revises: 
Create Date: 2023-02-03 22:41:32.165406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7957cd32304a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_locked', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_locked')

    # ### end Alembic commands ###