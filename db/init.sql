drop database voterdb;
create database voterdb;

use voterdb;

CREATE TABLE
  Users (
    User_ID int PRIMARY KEY AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    MiddleName varchar(100),
    LastName varchar(100) NOT NULL,
    Age int NOT NULL,
    StreetAddress1 varchar(250) NOT NULL,
    StreetAddress2 varchar(250) NOT NULL,
    City varchar(250) NOT NULL,
    State varchar(250) NOT NULL,
    ZipCode varchar(10),
    ID1 varchar(250) NOT NULL,
    ID2 varchar(250) NOT NULL,
    Email varchar(100) UNIQUE,
    Password varchar(255) NOT NULL,
    Salt varchar(255) NOT NULL,
    Role varchar(15) NOT NULL,
    Status varchar(255) NOT NULL
  );

CREATE TABLE
  Precincts (
    PrecinctID int PRIMARY KEY auto_increment,
    PrecinctName varchar(100) NOT NULL,
    NumberofCandidates int,
    Street varchar(100) NOT NULL,
    State varchar(100) NOT NULL,
    ZipCode int NOT NULL,
    ZipPlus4Start int NOT NULL,
    ZipPlus4End int NOT NULL,
    PollingManagerID int NULL
  );

INSERT INTO
  voterdb.Precincts (
    PrecinctName,
    NumberofCandidates,
    Street,
    State,
    ZipCode,
    ZipPlus4Start,
    ZipPlus4End,
    PollingManagerID
  )
VALUES
  (
    "Iowa City",
    5,
    "Benton Street",
    "IA",
    52241,
    0000,
    4999,
    3
  );

CREATE TABLE
  ElectoralRaces (
    RaceName varchar(100) PRIMARY KEY NOT NULL,
    Term varchar(100),
    NumofCandidates int,
    StartDate date NOT NULL,
    EndDate date NOT NULL,
    CONSTRAINT CHK_DATE CHECK (StartDate <= EndDate)
  );

INSERT INTO
  Users (
    FirstName,
    MiddleName,
    LastName,
    Age,
    StreetAddress1,
    StreetAddress2,
    City,
    State,
    ZipCode,
    ID1,
    ID2,
    Email,
    Password,
    Salt,
    Role,
    Status
  )
Values
  (
    "Eric",
    "J",
    "T",
    22,
    "Coralville",
    "20th Ave",
    "Coralville",
    "Iowa",
    "52241",
    "dl",
    "birth cert",
    "voter@e",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu",
    "Voter",
    "Approved"
  );

INSERT INTO
  Users (
    FirstName,
    MiddleName,
    LastName,
    Age,
    StreetAddress1,
    StreetAddress2,
    City,
    State,
    ZipCode,
    ID1,
    ID2,
    Email,
    Password,
    Salt,
    Role,
    Status
  )
Values
  (
    "Eric",
    "J",
    "T",
    22,
    "Coralville",
    "20th Ave",
    "Coralville",
    "Iowa",
    "52241",
    "dl",
    "birth cert",
    "admin@e",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu",
    "Admin",
    "Approved"
  );

INSERT INTO
  Users (
    FirstName,
    MiddleName,
    LastName,
    Age,
    StreetAddress1,
    StreetAddress2,
    City,
    State,
    ZipCode,
    ID1,
    ID2,
    Email,
    Password,
    Salt,
    Role,
    Status
  )
Values
  (
    "Eric",
    "J",
    "T",
    22,
    "Coralville",
    "20th Ave",
    "Coralville",
    "Iowa",
    "52241",
    "dl",
    "birth cert",
    "manager@e",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu",
    "Manager",
    "Approved"
  );

INSERT INTO
  Users (
    FirstName,
    MiddleName,
    LastName,
    Age,
    StreetAddress1,
    StreetAddress2,
    City,
    State,
    ZipCode,
    ID1,
    ID2,
    Email,
    Password,
    Salt,
    Role,
    Status
  )
Values
  (
    "Eric",
    "J",
    "T",
    22,
    "Coralville",
    "20th Ave",
    "Coralville",
    "Iowa",
    "52241",
    "dl",
    "birth cert",
    "erictrautsch@outlook.com",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku",
    "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu",
    "Voter",
    "Pending"
  );

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `get_user_auth` (IN mail varchar(255)) BEGIN
SELECT
  User_ID,
  Password,
  Salt,
  Role,
  Status,
  ZipCode
