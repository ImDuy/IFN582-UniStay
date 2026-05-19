from datetime import date
from app.models import *
from app.constants import PropertyType, PropertyAmenity


agent1 = Agent(
    id="A001",
    username="jack_realtor",
    first_name="Jack",
    last_name="Smith",
    email="jack@agency.com",
    phone="0412345678",
    avatar_url="https://api.dicebear.com/7.x/avataaars/svg?seed=Jack"
)

agent2 = Agent(
    id="A002",
    username="sarah_pro",
    first_name="Sarah",
    last_name="Wilson",
    email="sarah@agency.com",
    phone="0488776655"
)

prop1 = Property(
    id="P001",
    title="Modern Studio near UQ",
    address="123 Saint Lucia, Brisbane",
    description= "Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.",
    image_urls=["properties_1.jpeg", "studio2.jpg"],
    amenities=[PropertyAmenity.WIFI],
    documentations=["contract_p1.pdf"],
    property_type=PropertyType.STUDIO, # Studio
    rent_per_week=450.0,
    bedroom_count=1,
    bathroom_count=1,
    living_area=45.5,
    available_date=date(2026, 6, 1),
    rating=4.8,
    agent=agent1
)

prop2 = Property(
    id="P002",
    title="Shared House for Students",
    address="456 Toowong, Brisbane",
    description= "Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.",
    image_urls=["properties_2.jpeg"],
    amenities=[PropertyAmenity.SHARED_KITCHEN],
    documentations=["policy.pdf"],
    property_type=PropertyType.HOUSE,
    rent_per_week=250.0,
    bedroom_count=4,
    bathroom_count=2,
    living_area=120.0,
    available_date=date(2026, 5, 20),
    rating=4.2,
    agent=agent2
)

prop3 = Property(
    id="P003",
    title="Luxury Riverside Studio",
    address="789 Marine Parade, South Bank",
    description="Stunning studio apartment overlooking the Brisbane River. This premium space boasts top-of-the-line appliances, a private balcony, and floor-to-ceiling windows. Residents get exclusive access to the rooftop infinity pool and gym. Perfect for a young professional or couple looking for a vibrant lifestyle.",
    image_urls=["properties_3.jpeg"],
    amenities=[PropertyAmenity.PARKING, PropertyAmenity.WIFI, PropertyAmenity.FITNESS],
    documentations=["contract_p3.pdf"],
    property_type=PropertyType.APARTMENT,
    rent_per_week=550.0,
    bedroom_count=1,
    bathroom_count=1,
    living_area=55.0,
    available_date=date(2026, 6, 1),
    rating=4.8,
    agent=agent1
)

prop4 = Property(
    id="P004",
    title="Spacious Family Home with Backyard",
    address="12 Chelmer Street, Chelmer",
    description="Charming Queenslander home in a quiet, leafy suburb. Features a massive fully-fenced backyard perfect for kids and pets, a massive wrap-around veranda, and character features throughout. Located within a top-tier school catchment zone and just a short walk to the train station.",
    image_urls=["properties_4.jpeg", "properties_4_yard.jpeg"],
    amenities=[PropertyAmenity.PARKING],
    documentations=["pet_policy.pdf"],
    property_type=PropertyType.HOUSE,
    rent_per_week=820.0,
    bedroom_count=4,
    bathroom_count=2.5,
    living_area=210.0,
    available_date=date(2026, 5, 25),
    rating=4.5,
    agent=agent2
)

tenant1 = Tenant(
    id="T001",
    username="minh_nguyen",
    first_name="Minh",
    last_name="Nguyen",
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
    target_property=prop1,
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
