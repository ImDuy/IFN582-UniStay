from enum import Enum

class Defaults(Enum):
    IMAGE = 'properties_1.jpeg'
    DOCUMENT = 'documentation_1.pdf'

class EnquiryStatus(Enum):
    NEW = 'New'
    RESPONDED = 'Responded'
    CLOSED = 'Closed'

class OfferStatus(Enum):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'

class UserRole(Enum):
    AGENT = 'Agent'
    TENANT = 'Tenant'
    ADMIN = 'Admin'

class PropertyAmenity(Enum):
    WIFI = 'High-Speed Wifi'
    FITNESS = 'Fitness Center'
    PARKING = 'Parking Space'
    SHARED_KITCHEN = 'Shared Kitchen'

class PropertyType(Enum):
    APARTMENT = 'Apartment'
    HOUSE = 'House'
    CONDO = 'Condo'
    TOWNHOUSE = 'Townhouse'
    STUDIO = 'Studio'
