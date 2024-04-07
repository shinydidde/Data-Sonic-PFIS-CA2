CREATE TABLE Room (
    RoomNo INT AUTO_INCREMENT PRIMARY KEY, 
    RoomType VARCHAR(100) NOT NULL, 
    Occupancy INT NOT NULL, 
    RoomPrice BIGINT NOT NULL, 
    Available BOOLEAN, 
    RoomImage VARCHAR(100) NOT NULL,
    RoomDesc TEXT NOT NULL);

INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Suite Room", 2, 2000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-1.jpg", "When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Family Room", 2, 3000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-2.jpg", "When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Deluxe Room", 2, 4000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-3.jpg", "When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Classic Room", 2, 5000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-4.jpg", "When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Superior Room", 2, 6000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-5.jpg", "When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way.");
INSERT INTO Room (RoomType, Occupancy, RoomPrice, Available, RoomImage, RoomDesc) values ("Luxury Room", 2, 7000, true, "https://horsevalleyresort.francecentral.cloudapp.azure.com:8080/static/images/room-6.jpg", "When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane. Pityful a rethoric question ran over her cheek, then she continued her way."); 

ALTER TABLE Room ADD RoomImage VARCHAR(100) NOT NULL;