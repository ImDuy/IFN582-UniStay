from datetime import date
from app.models import *

agent1 = Agent(
    id="A001",
    username="jack_realtor",
    firstName="Jack",
    lastName="Smith",
    email="jack@agency.com",
    phone="0412345678",
    avatarUrl="https://api.dicebear.com/7.x/avataaars/svg?seed=Jack"
)

agent2 = Agent(
    id="A002",
    username="sarah_pro",
    firstName="Sarah",
    lastName="Wilson",
    email="sarah@agency.com",
    phone="0488776655"
)

prop1 = Property(
    id="P001",
    title="Modern Studio near UQ",
    address="123 Saint Lucia, Brisbane",
    imageUrls=["studio1.jpg", "studio2.jpg"],
    amenities=["Wifi", "Gym", "AirCon"],
    documentations=["contract_p1.pdf"],
    propertyType=1,
    rentPerWeek=450.0,
    numBedrooms=1,
    numBathrooms=1,
    livingArea=45.5,
    availableDate=date(2026, 6, 1),
    rating=4.8,
    agent=agent1
)

prop2 = Property(
    id="P002",
    title="Shared House for Students",
    address="456 Toowong, Brisbane",
    imageUrls=["house1.jpg"],
    amenities=["Laundry", "Kitchen"],
    documentations=["policy.pdf"],
    propertyType=2, # House
    rentPerWeek=250.0,
    numBedrooms=4,
    numBathrooms=2,
    livingArea=120.0,
    availableDate=date(2026, 5, 20),
    rating=4.2,
    agent=agent2
)

tenant1 = Tenant(
    id="T001",
    username="minh_nguyen",
    firstName="Minh",
    lastName="Nguyen",
    email="minh@student.edu.au",
    phone="0411223344"
)

bookmark1 = Bookmark(
    id="B001",
    tenant=tenant1,
    property=prop1,
    note="Very close to my campus",
)

enquiry1 = Enquiry(
    id="E001",
    sender=tenant1,
    targetProperty=prop1,
    status= EnquiryStatus.NEW
)

uni1 = University(
    id="U001",
    name="University of Queensland",
    address="St Lucia QLD 4072"
)

uni2 = University(
    id="U002",
    name="QUT",
    address="Gardent Point Rd"
)
nearby1 = Nearby(
    id="N001",
    property=prop1,
    university=uni1,
    distance=0.5
)

nearby2 = Nearby(
    id="N002",
    property=prop1,
    university=uni1,
    distance=7.2
)

nearby3 = Nearby(
    id="N003",
    property=prop2,
    university=uni1,
    distance=1.2
)

mockAgents = [agent1, agent2]
mockProperties = [prop1, prop2]
mockTenants = [tenant1]
mockBookmarks = [bookmark1]
mockEnquiries = [enquiry1]
mockUniversities = [uni1, uni2]
mockNearby = [nearby1, nearby2, nearby3]

def get_properties_by_agent(agentId):
    agentId = str(agentId)
    return [prop for prop in mockProperties if prop.agent.id == agentId]

def get_all_properties():
    return mockProperties