"""added image color and age column

Revision ID: 6e9c1c9c07cc
Revises: ee4b4b624ee0
Create Date: 2021-02-04 12:04:30.464537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e9c1c9c07cc'
down_revision = 'ee4b4b624ee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('type_coloration', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'type_coloration')
    # ### end Alembic commands ###
