from datetime import date
from app.models import *
from app.constants import PropertyTypes, PropertyAmenity


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
    description= "Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.",
    imageUrls=["img/properties_1.jpeg", "studio2.jpg"],
    amenities=[PropertyAmenity.WIFI],
    documentations=["contract_p1.pdf"],
    propertyType=PropertyTypes.STUDIO, # Studio
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
    description= "Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.",
    imageUrls=["img/properties_2.jpeg"],
    amenities=[PropertyAmenity.SHARED_KITCHEN],
    documentations=["policy.pdf"],
    propertyType=PropertyTypes.HOUSE,
    rentPerWeek=250.0,
    numBedrooms=4,
    numBathrooms=2,
    livingArea=120.0,
    availableDate=date(2026, 5, 20),
    rating=4.2,
    agent=agent2
)

prop3 = Property(
    id="P003",
    title="Luxury Riverside Studio",
    address="789 Marine Parade, South Bank",
    description="Stunning studio apartment overlooking the Brisbane River. This premium space boasts top-of-the-line appliances, a private balcony, and floor-to-ceiling windows. Residents get exclusive access to the rooftop infinity pool and gym. Perfect for a young professional or couple looking for a vibrant lifestyle.",
    imageUrls=["img/properties_3.jpeg"],
    amenities=[PropertyAmenity.PARKING, PropertyAmenity.WIFI, PropertyAmenity.FITNESS],
    documentations=["contract_p3.pdf"],
    propertyType=PropertyTypes.APARTMENT,
    rentPerWeek=550.0,
    numBedrooms=1,
    numBathrooms=1,
    livingArea=55.0,
    availableDate=date(2026, 6, 1),
    rating=4.8,
    agent=agent1
)

prop4 = Property(
    id="P004",
    title="Spacious Family Home with Backyard",
    address="12 Chelmer Street, Chelmer",
    description="Charming Queenslander home in a quiet, leafy suburb. Features a massive fully-fenced backyard perfect for kids and pets, a massive wrap-around veranda, and character features throughout. Located within a top-tier school catchment zone and just a short walk to the train station.",
    imageUrls=["img/properties_4.jpeg", "img/properties_4_yard.jpeg"],
    amenities=[PropertyAmenity.PARKING],
    documentations=["pet_policy.pdf"],
    propertyType=PropertyTypes.HOUSE,
    rentPerWeek=820.0,
    numBedrooms=4,
    numBathrooms=2.5,
    livingArea=210.0,
    availableDate=date(2026, 5, 25),
    rating=4.5,
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
mockProperties = [prop1, prop2, prop3, prop4]
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
