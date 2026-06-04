from datetime import date
import uuid
from app.models import *
from app.constants import PropertyType, PropertyAmenity
import uuid
from . import mysql

def get_properties_by_agent(agent_id):
    cur = mysql.connection.cursor()
    # fetch properties and their corresponding agents
    cur.execute("""SELECT p.id as p_id, p.title, p.address,
        p.description, p.propertyType, p.rentPerWeek, p.numBedrooms, 
        p.numBathrooms, p.livingArea, p.availableDate,
        u.id AS u_id, u.username, u.firstName, u.lastName,
        u.email, u.phone, u.avatarUrl, u.role  
        FROM property p JOIN user u ON p.agentId = u.id
        WHERE p.agentId = %s ORDER BY p.id DESC""", (agent_id,))
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
            agent=User(id=str(row['u_id']),username=row['username'], first_name=row['firstName'], 
                        last_name=row['lastName'], email=row['email'], phone=row['phone'],
                        role=UserRole(row['role']),
                        avatar_url=row['avatarUrl'] if 'avatarUrl' in row else '',)
        )
        # enquiries
        cur.execute("""SELECT e.senderId as tenant_id, e.submittedDate, e.status, e.message,
                    u.username, u.firstName, u.lastName, u.email, u.phone, u.avatarUrl, u.role
                    FROM enquiry e
                    JOIN user u ON e.senderId = u.id
                    WHERE e.targetPropertyId = %s
                    ORDER BY 
                        FIELD(e.status, 'New', 'Responded', 'Closed'),
                        e.submittedDate DESC""", (property_id,))
        prop.enquiries = [Enquiry(id = str(uuid.uuid4()), # since enquiry contains composite PK in database, we use the uuid to create unique id in the conceptual model
                    sender= User(str(row['tenant_id']), row['username'], row['firstName'], row['lastName'], row['email'], row['phone'], UserRole(row['role']), row['avatarUrl']),
                    message= row['message'],
                    status= EnquiryStatus(row['status']),
                    created_at=row['submittedDate']) for row in cur.fetchall()]
        # offers 
        cur.execute("""SELECT o.senderId as tenant_id, o.submittedDate, o.status,
            u.username, u.firstName, u.lastName, u.email, u.phone, u.avatarUrl, u.role
            FROM offer o
            JOIN user u ON o.senderId = u.id
            WHERE o.targetPropertyId = %s
            ORDER BY 
                FIELD(o.status, 'Pending', 'Accepted', 'Rejected'),
                o.submittedDate DESC""", (property_id,))
        prop.offers = [Offer(id = str(uuid.uuid4()), # since enquiry contains composite PK in database, we use the uuid to create unique id in the conceptual model
            sender= User(str(row['tenant_id']), row['username'], row['firstName'], row['lastName'], row['email'], row['phone'], UserRole(row['role']), row['avatarUrl']),
            status= OfferStatus(row['status']),
            created_at=row['submittedDate']) for row in cur.fetchall()]

        properties.append(prop)

    cur.close()
    return properties

def get_all_properties():
    # this is for admin -> no need to fetch enquiry and offer data for each property
    cur = mysql.connection.cursor()
    cur.execute("""SELECT p.id as p_id, p.title, p.address,
            p.description, p.propertyType, p.rentPerWeek, p.numBedrooms, 
            p.numBathrooms, p.livingArea, p.availableDate,
            u.id AS u_id, u.username, u.firstName, u.lastName,
            u.email, u.phone, u.avatarUrl, u.role  
            FROM property p JOIN user u ON p.agentId = u.id
            ORDER BY p.id DESC""")
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
            agent=User(id=str(row['u_id']),username=row['username'], first_name=row['firstName'], 
                        last_name=row['lastName'], email=row['email'], phone=row['phone'], 
                        role=UserRole(row['role']),
                        avatar_url=row['avatarUrl'] if 'avatarUrl' in row else '',)
        )
        properties.append(prop)

    cur.close()
    return properties

