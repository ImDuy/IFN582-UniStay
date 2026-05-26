from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List
from app.constants import Defaults, EnquiryStatus, PropertyAmenity, PropertyType

@dataclass
class User:
    id: str
    username: str
    first_name: str
    last_name: str
    email: str
    phone: str
    avatar_url: str | None = None

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
    # target_property: Property
    status: EnquiryStatus
    message: str
    created_at: datetime = datetime.now()

@dataclass
class Property:
    id: str
    title: str
    address: str
    description: str
    property_type: PropertyType
    rent_per_week: int
    bedroom_count: int
    bathroom_count: int
    living_area: float
    available_date: date
    agent: Agent  # the agent who manages this property

    primary_image_url: str = Defaults.IMAGE.value # primary images
    image_urls: List[str] = field(default_factory=lambda: list) # this one is for gallery images
    amenities: List[PropertyAmenity] = field(default_factory=list)
    documentations: List[str] = field(default_factory=lambda: [Defaults.DOCUMENT.value])

    # these attributes are for showing on listings page only, other pages no need to use them
    enquiries: List[Enquiry] = field(default_factory=lambda: list)
    @property
    def new_enquiry_count(self):
        count = 0
        for enquiry in self.enquiries:
            if enquiry.status == EnquiryStatus.NEW:
                count +=1
        return count

    def get_nearby_universities(self):
        # this one is to show nearby universities in the property details page
        # as we dont really implement any distance calculation feature, we gonna create a nearby table in the database and get the nearby data from that
        pass


@dataclass
class Bookmark:
    id: str
    tenant: Tenant
    property: Property
    note: str
    created_at: datetime = datetime.now()

@dataclass
class University:
    id: str
    name: str
    address: str

    def get_nearby_properties(self):
        # this one is to show nearby properties for each university in the home page
        # as we dont really implement any distance calculation feature, we gonna create a nearby table in the database and get the nearby data from that
        pass


@dataclass
class Nearby:
    id: str
    property: Property
    university: University
    distance: float = 0
