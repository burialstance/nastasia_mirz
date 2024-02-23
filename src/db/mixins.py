import datetime
from typing import Optional

import humanize
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class Timestamped(object):
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=lambda: datetime.datetime.now(tz=None),
        server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(onupdate=func.now(), nullable=True)

    @property
    def created_at_humanize(self) -> str:
        if self.created_at:
            return humanize.naturaltime(self.created_at)

    @property
    def updated_at_humanize(self) -> str:
        if self.updated_at:
            return humanize.naturaltime(self.updated_at)
