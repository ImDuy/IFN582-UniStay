use unistay;

insert into user (
password, firstName, lastName, email, phone, avatarUrl, role, createdAt
) values 
-- Agent values sample
(SHA2('password', 256), 'Jack', 'Smith', 'jack@agency.com', '0412345678', Null, 'Agent', '2026-04-10'),
(SHA2('password', 256), "Sarah", "Wilson", "sarah@agency.com", "0488776655", Null, 'Agent', '2026-01-11'),
-- Tenant values sample
(SHA2('password', 256), "Minh", "Nguyen", "minh@student.edu.au", "0411223344", Null, 'Tenant', '2026-05-23'),
(SHA2('password', 256), "Bill", "Tran", "bill@student.edu.au", "0423113344", Null, 'Tenant', '2026-05-10'),
-- Admin values sample
(SHA2('password', 256), "John", "Dee", "admin@admin.com", "0432123211", Null, 'Admin', '2026-04-29'),
(SHA2('password', 256), "Sam", "Smith", "Samsmith@gmail.com", "0433333333", Null, 'Admin', '2026-04-27');

insert into property (
title, address, description, propertyType,
rentPerWeek, numBedrooms, numBathrooms, livingArea,
availableDate, agentId, createdAt
) values 
('Modern Studio near UQ', '123 Saint Lucia, Brisbane','Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.','Studio',450,1, 1, 45.5, '2026-09-20', 1, '2026-04-19'),
('Shared House for Students', '456 Toowong, Brisbane', 'Beautiful modern apartment in the heart of downtown with city views.\nThis exceptional property offers a perfect blend of comfort and convenience. Located in a prime area with excellent access to public transportation, shopping centers, and dining options. The property features modern finishes, ample natural light, and well-maintained common areas. Ideal for students and professionals seeking quality accommodation.', 'House', 250, 4, 2, 120.0, '2026-07-20', 1, '2026-05-29'),
('Luxury Riverside Studio', '789 Marine Parade, South Bank', 'Stunning studio apartment overlooking the Brisbane River. This premium space boasts top-of-the-line appliances, a private balcony, and floor-to-ceiling windows. Residents get exclusive access to the rooftop infinity pool and gym. Perfect for a young professional or couple looking for a vibrant lifestyle.', 'Apartment', 550, 1, 1, 55.0, '2026-08-11', 2, '2026-02-12'), 
('Spacious Family Home with Backyard', "12 Chelmer Street, Chelmer", "Charming Queenslander home in a quiet, leafy suburb. Features a massive fully-fenced backyard perfect for kids and pets, a massive wrap-around veranda, and character features throughout. Located within a top-tier school catchment zone and just a short walk to the train station.", 'House', 820, 4, 2, 210.0, '2026-06-10', 2, '2026-01-22'),
('Sunny House in Chermside', '42 Gympie Road, Chermside, QLD', 'A bright and spacious house located in the heart of Chermside. Features modern finishes, natural lighting throughout, and easy access to public transport and Westfield shopping centre.', 'House', 450, 3, 2, 120.0, '2026-07-01', 1, '2026-03-22'),
('Modern Apartment in South Bank', '87 Grey Street, South Bank, QLD', 'Stylish apartment in the vibrant South Bank precinct. Enjoy stunning river views, high-end appliances, and walking distance to restaurants, galleries, and the Brisbane River.', 'Apartment', 380, 2, 1, 75.0, '2026-07-15', 2, '2026-01-29'),
('Cosy Townhouse in Camp Hill', '215 Old Cleveland Road, Camp Hill, QLD', 'Charming townhouse nestled in the leafy suburb of Camp Hill. Close to cafes, boutique shops, and public transport. Features an open-plan living area and a private courtyard for entertaining.', 'Townhouse', 520, 3, 2,  95.0, '2026-08-01', 1, '2026-01-02'),
('Elegant Condo in Fortitude Valley','33 Brunswick Street, Fortitude Valley, QLD','Sophisticated condo in lively Fortitude Valley. Boasts contemporary design, quality fixtures, and a balcony perfect for enjoying the vibrant neighbourhood atmosphere below.', 'Condo', 490, 2, 2,  85.0, '2026-07-20', 1, '2026-02-21'),
('Compact Studio in West End', '11 Boundary Street, West End, QLD', 'Efficient and modern studio in the heart of West End. Perfect for singles or students, offering a smart layout with quality fittings and proximity to Brisbane CBD and cultural hubs.', 'Studio', 310, 1, 1,  40.0, '2026-06-25', 2, '2026-02-15'),
('Spacious House in Carindale', '128 Creek Road, Carindale, QLD', 'Large family home in the peaceful suburb of Carindale. Features a generous backyard, updated kitchen, and multiple living zones. Well-connected to schools, parks, and Westfield Carindale.', 'House', 680, 4, 2, 200.0, '2026-08-10', 1, '2026-03-27'),
('Riverside Apartment in Newstead', '55 Breakfast Creek Road, Newstead, QLD', 'Contemporary apartment along the scenic riverside in Newstead. Includes premium finishes, resort-style facilities, and easy access to cycling paths, boutique shops, and dining precincts.', 'Apartment', 560, 2, 2,  80.0, '2026-07-05', 1, '2026-01-30'),
('Charming Townhouse in Paddington', '76 Given Terrace, Paddington, QLD', 'Delightful townhouse in the prestigious suburb of Paddington. Features timber floors, renovated interiors, and a leafy private garden. A short commute to Brisbane CBD via bus.', 'Townhouse', 470, 3, 1, 110.0, '2026-09-01', 2, '2025-12-29'),
('Modern Condo in Kangaroo Point', '19 River Terrace, Kangaroo Point, QLD', 'Stunning condo offering breathtaking Story Bridge and river views. Light-filled interiors, modern amenities, and an open-plan layout make this an exceptional urban retreat.', 'Condo', 740, 3, 2, 130.0, '2026-08-20', 2, '2026-05-29'),
('City-View Studio in Spring Hill', '301 Leichhardt Street, Spring Hill, QLD', 'Sleek studio apartment with sweeping city views in the sought-after Spring Hill precinct. Features floor-to-ceiling windows, integrated appliances, and access to building amenities.', 'Studio', 350, 1, 1,  45.0, '2026-07-10', 1, '2026-04-09'),
('Stylish Apartment in Ascot', '63 Racecourse Road, Ascot, QLD', 'Elegant apartment situated in the prestigious suburb of Ascot. Features high ceilings, modern finishes, and a private balcony overlooking tree-lined streets. Close to Doomben Racecourse, local cafes, and easy motorway access to Brisbane CBD.', 'Apartment', 570, 2, 2, 90.0, '2026-08-15', 2, '2026-02-06');

