"""empty message

Revision ID: 60d91e3cf3a5
Revises: 
Create Date: 2022-11-14 14:52:45.763552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d91e3cf3a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=True),
    sa.Column('artist_spotify_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artists_artist_name'), 'artists', ['artist_name'], unique=True)
    op.create_index(op.f('ix_artists_artist_spotify_id'), 'artists', ['artist_spotify_id'], unique=True)
    op.create_index(op.f('ix_artists_id'), 'artists', ['id'], unique=False)
    op.create_table('user_artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_artists_artist_id'), 'user_artists', ['artist_id'], unique=False)
    op.create_index(op.f('ix_user_artists_id'), 'user_artists', ['id'], unique=False)
    op.create_index(op.f('ix_user_artists_user_id'), 'user_artists', ['user_id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_index(op.f('ix_user_artists_user_id'), table_name='user_artists')
    op.drop_index(op.f('ix_user_artists_id'), table_name='user_artists')
    op.drop_index(op.f('ix_user_artists_artist_id'), table_name='user_artists')
    op.drop_table('user_artists')
    op.drop_index(op.f('ix_artists_id'), table_name='artists')
    op.drop_index(op.f('ix_artists_artist_spotify_id'), table_name='artists')
    op.drop_index(op.f('ix_artists_artist_name'), table_name='artists')
    op.drop_table('artists')
    # ### end Alembic commands ###