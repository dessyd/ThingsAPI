"""Create tables

Revision ID: 418da238a359
Revises: 01d7ab236560
Create Date: 2021-12-02 10:41:11.180611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418da238a359'
down_revision = '01d7ab236560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table_comment(
        'sensors',
        'one record per sensor intalled on each thing',
        existing_comment='one record per sensor intalled on each things',
        schema=None
    )
    op.alter_column('things', 'id',
               existing_type=sa.INTEGER(),
               comment='used internally only',
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('things', 'physical_id',
               existing_type=sa.VARCHAR(),
               comment='usually the MAC address',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('things', 'physical_id',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='usually the MAC address',
               existing_nullable=False)
    op.alter_column('things', 'id',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='used internally only',
               existing_nullable=False,
               autoincrement=True)
    op.create_table_comment(
        'sensors',
        'one record per sensor intalled on each things',
        existing_comment='one record per sensor intalled on each thing',
        schema=None
    )
    # ### end Alembic commands ###
