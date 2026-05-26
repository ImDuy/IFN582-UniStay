from datetime import date
import uuid
from app.models import *
from app.constants import PropertyType, PropertyAmenity
import uuid
from . import mysql


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
    rent_per_week=450,
    bedroom_count=1,
    bathroom_count=1,
    living_area=45.5,
    available_date=date(2026, 6, 1),
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
    rent_per_week=250,
    bedroom_count=4,
    bathroom_count=2,
    living_area=120.0,
    available_date=date(2026, 5, 20),
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
    rent_per_week=550,
    bedroom_count=1,
    bathroom_count=1,
    living_area=55.0,
    available_date=date(2026, 6, 1),
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
    rent_per_week=820,
    bedroom_count=4,
    bathroom_count=2,
    living_area=210.0,
    available_date=date(2026, 5, 25),
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

# enquiry1 = Enquiry(
#     id="E001",
#     sender=tenant1,
#     target_property=prop1,
#     status= EnquiryStatus.NEW
# )

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
# mockEnquiries = [enquiry1]
mockUniversities = [uni1, uni2]
mockNearby = [nearby1, nearby2, nearby3]

def get_properties_by_agent(agent_id):
    cur = mysql.connection.cursor()
    # fetch properties and their corresponding agents
    cur.execute("""SELECT p.id as p_id, p.title, p.address,
        p.description, p.propertyType, p.rentPerWeek, p.numBedrooms, 
        p.numBathrooms, p.livingArea, p.availableDate,
        u.id AS u_id, u.username, u.firstName, u.lastName,
        u.email, u.phone, u.avatarUrl, u.role  
        FROM property p JOIN user u ON p.agentId = u.id
        WHERE p.agentId = %s""", (agent_id,))
    results = cur.fetchall()

    properties = []
    for row in results:
        # for each property, fetch its associated amenities, images and documents
        property_id = row['p_id']
        # amenities
        cur.execute(
            "SELECT amenity FROM propertyAmenity WHERE propertyId = %s",
            (property_id,)
        )
        amenities = [PropertyAmenity(r["amenity"]) for r in cur.fetchall()]
        # images
        cur.execute(
            "SELECT url, isPrimary FROM propertyImage WHERE propertyId = %s",
            (property_id,)
        )
        primary_image_url = next((r["url"] for r in cur.fetchall() if r["isPrimary"]), Defaults.IMAGE.value)
        gallery_image_urls = [r["url"] for r in cur.fetchall() if not r["isPrimary"]]
        # documents
        cur.execute(
            "SELECT url FROM propertyDocumentation WHERE propertyId = %s",
            (property_id,)
        )
        documents = [r["url"] for r in cur.fetchall()]

        prop = Property(
            id=str(property_id),
            title=row["title"],
            address=row["address"],
            description=row["description"],
            property_type=PropertyType(row["propertyType"]),
            rent_per_week=row["rentPerWeek"],
            bedroom_count=row["numBedrooms"],
            bathroom_count=row["numBathrooms"],
            living_area=row["livingArea"],
            available_date=row["availableDate"],
            amenities=amenities,
            primary_image_url=primary_image_url,
            image_urls= gallery_image_urls,
            documentations=documents if documents else [Defaults.DOCUMENT.value],
            agent=Agent(id=str(row['u_id']),username=row['username'], first_name=row['firstName'], 
                        last_name=row['lastName'], email=row['email'], phone=row['phone'], 
                        avatar_url=row['avatarUrl'] if 'avatarUrl' in row else '',)
        )
        
        # enquiries
        cur.execute("""SELECT e.senderId as tenant_id, e.submittedDate, e.status, e.message,
                    u.username, u.firstName, u.lastName, u.email, u.phone, u.avatarUrl
                    FROM enquiry e
                    JOIN user u ON e.senderId = u.id
                    WHERE e.targetPropertyId = %s
                    ORDER BY 
                        FIELD(e.status, 'New', 'Responded', 'Closed'),
                        e.submittedDate DESC""", (property_id,))
        prop.enquiries = [Enquiry(id = str(uuid.uuid4()), # since enquiry contains composite PK in database, we use the uuid to create unique id in the conceptual model
                    sender= Tenant(str(row['tenant_id']), row['username'], row['firstName'], row['lastName'], row['email'], row['phone'], row['avatarUrl']),
                    message= row['message'],
                    status= EnquiryStatus(row['status']),
                    created_at=row['submittedDate']) for row in cur.fetchall()]
        # offers 
        cur.execute("""SELECT o.senderId as tenant_id, o.submittedDate, o.status,
            u.username, u.firstName, u.lastName, u.email, u.phone, u.avatarUrl
            FROM offer o
            JOIN user u ON o.senderId = u.id
            WHERE o.targetPropertyId = %s
            ORDER BY 
                FIELD(o.status, 'Pending', 'Accepted', 'Rejected'),
                o.submittedDate DESC""", (property_id,))
        prop.offers = [Offer(id = str(uuid.uuid4()), # since enquiry contains composite PK in database, we use the uuid to create unique id in the conceptual model
            sender= Tenant(str(row['tenant_id']), row['username'], row['firstName'], row['lastName'], row['email'], row['phone'], row['avatarUrl']),
            status= OfferStatus(row['status']),
            created_at=row['submittedDate']) for row in cur.fetchall()]

        properties.append(prop)

    cur.close()
    return properties

def get_all_properties():
    # this is for admin -> no need to fetch associated enquiry data for each property
    return mockProperties

