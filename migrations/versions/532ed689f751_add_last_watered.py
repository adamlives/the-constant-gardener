"""add last watered

Revision ID: 532ed689f751
Revises: 7df050595e38
Create Date: 2020-06-28 21:09:36.454128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532ed689f751'
down_revision = '7df050595e38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('last_watered', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_plant_last_watered'), 'plant', ['last_watered'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_plant_last_watered'), table_name='plant')
    op.drop_column('plant', 'last_watered')
    # ### end Alembic commands ###
