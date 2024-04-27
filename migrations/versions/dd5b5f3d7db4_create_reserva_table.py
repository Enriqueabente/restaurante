"""create reserva table

Revision ID: dd5b5f3d7db4
Revises: 
Create Date: 2024-04-27 13:28:44.810794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd5b5f3d7db4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reserva',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('hora', sa.Time(), nullable=True),
    sa.Column('personas', sa.Integer(), nullable=True),
    sa.Column('nombre_cliente', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserva')
    # ### end Alembic commands ###