insert into university (name, address, logoUrl) values 
("University of Queensland", "St Lucia QLD 4072", "logo_uq.jpg"),
("Queensland University of Technology", "Gardent Point Rd", "logo_qut.jpg"), 
("Griffith University", "Nathan QLD 4111", "logo_gu.png");

insert into nearby (propertyId, universityId, distance) values 
(1, 1, 0.5), 
(1, 2, 7.2), 
(2, 1, 1.2),
(3, 3, 3.4),
(3, 2, 2.0),
(3, 1, 1.2),
(4, 1, 6.2),
(5, 2, 3.9),
(5, 1, 4.4),
(6, 2, 3.5),
(7, 3, 9.4),
(7, 2, 1.9),
(8, 1, 0.8),
(8, 2, 4.2),
(9, 3, 2.6),
(10, 2, 3.1),
(10, 3, 4.2),
(11, 3, 5.3),
(12, 1, 9.5),
(12, 2, 1.9),
(13, 1, 4.5),
(14, 2, 1.9),
(14, 3, 0.3),
(15, 1, 3.5),
(15, 3, 4.7);

insert into bookmark (tenantId, propertyId, note, createdAt) values
(3, 1, 'Very close to my campus.', '2026-05-22'),
(3, 2, 'Fantastic', '2026-05-22');

