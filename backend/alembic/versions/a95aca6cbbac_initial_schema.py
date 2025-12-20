"""initial schema

Revision ID: a95aca6cbbac
Revises: 
Create Date: 2025-12-20 22:49:13.376476

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a95aca6cbbac'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('first_name', sa.String(255), nullable=False),
        sa.Column('middle_name', sa.String(255), nullable=True),
        sa.Column('last_name', sa.String(255), nullable=False),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('avatar_path', sa.String(255), nullable=True),
        sa.Column('points', sa.Integer(), server_default='0', nullable=False),
        sa.Column('permission', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('email')
    )

    op.create_table(
        'event',
        sa.Column('event_id', sa.Uuid(), nullable=False),
        sa.Column('event_name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('acceptation_status', sa.String(255), server_default='PENDING', nullable=False),
        sa.Column('starts_at', sa.DateTime(), nullable=False),
        sa.Column('ends_at', sa.DateTime(), nullable=False),
        sa.Column('min_count_of_volunteers', sa.Integer(), nullable=True),
        sa.Column('max_count_of_volunteers', sa.Integer(), nullable=True),
        sa.Column('image_path', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('event_id')
    )

    op.create_table(
        'event_tag',
        sa.Column('event_category_id', sa.Uuid(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('event_category_id')
    )

    op.create_table(
        'event_tag_attachment',
        sa.Column('event_category_id', sa.Uuid(), nullable=False),
        sa.Column('event_id', sa.Uuid(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['event_category_id'], ['event_tag.event_category_id'], ),
        sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
        sa.PrimaryKeyConstraint('event_category_id', 'event_id')
    )

    op.create_table(
        'event_member',
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('event_id', sa.Uuid(), nullable=False),
        sa.Column('role', sa.String(50), nullable=False), # volunteer, organizer
        sa.Column('acceptation_status', sa.String(255), server_default='PENDING', nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('user_id', 'event_id')
    )

    op.create_table(
        'event_archive_storage',
        sa.Column('event_archive_storage_id', sa.Uuid(), nullable=False),
        sa.Column('event_id', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('acceptation_status', sa.String(255), nullable=False),
        sa.Column('url', sa.String(255), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('event_archive_storage_id')
    )

    op.create_table(
        'event_feedback',
        sa.Column('event_feedback_id', sa.Uuid(), nullable=False),
        sa.Column('event_id', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Uuid(), nullable=True),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('rate', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('event_feedback_id')
    )

    op.create_table(
        'event_public_feedback_form',
        sa.Column('event_id', sa.Uuid(), nullable=False),
        sa.Column('identifier', sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
        sa.UniqueConstraint('identifier'),
        sa.PrimaryKeyConstraint('event_id')
    )

    op.create_table(
        'shop_item',
        sa.Column('shop_item_id', sa.Uuid(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('cost', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('shop_item_id')
    )

    op.create_table(
        'shop_order',
        sa.Column('shop_order_id', sa.Uuid(), nullable=False),
        sa.Column('ordered_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('shop_order_id')
    )

    op.create_table(
        'shop_cart_item',
        sa.Column('shop_cart_item_id', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('shop_item_id', sa.Uuid(), nullable=False),
        sa.Column('shop_order_id', sa.Uuid(), nullable=True),
        sa.Column('amount', sa.Integer(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['shop_item_id'], ['shop_item.shop_item_id'], ),
        sa.ForeignKeyConstraint(['shop_order_id'], ['shop_order.shop_order_id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('shop_cart_item_id')
    )

def downgrade():
    op.drop_table('shop_cart_item')
    op.drop_table('shop_order')
    op.drop_table('shop_item')
    op.drop_table('event_public_feedback_form')
    op.drop_table('event_feedback')
    op.drop_table('event_archive_storage')
    op.drop_table('event_member')
    op.drop_table('event_tag_attachment')
    op.drop_table('event_tag')
    op.drop_table('event')
    op.drop_table('user')
