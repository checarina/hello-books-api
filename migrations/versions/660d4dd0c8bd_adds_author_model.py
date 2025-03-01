"""adds Author model

Revision ID: 660d4dd0c8bd
Revises: fb6fd11367a1
Create Date: 2022-11-06 21:14:58.408290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660d4dd0c8bd'
down_revision = 'fb6fd11367a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('book', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'author', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'author_id')
    op.drop_table('author')
    # ### end Alembic commands ###