FROM
  Users
WHERE
  STRCMP(Email, mail) = 0;

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `insert_user` (IN name1 varchar(100),
  IN name2 varchar(100),
  IN name3 varchar(100),
  IN age int,
  IN address1 varchar(250),
  IN address2 varchar(250),
  IN city varchar(250),
  IN state varchar(100),
  IN zip int,
  IN ID1 varchar(20),
  IN ID2 varchar(20),
  IN email varchar(100),
  IN password varchar(255),
  IN salt varchar(255),
  IN role varchar(255),
  IN status varchar(255)
) BEGIN
INSERT INTO
  voterdb.Users (
    FirstName,
    MiddleName,
    LastName,
    Age,
    StreetAddress1,
    StreetAddress2,
    City,
    State,
    ZipCode,
    ID1,
    ID2,
    Email,
    Password,
    Salt,
    Role,
    Status
  )
VALUES
  (
    name1,
    name2,
    name3,
    age,
    address1,
    address2,
    city,
    state,
    zip,
    ID1,
    ID2,
    email,
    password,
    salt,
    role,
    status
  );
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `approve_user` (IN email varchar(100)) BEGIN
UPDATE Users
SET
  Status = "Approved"
WHERE
  STRCMP(Email, email) = 0;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `deny_user` (IN email varchar(100)) BEGIN
UPDATE Users
SET
  Status = "Denied"
WHERE
  STRCMP(Email, email) = 0;

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `insert_precinct` (
  IN PName varchar(100),
  IN CandidatesCount int,
  IN street varchar(100),
  IN state varchar(100),
  IN zip int,
  IN ZipStart int,
  IN ZipEnd int
) BEGIN
INSERT INTO
  voterdb.Precincts (
    PrecinctName,
    NumberofCandidates,
    Street,
    State,
    ZipCode,
    ZipPlus4Start,
    ZipPlus4End
  )
VALUES
  (
    PName,
    CandidatesCount,
    street,
    state,
    zip,
    ZipStart,
    ZipEnd
  );

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `view_precinct` () BEGIN
SELECT
  *
FROM
  voterdb.Precincts;

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `get_precinct_info` (IN PID int, IN PName varchar(100)) BEGIN
SELECT
  Count(*)
FROM
  voterdb.Precincts
WHERE
  STRCMP(PrecinctID, PID) = 0
  AND STRCMP(PrecinctName, PName) = 0;

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `update_precinct` (IN PID int,
  IN PName varchar(100),
  IN CandidatesCount int,
  IN zip int,
  IN ZipStart int,
  IN ZipEnd int
) BEGIN
UPDATE voterdb.Precincts
SET
  PrecinctName = PName,
  NumberofCandidates = CandidatesCount,
  ZipCode = zip,
  ZipPlus4Start = ZipStart,
  ZipPlus4End = ZipEnd
WHERE
  PrecinctID = PID;
END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `del_precinct` (IN PID int, IN PName varchar(100)) BEGIN
DELETE FROM voterdb.Precincts
WHERE
  PrecinctID = PID
  and PrecinctName = PName;
END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `view_races` () BEGIN
SELECT
  *
FROM
  voterdb.ElectoralRaces;

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `insert_races` (
  IN RName varchar(100),
  IN term varchar(100),
  IN CandidatesCount int,
  IN SDate date,
  IN EDate date
) BEGIN
INSERT INTO
  voterdb.ElectoralRaces (
    RaceName,
    Term,
    NumofCandidates,
    StartDate,
    EndDate
  )
VALUES
  (RName, term, CandidatesCount, SDate, EDate);

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `update_races` (
  IN RName varchar(100),
  IN term varchar(100),
  IN CandidatesCount int,
  IN SDate date,
  IN EDate date
) BEGIN
UPDATE voterdb.ElectoralRaces
SET
  RaceName = RName,
  Term = term,
  NumofCandidates = CandidatesCount,
  StartDate = SDate,
  EndDate = EDate;

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `del_races` (IN RName varchar(100)) BEGIN
DELETE FROM voterdb.ElectoralRaces
WHERE
  RaceName = RName;

