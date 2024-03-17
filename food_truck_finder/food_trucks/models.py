from mongoengine import Document, StringField, ListField, DictField, PointField

class FoodTruck(Document):
    name = StringField(required=True)
    facility_type = StringField(required=True)
    location_description = StringField(required=True)
    address = StringField(required=True)
    permit = StringField(required=True)
    status = StringField(required=True)
    food_items = ListField(StringField())
    location = PointField(auto_index=False, required=True)
    open_hours = DictField()

    def __str__(self):
        return self.name