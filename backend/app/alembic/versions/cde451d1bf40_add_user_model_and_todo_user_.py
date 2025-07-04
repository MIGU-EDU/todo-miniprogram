"""Add user model and todo user relationship

Revision ID: cde451d1bf40
Revises: 
Create Date: 2025-06-16 21:59:57.793714

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'cde451d1bf40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('openid', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('nickname', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=True),
    sa.Column('avatar_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_openid'), 'users', ['openid'], unique=True)
    op.add_column('todos', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'todos', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'user_id')
    op.drop_index(op.f('ix_users_openid'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