END $$ 
DELIMITER ;

-- Election Additions
CREATE TABLE
  `Elections` (
    `ElectionTitle` varchar(255) NOT NULL,
    `NaturalGeography` varchar(150) NOT NULL,
    `ElectoralConstituency` int NOT NULL,
    `PublicStatus` tinyint(4) NOT NULL,
    PRIMARY KEY (`ElectionTitle`)
  );

-- Seed elections with an election
INSERT INTO
  `voterdb`.`Elections` (
    `ElectionTitle`,
    `NaturalGeography`,
    `ElectoralConstituency`,
    `PublicStatus`
  )
VALUES
  ("US-Senate-IA-1", "Iowa", 52241, "0");

-- INSERT INTO `Elections`
INSERT INTO
  `voterdb`.`Elections` (
    `ElectionTitle`,
    `NaturalGeography`,
    `ElectoralConstituency`,
    `PublicStatus`
  )
VALUES
  ("US-Senate-IA-2", "Iowa", 52246, "0");

DELIMITER $$
CREATE PROCEDURE `view_elections` () BEGIN
SELECT
  ElectionTitle,
  NaturalGeography,
  ElectoralConstituency,
  PublicStatus
FROM
  Elections;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `view_election` (IN title varchar(255)) BEGIN
SELECT
  ElectionTitle,
  NaturalGeography,
  ElectoralConstituency,
  PublicStatus
FROM
  Elections
WHERE
  ElectionTitle = title;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `new_election` (
  IN title varchar(255),
  in nat_geo varchar(255),
  in el_cons varchar(255),
  pub_status tinyint(4)
) BEGIN
INSERT INTO
  `voterdb`.`Elections` (
    `ElectionTitle`,
    `NaturalGeography`,
    `ElectoralConstituency`,
    `PublicStatus`
  )
VALUES
  (title, nat_geo, el_cons, pub_status);

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `update_election` (
  IN current_title varchar(255),
  IN new_title varchar(255),
  in nat_geo varchar(255),
  in el_cons varchar(255),
  pub_status tinyint(4)
) BEGIN
UPDATE `voterdb`.`Elections`
SET
  `ElectionTitle` = new_title,
  `NaturalGeography` = nat_geo,
  `ElectoralConstituency` = el_cons,
  `PublicStatus` = pub_status
WHERE
  `ElectionTitle` = current_title;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `delete_election` (IN title varchar(255)) BEGIN
DELETE FROM `voterdb`.`Elections`
WHERE
  ElectionTitle = title;

END $$ 
DELIMITER ;

-- 7a
CREATE TABLE
  ElectionDates (
    ElectionDateID INT PRIMARY KEY AUTO_INCREMENT,
    ElectionTitle VARCHAR(255),
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (ElectionTitle) REFERENCES Elections (ElectionTitle)
  );

DELIMITER $$
CREATE PROCEDURE `new_election_date` (
  IN title varchar(255),
  IN start_date DATE,
  in end_date DATE
) BEGIN
INSERT INTO
  ElectionDates (ElectionTitle, StartDate, EndDate)
VALUES
  (title, start_date, end_date);

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `view_election_date` (IN title varchar(255)) BEGIN
SELECT
  ElectionDateID,
  ElectionTitle,
  StartDate,
  EndDate
FROM
  ElectionDates
WHERE
  STRCMP(ElectionTitle, title) = 0;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `delete_election_date` (IN electionID INT) BEGIN
DELETE FROM ElectionDates
WHERE
  ElectionDateID = electionID;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `update_election_date` (
  IN election_date_id INT,
  IN title varchar(255),
  IN start_date DATE,
  IN end_date DATE
) BEGIN
UPDATE ElectionDates
SET
  ElectionTitle = title,
  StartDate = start_date,
  EndDate = end_date
WHERE
  ElectionTitleID = election_date_id;

END $$ 
DELIMITER ;

-- 7c
CREATE TABLE
  ElectionCandidates (
    CandidateID INT PRIMARY KEY AUTO_INCREMENT,
    ElectionTitle VARCHAR(255),
    ElectoralRace VARCHAR(255),
    CandidateFirstName VARCHAR(255),
    CandidateLastName VARCHAR(255),
    CandidateInfo VARCHAR(255),
    CandidateVotes INT,
    FOREIGN KEY (ElectionTitle) REFERENCES Elections (ElectionTitle)
  );

