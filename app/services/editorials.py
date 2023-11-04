from app.models.editorials import Editorial


class EditorialsService:
    def __init__(self):
        pass

    def get_items(self, limit: int = 30, offset: int = 0):
        return Editorial.get_items(limit, offset)

    def get_item(self, item_id: int):
        return Editorial.get_item(item_id)

    def create(self, data: dict):
        return Editorial.create(data)

    def update(self, item_id: int, data: dict):
        return Editorial.update(item_id, data)

    def delete(self, item_id: int):
        return Editorial.delete(item_id)


editorialsService = EditorialsService()
