"""empty message

Revision ID: 18096f78e6f4
Revises: 7f6c24a0ecb8
Create Date: 2023-11-28 18:47:59.311919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18096f78e6f4'
down_revision = '7f6c24a0ecb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('formacao_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'formacao', ['formacao_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('formacao_id')

    # ### end Alembic commands ###
