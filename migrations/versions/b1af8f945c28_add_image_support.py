"""add image support

Revision ID: b1af8f945c28
Revises: c97738754f43
Create Date: 2020-06-30 19:56:39.044438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1af8f945c28'
down_revision = 'c97738754f43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('image_filename', sa.String(), nullable=True))
    op.add_column('plant', sa.Column('image_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plant', 'image_url')
    op.drop_column('plant', 'image_filename')
    # ### end Alembic commands ###
