use unistay;

insert into user (password, firstName, lastName, email, phone, avatarUrl, role
) values 
-- Agent values sample
(SHA2('password', 256),
'Jack',
'Smith',
'jack@agency.com',
'0412345678',
Null,
'Agent'
),(SHA2('password', 256),
"Sarah",
"Wilson",
"sarah@agency.com",
"0488776655",
Null,
'Agent'
),
-- Tenant values sample
(SHA2('password', 256),
"Minh",
"Nguyen",
"minh@student.edu.au",
"0411223344",
Null,
'Tenant'
),
(SHA2('password', 256),
"Bill",
"Tran",
"bill@student.edu.au",
"0423113344",
Null,
'Tenant'
),
(SHA2('password', 256),
"John",
"Dee",
"admin@admin.com",
"0432123211",
Null,
'Admin'
);

insert into property (
title, address, description, propertyType,
rentPerWeek, numBedrooms, numBathrooms, livingArea,
availableDate, agentId
) values ( 
'Modern Studio near UQ', 
'123 Saint Lucia, Brisbane',
'Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.',
'Studio',
450,
1,
1,
45.5,
'2026-09-20',
1
), (
'Shared House for Students',
'456 Toowong, Brisbane',
'Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.',
'House',
250,
4,
2,
120.0,
'2026-07-20',
1
), (
'Luxury Riverside Studio',
'789 Marine Parade, South Bank',
'Stunning studio apartment overlooking the Brisbane River. This premium space boasts top-of-the-line appliances, a private balcony, and floor-to-ceiling windows. Residents get exclusive access to the rooftop infinity pool and gym. Perfect for a young professional or couple looking for a vibrant lifestyle.',
'Apartment',
550,
1,
1,
55.0,
'2026-08-11',
2
), (
'Spacious Family Home with Backyard',
"12 Chelmer Street, Chelmer",
"Charming Queenslander home in a quiet, leafy suburb. Features a massive fully-fenced backyard perfect for kids and pets, a massive wrap-around veranda, and character features throughout. Located within a top-tier school catchment zone and just a short walk to the train station.",
'House',
820,
4,
2,
210.0,
'2026-06-10',
2
);

insert into university (name, address, logoUrl) values (
"University of Queensland",
"St Lucia QLD 4072",
"logo_uq.jpg"
),(
"Queensland University of Technology",
"Gardent Point Rd",
"logo_qut.jpg"
), (
"Griffith University",
"Nathan QLD 4111",
"logo_gu.png"
);

insert into nearby (propertyId, universityId, distance) values (
1,
1,
0.5
), (
1,
2,
7.2
), (
2,
1,
1.2
);

insert into bookmark (tenantId, propertyId, note, createdAt) values (
3,
1,
'Very close to my campus.',
'2026-05-22'
), (
3,
2,
'Fantastic',
'2026-05-22'
);

insert into enquiry (senderId, targetPropertyId, message, submittedDate, status) values (
3,
1,
'Is parking available at this property? Also, are pets allowed?',
'2026-05-22',
'New'
), (
4,
1,
'Can we have a meet',
'2026-05-20',
'Responded'
);

insert into offer (senderId, targetPropertyId, submittedDate, status) values (
3,
2,
'2026-05-22',
'Pending'
),(
4,
2,
'2026-05-22',
'Accepted'
);

insert into propertyAmenity (propertyId, amenity) values (
1,
'High-Speed Wifi'
), (
1,
'Fitness Center'
), (
1,
'Parking Space'
), (
2,
'Parking Space'
), (
2,
'Shared Kitchen'
), (
3,
'High-Speed Wifi'
);

insert into propertyImage (propertyId, url, isPrimary) values (
1,
"properties_1.jpeg",
True
), (
2,
"properties_2.jpeg", 
True
), (
3,
"properties_3.jpeg",
True
), (
4,
"properties_4.jpeg",
True
), (
1,
'properties_1_gallery_1.jpeg',
False
), (
1,
'properties_1_gallery_2.jpeg',
False
), (
2,
'properties_2_gallery_1.jpeg',
False
), (
2,
'properties_2_gallery_2.jpeg',
False
);

