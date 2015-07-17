"""empty message

Revision ID: 3ec3c901f083
Revises: cb69836906d
Create Date: 2015-07-15 15:29:19.267546

"""

# revision identifiers, used by Alembic.
revision = '3ec3c901f083'
down_revision = 'cb69836906d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index('ix_roles_default', 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_default', 'roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###
