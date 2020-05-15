from django.db.models import OuterRef, Subquery
from django.db import models


class AbstractChainer():
    chain_model = None
    chain_with_model = None
    chain_field = None
    chain_with_field = None
    chain_by_field = None

    def __init__(self, chain_model: models.Model, chain_with_model: models.Model, chain_field: str,
                 chain_with_field: str, chain_by_field: str):
        self.chain_model = chain_model
        self.chain_with_model = chain_with_model
        self.chain_field = chain_field
        self.chain_with_field = chain_with_field
        self.chain_by_field = chain_by_field

    def chain(self):

        sub_query = {
            self.chain_by_field: OuterRef(self.chain_with_field)
        }

        query = {
            self.chain_field: Subquery(
                self.chain_with_model.objects.filter(
                    **sub_query
                ).values('id')[:1]
            )
        }
        self.chain_model.objects.update(**query)
        print(f"{self.chain_model} chaining ended")
