-- Create the database
CREATE DATABASE IF NOT EXISTS spartan_training;
USE spartan_training;

-- Create the spartans table
CREATE TABLE IF NOT EXISTS spartans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    stream ENUM('C# Dev', 'C# Test', 'Java Dev', 'Java Test', 'DevOps', 'Data Engineering', 'Business Solutions') NOT NULL,
    trainer ENUM('Nish Mandal', 'Cathy French', 'Luke Fairbrass', 'Phil Windridge', 'Ramon Rossi', 'Tommy Mitchell') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- Insert sample Spartans (Simpsons characters)
INSERT INTO spartans (first_name, last_name, email, stream, trainer, start_date, end_date) VALUES
-- DevOps (Luke Fairbrass)
('Homer', 'Simpson', 'homer.simpson@sparta.fake', 'DevOps', 'Luke Fairbrass', '2024-01-10', '2024-06-10'),
('Carl', 'Carlson', 'carl.carlson@sparta.fake', 'DevOps', 'Luke Fairbrass', '2024-02-15', '2024-07-15'),
('Lenny', 'Leonard', 'lenny.leonard@sparta.fake', 'DevOps', 'Luke Fairbrass', '2024-03-01', '2024-08-01'),

-- Business Solutions (Tommy Mitchell)
('Mr', 'Burns', 'mr.burns@sparta.fake', 'Business Solutions', 'Tommy Mitchell', '2024-04-05', '2024-09-05'),
('Waylon', 'Smithers', 'waylon.smithers@sparta.fake', 'Business Solutions', 'Tommy Mitchell', '2024-05-20', '2024-10-20'),

-- Java Dev (Cathy French)
('Bart', 'Simpson', 'bart.simpson@sparta.fake', 'Java Dev', 'Cathy French', '2024-06-10', '2024-11-10'),
('Milhouse', 'Van Houten', 'milhouse.vanhouten@sparta.fake', 'Java Dev', 'Cathy French', '2024-07-15', '2024-12-15'),

-- Java Test (Phil Windridge)
('Moe', 'Szyslak', 'moe.szyslak@sparta.fake', 'Java Test', 'Phil Windridge', '2024-08-20', '2025-01-20'),
('Barney', 'Gumble', 'barney.gumble@sparta.fake', 'Java Test', 'Phil Windridge', '2024-09-25', '2025-02-25'),

-- C# Dev (Nish Mandal)
('Marge', 'Simpson', 'marge.simpson@sparta.fake', 'C# Dev', 'Nish Mandal', '2024-10-30', '2025-03-30'),
('Apu', 'Nahasapeemapetilon', 'apu.nahasapeemapetilon@sparta.fake', 'C# Dev', 'Nish Mandal', '2024-11-05', '2025-04-05'),

-- C# Test (Ramon Rossi)
('Lisa', 'Simpson', 'lisa.simpson@sparta.fake', 'C# Test', 'Ramon Rossi', '2024-12-10', '2025-05-10'),
('Maggie', 'Simpson', 'maggie.simpson@sparta.fake', 'C# Test', 'Ramon Rossi', '2025-01-15', '2025-06-15');

