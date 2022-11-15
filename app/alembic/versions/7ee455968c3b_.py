"""empty message

Revision ID: 7ee455968c3b
Revises: 686d98beee3b
Create Date: 2022-11-15 10:47:21.061757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ee455968c3b'
down_revision = '686d98beee3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('image_url', sa.String(), nullable=True))
    op.create_index(op.f('ix_artists_image_url'), 'artists', ['image_url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_artists_image_url'), table_name='artists')
    op.drop_column('artists', 'image_url')
    # ### end Alembic commands ###
