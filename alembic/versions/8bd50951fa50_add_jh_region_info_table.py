"""Add JH region info table that is in sync with the official lookup table

Revision ID: 8bd50951fa50
Revises: 8497fb70170b
Create Date: 2020-04-17 13:17:58.486861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bd50951fa50'
down_revision = '8497fb70170b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jh_region_info',
    sa.Column('jh_id', sa.Integer(), nullable=False),
    sa.Column('scope', sa.Enum('COUNTRY_REGION', 'PROVINCE_STATE', 'ADMIN2', name='scope'), nullable=True),
    sa.Column('country_code_iso2', sa.String(length=2), nullable=True),
    sa.Column('country_code_iso3', sa.String(length=3), nullable=True),
    sa.Column('country_region', sa.String(), nullable=True),
    sa.Column('province_state', sa.String(), nullable=True),
    sa.Column('fips', sa.String(), nullable=True),
    sa.Column('admin2', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('jh_id')
    )
    op.create_index(op.f('ix_jh_region_info_jh_id'), 'jh_region_info', ['jh_id'], unique=False)
    op.add_column('jh_daily_reports', sa.Column('jh_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'jh_daily_reports', 'jh_region_info', ['jh_id'], ['jh_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jh_daily_reports', type_='foreignkey')
    op.drop_column('jh_daily_reports', 'jh_id')
    op.drop_index(op.f('ix_jh_region_info_jh_id'), table_name='jh_region_info')
    op.drop_table('jh_region_info')
    # ### end Alembic commands ###