def get_user_accounts_except_admin():
    # this is for admin -> no need to fetch enquiry and offer data for each property
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM user WHERE role != 'Admin' ORDER BY id DESC""")
    results = cur.fetchall()

    cur.close()
    return [User(str(row['id']),row['username'], row['firstName'], row['lastName'], row['email'], row['phone'], UserRole(row['role']), row['avatarUrl']) for row in results]

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
    cur.execute("DELETE FROM property WHERE id = %s", (property_id,))
    # amenities, images, documents are also deleted in database with ON DELETE CASCADE 

    mysql.connection.commit()
    cur.close()

def get_property(property_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM property WHERE id = %s", (property_id,))
    property_data = cursor.fetchone()
    cursor.close()
    return property_data

def get_img_url(property_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT url FROM propertyimage WHERE propertyId = %s and isPrimary = 1", (property_id,))
    primary_image = cursor.fetchone()
    cursor.close()
    return primary_image

def get_amenities(property_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT amenity FROM propertyamenity WHERE propertyId = %s", (property_id,))
    amenities = cursor.fetchall()
    cursor.close()
    return amenities

def get_uni_nearby(property_id):
    cursor = mysql.connection.cursor()
    uni_nearby ="""
    SELECT a.name, b.distance
    FROM nearby as b
    LEFT JOIN university as a ON b.universityId = a.id
    WHERE b.propertyId = %s
    """
    cursor.execute(uni_nearby, (property_id,))
    nearby_universities = cursor.fetchall()
    cursor.close()
    return nearby_universities

def bookmark_overlap(tenant_id, property_id):
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT propertyId FROM bookmark WHERE tenantId = %s AND propertyId = %s ", (tenant_id, property_id))
    check = cursor.fetchone()
    cursor.close()
    return check

def enquiry(tenant_id, property_id, enquiry):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT senderId FROM enquiry WHERE senderId = %s AND targetPropertyId = %s ", (tenant_id, property_id))
    check = cursor.fetchone()
    if check:
        cursor.close()
        return
    cursor.execute(
        """
        INSERT INTO enquiry (senderId, targetPropertyId, message, submittedDate, status)
        VALUES (%s, %s, %s, NOW(), 'New')
        """,
        (tenant_id, property_id, enquiry)
    )
    mysql.connection.commit()
    cursor.close()
    return True

def offer(tenant_id, property_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT senderId FROM offer WHERE senderId = %s AND targetPropertyId = %s ", (tenant_id, property_id))
    check = cursor.fetchone()
    if check:
        cursor.close()
        return
    cursor.execute(
        """
        INSERT INTO offer (senderId, targetPropertyId, submittedDate, status)
        VALUES (%s, %s, NOW(), 'Pending')
        """,
        (tenant_id, property_id)
    )
    mysql.connection.commit()
    cursor.close()
    return True

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


def get_bookmark_by_tenant(user_id):
    
    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT *
        FROM unistay.bookmark a
        JOIN unistay.property b ON a.propertyId = b.id
        LEFT JOIN unistay.propertyimage i 
            ON b.id = i.propertyId AND i.isPrimary = 1
        WHERE a.tenantId = %s
    """,(user_id,))
    results = cursor.fetchall()
    cursor.close()
    return  [
        Bookmark(
            id=str(row['id']),
            tenantId=str(row['tenantId']),
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
                image_urls=row['url']
            ),
            note=row.get('note', ''),
            created_at=row.get('createdAt')
        )
        for row in results
    ]

def add_bookmark_by_id(tenant_id, property_id):
    cursor = mysql.connection.cursor()
    execute = """
    INSERT INTO bookmark (tenantId, propertyId, createdAt) values
    (%s, %s, NOW())
    """
    cursor.execute(execute, (tenant_id, property_id))
    mysql.connection.commit()
    cursor.close()
    

