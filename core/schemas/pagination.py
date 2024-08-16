from pydantic import BaseModel


class Pagination(BaseModel):
    per_page: int
    page: int