DELIMITER $$
CREATE PROCEDURE `new_election_candidate` (
  IN title VARCHAR(255),
  IN race VARCHAR(255),
  IN first_name VARCHAR(255),
  IN last_name VARCHAR(255),
  IN info VARCHAR(255)
) BEGIN
INSERT INTO
  ElectionCandidates (
    ElectionTitle,
    ElectoralRace,
    CandidateFirstName,
    CandidateLastName,
    CandidateInfo,
    CandidateVotes
  )
VALUES
  (title, race, first_name, last_name, info, 0);

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `view_election_candidate` (IN election_title varchar(255)) BEGIN
SELECT
  CandidateID,
  ElectionTitle,
  ElectoralRace,
  CandidateFirstName,
  CandidateLastName,
  CandidateInfo
FROM
  ElectionCandidates
WHERE
  ElectionTitle = election_title;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `delete_election_candidate` (IN candidate_id INT) BEGIN
DELETE FROM ElectionCandidates
WHERE
  CandidateID = candidate_id;

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `update_election_candidate` (
  IN candidate_id INT,
  IN title VARCHAR(255),
  IN race VARCHAR(255),
  IN first_name VARCHAR(255),
  IN last_name VARCHAR(255),
  IN info VARCHAR(255)
) BEGIN
UPDATE ElectionCandidates
SET
  ElectionTitle = title,
  ElectoralRace = race,
  CandidateFirstName = first_name,
  CandidateLastName = last_name,
  CandidateInfo = info
WHERE
  CandidateID = candidate_id;

END $$ 
DELIMITER ;

CREATE TABLE
  Votes (
    User_ID VARCHAR(255) NOT NULL,
    Election_ID VARCHAR(255) NOT NULL
  );
  
-- USE `voterdb`$$
DELIMITER $$
CREATE PROCEDURE `insert_vote` (
  IN userID varchar(255),
  IN electionID varchar(255)
) BEGIN
INSERT INTO
  Votes (
    User_ID,
    Election_ID)
VALUES(
    userID,
    electionID
    );

END $$ 
DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `get_vote` (IN userID varchar(255), election varchar(255)) BEGIN
SELECT
  *
FROM
  Votes
WHERE
  TRIM(User_ID) = TRIM(userID) AND
  TRIM(Election_ID) = TRIM(election);

END $$ 
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `update_candidate_votes` (in candidate_id INT) BEGIN
UPDATE ElectionCandidates
SET
  CandidateVotes = CandidateVotes + 1
WHERE
  CandidateID = candidate_id;

END $$ 
DELIMITER ;

-- Audit table
CREATE TABLE audit_log (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(255),
    operation_type VARCHAR(10),
    old_value TEXT,
    new_value TEXT,
    audit_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Triggers for Users Table
-- 
-- 
--  
-- 
DELIMITER $$

CREATE TRIGGER after_insert_Users
AFTER INSERT ON Users 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, new_value)
    VALUES ('Users', 'INSERT', CONCAT_WS(', ', 
        NEW.User_ID, NEW.FirstName, NEW.MiddleName, NEW.LastName, NEW.Age, 
        NEW.StreetAddress1, NEW.StreetAddress2, NEW.City, NEW.State, NEW.ZipCode, 
        NEW.ID1, NEW.ID2, NEW.Email, NEW.Password, NEW.Salt, NEW.Role, NEW.Status));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_update_Users
AFTER UPDATE ON Users 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value, new_value)
    VALUES ('Users', 'UPDATE', 
        CONCAT_WS(', ', 
            OLD.User_ID, OLD.FirstName, OLD.MiddleName, OLD.LastName, OLD.Age, 
            OLD.StreetAddress1, OLD.StreetAddress2, OLD.City, OLD.State, OLD.ZipCode, 
            OLD.ID1, OLD.ID2, OLD.Email, OLD.Password, OLD.Salt, OLD.Role, OLD.Status),
        CONCAT_WS(', ', 
            NEW.User_ID, NEW.FirstName, NEW.MiddleName, NEW.LastName, NEW.Age, 
            NEW.StreetAddress1, NEW.StreetAddress2, NEW.City, NEW.State, NEW.ZipCode, 
            NEW.ID1, NEW.ID2, NEW.Email, NEW.Password, NEW.Salt, NEW.Role, NEW.Status));
