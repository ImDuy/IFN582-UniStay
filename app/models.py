from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List
from app.constants import EnquiryStatus, PropertyAmenity

@dataclass
class User:
    id: str
    username: str
    firstName: str
    lastName: str
    email: str
    phone: str
    avatarUrl: str | None = None

    def register(self):
        pass
    def login(self):
        pass
    def logout(self):
        pass
    def search_property(self):
        pass
@dataclass
class Agent(User):
    # Agent inherits from User (so it has all the attributes and methods from User)
    def add_new_property(self):
        pass
    def edit_property(self):
        pass
    def delete_property(self):
        pass
    def get_managed_properties(self):
        pass

@dataclass
class Property:
    id: str
    title: str
    address: str
    imageUrls: List[str]
    amenities: List[PropertyAmenity]
    documentations: List[str]
    propertyType: int
    rentPerWeek: float
    numBedrooms: int
    numBathrooms: int
    livingArea: float
    availableDate: date
    rating: float
    agent: Agent  # the agent who manages this property

    def get_nearby_universities(self):
        # this one is to show nearby universities in the property details page
        # as we dont really implement any distance calculation feature, we gonna create a nearby table in the database and get the nearby data from that
        pass



@dataclass
class Tenant(User):
    # Tenant inherits from User (so it has all the attributes and methods from User)
    def get_bookmarked_properties(self):
        pass
    def bookmark_property(self): # add new bookmark item
        pass
    def edit_bookmark(self): # just edit bookmark note
        pass
    def remove_bookmark(self):
        pass
    def submit_enquiry(self): # add new enquiry item
        pass

@dataclass
class Enquiry:
    id: str
    sender: Tenant
    targetProperty: Property
    status: EnquiryStatus
    submittedDate: datetime = datetime.now()

@dataclass
class Bookmark:
    id: str
    tenant: Tenant
    property: Property
    note: str
    createdAt: datetime = datetime.now()

@dataclass
class University:
    id: str
    name: str
    address: str

    def get_nearby_properties(self):
        # this one is to show nearby properties for each university in the home page
        # as we dont really implement any distance calculation feature, we gonna create a nearby table in the database and get the nearby data from that
        pass

