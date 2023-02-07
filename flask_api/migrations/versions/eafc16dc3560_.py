"""empty message

Revision ID: eafc16dc3560
Revises: cb878c77852f
Create Date: 2023-02-06 13:47:30.530438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eafc16dc3560'
down_revision = 'cb878c77852f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('book_url',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('book_url',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###