END $$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER after_delete_Users
AFTER DELETE ON Users 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value)
    VALUES ('Users', 'DELETE', CONCAT_WS(', ', 
        OLD.User_ID, OLD.FirstName, OLD.MiddleName, OLD.LastName, OLD.Age, 
        OLD.StreetAddress1, OLD.StreetAddress2, OLD.City, OLD.State, OLD.ZipCode, 
        OLD.ID1, OLD.ID2, OLD.Email, OLD.Password, OLD.Salt, OLD.Role, OLD.Status));
END $$

DELIMITER ;
-- 
-- 
-- 
-- 
-- END triggers for Users Table

-- Begin Triggers for Precincts table
-- 
-- 
-- 
-- 
DELIMITER $$

CREATE TRIGGER after_insert_Precincts
AFTER INSERT ON Precincts 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, new_value)
    VALUES ('Precincts', 'INSERT', CONCAT_WS(', ', 
        NEW.PrecinctID, NEW.PrecinctName, NEW.NumberofCandidates, NEW.Street, 
        NEW.State, NEW.ZipCode, NEW.ZipPlus4Start, NEW.ZipPlus4End));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_update_Precincts
AFTER UPDATE ON Precincts 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value, new_value)
    VALUES ('Precincts', 'UPDATE', 
        CONCAT_WS(', ', 
            OLD.PrecinctID, OLD.PrecinctName, OLD.NumberofCandidates, OLD.Street, 
            OLD.State, OLD.ZipCode, OLD.ZipPlus4Start, OLD.ZipPlus4End),
        CONCAT_WS(', ', 
            NEW.PrecinctID, NEW.PrecinctName, NEW.NumberofCandidates, NEW.Street, 
            NEW.State, NEW.ZipCode, NEW.ZipPlus4Start, NEW.ZipPlus4End));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_delete_Precincts
AFTER DELETE ON Precincts 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value)
    VALUES ('Precincts', 'DELETE', CONCAT_WS(', ', 
        OLD.PrecinctID, OLD.PrecinctName, OLD.NumberofCandidates, OLD.Street, 
        OLD.State, OLD.ZipCode, OLD.ZipPlus4Start, OLD.ZipPlus4End));
END $$

DELIMITER ;

-- 
-- 
-- 
-- END Triggers for Precincts

-- START Triggers for Electoral Races
DELIMITER $$

CREATE TRIGGER after_insert_ElectoralRaces
AFTER INSERT ON ElectoralRaces 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, new_value)
    VALUES ('ElectoralRaces', 'INSERT', CONCAT_WS(', ', 
        NEW.RaceName, NEW.Term, NEW.NumofCandidates, NEW.StartDate, NEW.EndDate));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_update_ElectoralRaces
AFTER UPDATE ON ElectoralRaces 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value, new_value)
    VALUES ('ElectoralRaces', 'UPDATE', 
        CONCAT_WS(', ', 
            OLD.RaceName, OLD.Term, OLD.NumofCandidates, OLD.StartDate, OLD.EndDate),
        CONCAT_WS(', ', 
            NEW.RaceName, NEW.Term, NEW.NumofCandidates, NEW.StartDate, NEW.EndDate));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_delete_ElectoralRaces
AFTER DELETE ON ElectoralRaces 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value)
    VALUES ('ElectoralRaces', 'DELETE', CONCAT_WS(', ', 
        OLD.RaceName, OLD.Term, OLD.NumofCandidates, OLD.StartDate, OLD.EndDate));
END $$

DELIMITER ;

-- END Triggers for Electoral Races

-- START Triggers for Elections
DELIMITER $$

CREATE TRIGGER after_insert_Elections
AFTER INSERT ON Elections 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, new_value)
    VALUES ('Elections', 'INSERT', CONCAT_WS(', ', 
        NEW.ElectionTitle, NEW.NaturalGeography, NEW.ElectoralConstituency, NEW.PublicStatus));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_update_Elections
