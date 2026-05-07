from enum import Enum

class EnquiryStatus(Enum):
    NEW = 'New'
    RESPONDED = 'Responded'
    CLOSED = 'Closed'

class UserRole(Enum):
    AGENT = 'Agent'
    TENANT = 'Tenant'
    ADMIN = 'Admin'

class PropertyAmenity(Enum):
    WIFI = 'High-Speed Wifi'
    FITNESS = 'Fitness Center'
    PARKING = 'Parking Space'
    SHARED_KITCHEN = 'Shared Kitchen'