def add_property(form, agent_id):
    cur = mysql.connection.cursor()
    # insert property record
    cur.execute(""" INSERT INTO property (
                title, address, description, propertyType, rentPerWeek,
                numBedrooms, numBathrooms, livingArea, availableDate, agentId
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, ( form.title.data, form.address.data, form.description.data,
            form.property_type.data.value, form.rent_per_week.data, form.bedroom_count.data,
            form.bathroom_count.data, form.living_area.data, form.available_date.data,
            agent_id
        ))
    
    # insert amenity records
    amenities = form.amenities.data
    print(amenities)
    property_id = cur.lastrowid # get the id of the inserted property
    for amenity in amenities:
        cur.execute("""INSERT INTO propertyAmenity(propertyId, amenity)
                    VALUES (%s, %s)""", (property_id, amenity.value))
    
    mysql.connection.commit()
    cur.close()

def update_property(property_id, form):
    cur = mysql.connection.cursor()
    # update property info
    cur.execute(""" UPDATE property SET 
                title = %s, address = %s, description = %s, propertyType = %s, rentPerWeek = %s,
                numBedrooms = %s, numBathrooms = %s, livingArea = %s, availableDate = %s
                WHERE id = %s""", 
        ( form.title.data, form.address.data, form.description.data,
            form.property_type.data.value, form.rent_per_week.data, form.bedroom_count.data,
            form.bathroom_count.data, form.living_area.data, form.available_date.data, property_id))
    
    # update amenity info by deleting all and inserting new ones
    cur.execute(
        "DELETE FROM propertyAmenity WHERE propertyId = %s",
        (property_id,)
    )
    amenities = form.amenities.data
    for amenity in amenities:
        cur.execute("""INSERT INTO propertyAmenity(propertyId, amenity)
                    VALUES (%s, %s)""", (property_id, amenity.value))
    
    mysql.connection.commit()
    cur.close()
    
def delete_property(property_id):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM property WHERE id = %s", (property_id))
    # amenities, images, documents are also deleted in database with ON DELETE CASCADE 

    mysql.connection.commit()
    cur.close()

def update_enquiries_by_property(property_id, form):
    cur = mysql.connection.cursor()
    for enquiry_form in form.enquiries:
        cur.execute("""UPDATE enquiry SET status = %s
            WHERE senderId = %s AND targetPropertyId = %s""", 
            ( enquiry_form.status.data, enquiry_form.tenant_id.data, property_id))
    mysql.connection.commit()
    cur.close()

def update_offers_by_property(property_id, form):
    cur = mysql.connection.cursor()
    for offer_form in form.offers:
        cur.execute("""UPDATE offer SET status = %s
            WHERE senderId = %s AND targetPropertyId = %s""", 
            ( offer_form.status.data, offer_form.tenant_id.data, property_id))
    mysql.connection.commit()
    cur.close()

def get_nearby():
    return mockNearby

def get_university():
    return mockUniversities

def get_properties_by_university(uni_name):
    uq_properties = [prop1, prop2]
    qut_properties = [prop3]
    griffith_properties = [prop4]

    if uni_name == "uq":
        return uq_properties
    elif uni_name == "qut":
        return qut_properties
    elif uni_name == "griffith":
        return griffith_properties
    return mockProperties

def search_properties(query):
    query = query.lower()
    results = []
    for property in mockProperties:
        if (query in property.title.lower() or 
            query in property.address.lower()):
            results.append(property)
    return results

def get_properties_by_bookmark(user_id):
    
    cursor = mysql.connection.cursor()

    cursor.execute('select * from unistay.bookmark a join unistay.property b on a.propertyId = b.id where tenantId =  %s',(user_id,))

    results = cursor.fetchall()
    cursor.close()
    return  [
        Bookmark(
            id=str(row['id']),
            tenant=Tenant(
                id=str(row['tenantId']),                  
                username="",
                first_name="",
                last_name="",
                email="",
                phone=""),
            property=Property(
                id=str(row['propertyId']),
                title=row['title'],
                address=row['address'],
                description=row['description'],
                amenities=[],
                property_type=None,
                rent_per_week=row['rentPerWeek'],
                bedroom_count=row['numBedrooms'],
                bathroom_count=row['numBathrooms'],
                living_area=float(row['livingArea']),
                available_date=None,
                agent=None,
                image_urls=[]
            ),
            note=row.get('note', ''),
            created_at=row.get('createdAt')
        )
        for row in results
    ]
    
def delete_bookmarks(property_id):
    pass

# fetch props and filter by q
def get_all_properties_db(q=None):
    cur = mysql.connection.cursor()
    if q:
        cur.execute("SELECT * FROM property WHERE title LIKE %s OR address LIKE %s",
                    (f'%{q}%', f'%{q}%'))
    else:
        cur.execute("SELECT * FROM property")
    result = cur.fetchall()
    cur.close()
    return result

# fetch all uni
def get_universities_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM university")
    result = cur.fetchall()
    cur.close()
    return result

# fetch images for each prop, return {propertyId: url}
def get_image_map_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT propertyId, url FROM propertyImage WHERE isPrimary = 1")
    images = cur.fetchall()
    cur.close()
    image_map = {}
    for img in images:
        image_map[img['propertyId']] = img['url']
    return image_map

# nearby unis for each prop 
def get_nearby_db():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT n.propertyId, n.universityId, n.distance, u.name as universityName
        FROM nearby n
        JOIN university u ON n.universityId = u.id
    """)
    result = cur.fetchall()
    cur.close()
    # {propertyId: [list of nearby]}
    nearby_map = {}
    for n in result:
        pid = n['propertyId']
        if pid not in nearby_map:
            nearby_map[pid] = []
        nearby_map[pid].append(n)
    return nearby_map