AFTER UPDATE ON Elections 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value, new_value)
    VALUES ('Elections', 'UPDATE', 
        CONCAT_WS(', ', 
            OLD.ElectionTitle, OLD.NaturalGeography, OLD.ElectoralConstituency, OLD.PublicStatus),
        CONCAT_WS(', ', 
            NEW.ElectionTitle, NEW.NaturalGeography, NEW.ElectoralConstituency, NEW.PublicStatus));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_delete_Elections
AFTER DELETE ON Elections 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value)
    VALUES ('Elections', 'DELETE', CONCAT_WS(', ', 
        OLD.ElectionTitle, OLD.NaturalGeography, OLD.ElectoralConstituency, OLD.PublicStatus));
END $$

DELIMITER ;

-- END Triggers for Elections

-- Start Triggers for ElectionDates
DELIMITER $$

CREATE TRIGGER after_insert_ElectionDates
AFTER INSERT ON ElectionDates 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, new_value)
    VALUES ('ElectionDates', 'INSERT', CONCAT_WS(', ', 
        NEW.ElectionDateID, NEW.ElectionTitle, NEW.StartDate, NEW.EndDate));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_update_ElectionDates
AFTER UPDATE ON ElectionDates 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value, new_value)
    VALUES ('ElectionDates', 'UPDATE', 
        CONCAT_WS(', ', 
            OLD.ElectionDateID, OLD.ElectionTitle, OLD.StartDate, OLD.EndDate),
        CONCAT_WS(', ', 
            NEW.ElectionDateID, NEW.ElectionTitle, NEW.StartDate, NEW.EndDate));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_delete_ElectionDates
AFTER DELETE ON ElectionDates 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value)
    VALUES ('ElectionDates', 'DELETE', CONCAT_WS(', ', 
        OLD.ElectionDateID, OLD.ElectionTitle, OLD.StartDate, OLD.EndDate));
END $$

DELIMITER ;

-- End Triggers For Election Dates

-- Start Triggers for Election Candidates
DELIMITER $$

CREATE TRIGGER after_insert_ElectionCandidates
AFTER INSERT ON ElectionCandidates 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, new_value)
    VALUES ('ElectionCandidates', 'INSERT', CONCAT_WS(', ', 
        NEW.CandidateID, NEW.ElectionTitle, NEW.ElectoralRace, NEW.CandidateFirstName, NEW.CandidateLastName));
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_update_ElectionCandidates
AFTER UPDATE ON ElectionCandidates 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value, new_value)
    VALUES ('ElectionCandidates', 'UPDATE', 
        CONCAT_WS(', ', 
            OLD.CandidateID, OLD.ElectionTitle, OLD.ElectoralRace, OLD.CandidateFirstName, OLD.CandidateLastName),
        CONCAT_WS(', ', 
            NEW.CandidateID, NEW.ElectionTitle, NEW.ElectoralRace, NEW.CandidateFirstName, NEW.CandidateLastName));
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_delete_ElectionCandidates
AFTER DELETE ON ElectionCandidates 
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, old_value)
    VALUES ('ElectionCandidates', 'DELETE', CONCAT_WS(', ', 
        OLD.CandidateID, OLD.ElectionTitle, OLD.ElectoralRace, OLD.CandidateFirstName, OLD.CandidateLastName));
END$$

DELIMITER ;

-- END Triggers for Election Candidates
-- 
-- 
-- 
-- 
-- END AUDIT TRIGGERS

DELIMITER $$
USE `voterdb`$$
CREATE PROCEDURE `assign_manager` (
  IN ManagerID int,
  IN PID int,
  IN PName varchar(100)
) BEGIN
UPDATE voterdb.Precincts
SET
  PollingManagerID = ManagerID
WHERE
  PrecinctID = PID and PrecinctName = PName;
END $$ 
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE `view_myprecinct` () BEGIN
SELECT 
P.PrecinctID, P.PrecinctName, P.NumberofCandidates, P.State, P.ZipCode, P.ZipPlus4Start, p.ZipPlus4End 
FROM Precincts P join Users U 
ON P.PollingManagerID = U.User_ID;
END $$ 
DELIMITER ;