insert into enquiry (senderId, targetPropertyId, message, submittedDate, status) values 
(3, 1, 'Is parking available at this property? Also, are pets allowed?', '2026-05-22', 'New'), 
(4, 1, 'Can we have a meet', '2026-05-20', 'Responded'),
(3, 4, 'Can I ask something?', '2026-06-04', 'New'),
(3, 10, 'Can I move on little faster?', '2026-06-04', 'Closed'),
(4, 8,  'Is it actually condo?', '2026-06-04', 'Responded');

insert into offer (senderId, targetPropertyId, submittedDate, status) values 
(3, 2, '2026-05-22', 'Pending'),
(4, 2, '2026-05-22', 'Accepted'),
(3, 8, '2026-06-04', 'Rejected');

insert into propertyAmenity (propertyId, amenity) values 
(1, 'High-Speed Wifi'), 
(1, 'Fitness Center'), 
(1, 'Parking Space'), 
(2, 'Parking Space'), 
(2, 'Shared Kitchen'), 
(3, 'High-Speed Wifi'),
(4, 'Shared Kitchen'),
(5, 'High-Speed Wifi'),
(5, 'Parking Space'),
(6, 'Fitness Center'),
(6, 'High-Speed Wifi'),
(6, 'Shared Kitchen'),
(7, 'Parking Space'),
(8, 'High-Speed Wifi'),
(8, 'Fitness Center'),
(8, 'Parking Space'),
(8, 'Shared Kitchen'),
(10, 'Parking Space'),
(10, 'Fitness Center'),
(11, 'High-Speed Wifi'),
(12, 'Shared Kitchen'),
(13, 'High-Speed Wifi'),
(13, 'Parking Space'),
(13, 'Fitness Center'),
(14, 'High-Speed Wifi'),
(15, 'High-Speed Wifi'),
(15, 'Parking Space'),
(15, 'Fitness Center');

insert into propertyImage (propertyId, url, isPrimary) values 
(1, "properties_1.jpeg", True), 
(2, "properties_2.jpeg", True), 
(3, "properties_3.jpeg", True), 
(4, "properties_4.jpeg", True), 
(5, "properties_5.jpeg", True),
(6, "properties_6.jpeg", True),
(7, "properties_7.jpeg", True),
(8, "properties_8.jpeg", True),
(9, "properties_9.jpeg", True),
(10, "properties_10.jpeg", True),
(11, "properties_11.jpeg", True),
(12, "properties_12.jpeg", True),
(13, "properties_13.jpeg", True),
(14, "properties_14.jpeg", True),
(15, "properties_15.jpeg", True),
(1, 'properties_1-1.jpeg', False), 
(1, 'properties_1-2.jpeg', False), 
(2, 'properties_2-1.jpeg', False), 
(2, 'properties_2-2.jpeg', False),
(3, 'properties_3-1.jpeg', False), 
(3, 'properties_3-2.jpeg', False),
(4, 'properties_4-1.jpeg', False), 
(4, 'properties_4-2.jpeg', False),
(5, 'properties_5-1.jpeg', False), 
(5, 'properties_5-2.jpeg', False),
(6, 'properties_6-1.jpeg', False), 
(6, 'properties_6-2.jpeg', False),
(7, 'properties_7-1.jpeg', False), 
(7, 'properties_7-2.jpeg', False),
(8, 'properties_8-1.jpeg', False), 
(8, 'properties_8-2.jpeg', False),
(9, 'properties_9-1.jpeg', False), 
(9, 'properties_9-2.jpeg', False),
(10, 'properties_10-1.jpeg', False), 
(10, 'properties_10-2.jpeg', False),
(11, 'properties_11-1.jpeg', False), 
(11, 'properties_11-2.jpeg', False),
(12, 'properties_12-1.jpeg', False), 
(12, 'properties_12-2.jpeg', False),
(13, 'properties_13-1.jpeg', False), 
(13, 'properties_13-2.jpeg', False),
(14, 'properties_14-1.jpeg', False), 
(14, 'properties_14-2.jpeg', False),
(15, 'properties_15-1.jpeg', False), 
(15, 'properties_15-2.jpeg', False);
