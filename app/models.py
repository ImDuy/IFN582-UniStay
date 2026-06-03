from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List
from app.constants import Defaults, EnquiryStatus, OfferStatus, PropertyAmenity, PropertyType, UserRole

@dataclass
class User:
    id: str
    username: str
    first_name: str
    last_name: str
    email: str
    phone: str
    role: UserRole  # use 'role' attribute to indicate user role instead of generalization so we dont need to map to the correct role class when fetching from db
    avatar_url: str | None = None

@dataclass
class Enquiry:
    id: str
    sender: User
    status: EnquiryStatus
    message: str
    created_at: datetime = field(default_factory=lambda: datetime.now())

@dataclass
class Offer:
    id: str
    sender: User
    status: OfferStatus
    created_at: datetime = field(default_factory=lambda: datetime.now())

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
    agent: User  # the agent who manages this property

    primary_image_url: str = Defaults.IMAGE.value # primary images
    image_urls: List[str] = field(default_factory=list) # this one is for gallery images
    amenities: List[PropertyAmenity] = field(default_factory=list)
    documentations: List[str] = field(default_factory=lambda: [Defaults.DOCUMENT.value])

    # these attributes are for showing on listings page only, other pages no need to use them
    enquiries: List[Enquiry] = field(default_factory=list)
    offers: List[Offer] = field(default_factory=list)
    @property
    def new_enquiry_count(self):
        count = 0
        for enquiry in self.enquiries:
            if enquiry.status == EnquiryStatus.NEW:
                count +=1
        return count
    @property
    def pending_offer_count(self):
        count = 0
        for offer in self.offers:
            if offer.status == OfferStatus.PENDING:
                count +=1
        return count
    @staticmethod
    def get_total_new_enquiries(properties):
        count = 0
        for property in properties:
            count += property.new_enquiry_count
        return count
    @staticmethod
    def get_total_pending_offers(properties):
        count = 0
        for property in properties:
            count += property.pending_offer_count
        return count

    def get_nearby_universities(self):
        # this one is to show nearby universities in the property details page
        # as we dont really implement any distance calculation feature, we gonna create a nearby table in the database and get the nearby data from that
        pass


@dataclass
class Bookmark:
    id: str
    tenantId: str
    property: Property
    note: str
    created_at: datetime = field(default_factory=lambda: datetime.now())

@dataclass
class University:
    id: str
    name: str
    address: str
    logoUrl: str | None = None

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