def delete_bookmark_by_id(bookmark_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM bookmark WHERE id = %s", (bookmark_id,))

    mysql.connection.commit()
    cur.close()

# fetch props and filter by q
def get_all_properties_db(q=None):
    cur = mysql.connection.cursor()
    if q:
        cur.execute("SELECT * FROM property WHERE title LIKE %s OR address LIKE %s",
                    ('%'+q+'%', '%'+q+'%'))
    else:
        cur.execute("SELECT * FROM property")
    result = cur.fetchall()
    cur.close()
    return [
        Property(
            id=str(row['id']),
            title=row['title'],
            address=row['address'],
            description=row['description'],
            property_type=PropertyType(row['propertyType']),
            rent_per_week=row['rentPerWeek'],
            bedroom_count=row['numBedrooms'],
            bathroom_count=row['numBathrooms'],
            living_area=float(row['livingArea']),
            available_date=row['availableDate'],
            agent=None
        )
        for row in result
    ]

# fetch all uni
def get_universities_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM university")
    result = cur.fetchall()
    cur.close()
    return [
        University(
            id=str(row['id']),
            name=row['name'],
            address=row['address'],
            logoUrl=row['logoUrl'] if row['logoUrl'] else None
        )
        for row in result
    ]

# fetch primary images for each prop
def get_image_map_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT propertyId, url FROM propertyImage WHERE isPrimary = 1")
    images = cur.fetchall()
    cur.close()
    # build dict, propertyId as key, url as value
    image_map = {}
    for img in images:
        image_map[str(img['propertyId'])] = img['url']
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
    # build dict, propertyId as key, list as value to store more than one nearby uni
    nearby_map = {}
    for n in result:
        pid = n['propertyId']
        if pid not in nearby_map:
            nearby_map[pid] = []
        nearby_map[pid].append(Nearby(
            id=None,
            property=None,
            university=University(
                id=str(n['universityId']),
                name=n['universityName'],
                address=''
            ),
            distance=float(n['distance'])
        ))
    return nearby_map

#filter modal
def get_filtered_properties_db(q=None, uni=None, property_type=None, dist=None, price_min=None, price_max=None, amenities=None):
    cur = mysql.connection.cursor()
    
    sql = """
        SELECT DISTINCT p.* FROM property p
        LEFT JOIN nearby n ON p.id = n.propertyId
        LEFT JOIN propertyAmenity a ON p.id = a.propertyId
        WHERE 1=1
    """
    # WHERE 1=1 is to add 'AND' later
    
    params = []

    if q:
        search = '%'+q+'%'
        sql += " AND (p.title LIKE %s OR p.address LIKE %s)"
        params.extend([search, search])

    if uni and uni != 'all':
        sql += " AND n.universityId = %s"
        params.append(uni)

    if property_type and property_type != 'all':
        sql += " AND p.propertyType = %s"
        params.append(property_type)

    if dist and dist != 'any':
        sql += " AND n.distance <= %s"
        params.append(dist)

    if price_min and price_max:
        if int(price_min) > int(price_max):
            price_min, price_max = price_max, price_min

    if price_min:
        sql += " AND p.rentPerWeek >= %s"
        params.append(price_min)

    if price_max:
        sql += " AND p.rentPerWeek <= %s"
        params.append(price_max)
        
    if amenities:
        for amenity in amenities:
            sql += " AND p.id IN (SELECT propertyId FROM propertyAmenity WHERE amenity = %s)"
            params.append(amenity)

    cur.execute(sql, params)
    result = cur.fetchall()
    cur.close()
    return [
        Property(
            id=str(row['id']),
            title=row['title'],
            address=row['address'],
            description=row['description'],
            property_type=PropertyType(row['propertyType']),
            rent_per_week=row['rentPerWeek'],
            bedroom_count=row['numBedrooms'],
            bathroom_count=row['numBathrooms'],
            living_area=float(row['livingArea']),
            available_date=row['availableDate'],
            agent=None
        )
        for row in result
    ]

def get_user_by_email(email):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, username, password, role FROM user WHERE email = %s",(email,))
    user = cursor.fetchone()
    cursor.close()
    return user


def user_exists_by_email(email):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM user WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    return user


def add_user(username, password, first_name, last_name, email, phone, avatar_url, role):
    cursor = mysql.connection.cursor()
    cursor.execute("""INSERT INTO user (username, password, firstName, lastName, email, phone, avatarUrl, role)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
        (username, password, first_name, last_name, email, phone, avatar_url, role))
    mysql.connection.commit()
    cursor.close()
