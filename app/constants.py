from enum import Enum

class Defaults(Enum):
    IMAGE = 'properties_default.jpeg'
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

    @property
    def color(self):
        return {
            UserRole.AGENT: "primary",
            UserRole.TENANT: "success",
            UserRole.ADMIN: "dark"
        }[self]

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
    @property
    def color(self):
        return {
            PropertyType.APARTMENT: "primary",
            PropertyType.HOUSE: "success",
            PropertyType.CONDO: "info",
            PropertyType.TOWNHOUSE: "warning",
            PropertyType.STUDIO: "dark",
        }[self]
