CREATE TABLE Room (
    RoomNo INT AUTO_INCREMENT PRIMARY KEY, 
    RoomType VARCHAR(100) NOT NULL, 
    Occupancy INT NOT NULL, 
    RoomPrice BIGINT NOT NULL, 
    Available BOOLEAN, 
    RoomImage VARCHAR(100) NOT NULL,
    RoomDesc TEXT NOT NULL);

INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Suite Room", 2, 2000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-1.jpg", "The suite room at Horse Valley Resort offers luxurious accommodations with spacious living areas, elegant furnishings, modern amenities, and stunning views, ensuring a memorable and comfortable stay for guests.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Family Room", 2, 3000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-2.jpg", "The family room at Horse Valley Resort provides a cozy and welcoming atmosphere, ideal for families, featuring ample space, comfortable bedding, and convenient amenities for an enjoyable and relaxing stay together.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Deluxe Room", 2, 4000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-3.jpg", "The deluxe room at Horse Valley Resort offers a refined retreat with contemporary décor, plush furnishings, and upscale amenities, providing guests with an indulgent and rejuvenating experience during their stay.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Classic Room", 2, 5000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-4.jpg", "The classic room at Horse Valley Resort exudes timeless charm and comfort, featuring elegant décor, cozy furnishings, and essential amenities, creating a serene and inviting atmosphere for a delightful stay.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Superior Room", 2, 6000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-5.jpg", "The superior room at Horse Valley Resort presents a blend of sophistication and comfort, boasting modern décor, upscale furnishings, and enhanced amenities, ensuring a luxurious experience for discerning guests.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Luxury Room", 2, 7000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-6.jpg", "The luxury room at Horse Valley Resort epitomizes opulence and refinement, offering lavish furnishings, exquisite décor, state-of-the-art amenities, and breathtaking views, a great retreat for discerning travelers."); 

ALTER TABLE Room ADD RoomImage VARCHAR(100) NOT NULL;