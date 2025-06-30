-- Feature-Persona Data Structure
-- This script creates tables and inserts data for the utility management system

-- Create Personas table
CREATE TABLE Personas (
    persona_id INT PRIMARY KEY IDENTITY(1,1),
    persona_name VARCHAR(100) NOT NULL,
    persona_code VARCHAR(50) NOT NULL,
    description TEXT,
    created_date DATETIME DEFAULT GETDATE(),
    updated_date DATETIME DEFAULT GETDATE()
);

-- Create Features table
CREATE TABLE Features (
    feature_id INT PRIMARY KEY IDENTITY(1,1),
    feature_name VARCHAR(100) NOT NULL,
    feature_code VARCHAR(50) NOT NULL,
    description TEXT,
    created_date DATETIME DEFAULT GETDATE(),
    updated_date DATETIME DEFAULT GETDATE()
);

-- Create Feature-Persona Capabilities table
CREATE TABLE FeaturePersonaCapabilities (
    capability_id INT PRIMARY KEY IDENTITY(1,1),
    feature_id INT,
    persona_id INT,
    capability_description TEXT NOT NULL,
    is_active BIT DEFAULT 1,
    created_date DATETIME DEFAULT GETDATE(),
    updated_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (feature_id) REFERENCES Features(feature_id),
    FOREIGN KEY (persona_id) REFERENCES Personas(persona_id)
);

-- Insert Personas data
INSERT INTO Personas (persona_name, persona_code, description) VALUES
('Residential Customer (RC Demo User)', 'RC_DEMO_USER', 'End customer who uses the utility services'),
('Utility Operations Manager (UOM Demo User)', 'UOM_DEMO_USER', 'Manager responsible for utility operations and monitoring'),
('Customer Support Agent (Agentforce)', 'AGENTFORCE', 'Support agent who assists customers and manages interactions');

-- Insert Features data
INSERT INTO Features (feature_name, feature_code, description) VALUES
('Smart_Meter_Request__c', 'SMART_METER_REQUEST', 'Smart meter installation management'),
('Energy_Usage_Feed__c', 'ENERGY_USAGE_FEED', 'Real-time energy consumption data'),
('Energy_Report__c', 'ENERGY_REPORT', 'Monthly energy reporting'),
('Product_Recommendation__c', 'PRODUCT_RECOMMENDATION', 'Product suggestions and campaigns'),
('Interaction_Log__c', 'INTERACTION_LOG', 'Customer interaction tracking'),
('Order__c', 'ORDER', 'Product ordering system'),
('Email_Campaign__c', 'EMAIL_CAMPAIGN', 'Email marketing and communication');

-- Insert Feature-Persona Capabilities data
INSERT INTO FeaturePersonaCapabilities (feature_id, persona_id, capability_description) VALUES
-- Smart_Meter_Request__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'SMART_METER_REQUEST'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'Request smart meter installation'),

((SELECT feature_id FROM Features WHERE feature_code = 'SMART_METER_REQUEST'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Monitor installation requests'),

((SELECT feature_id FROM Features WHERE feature_code = 'SMART_METER_REQUEST'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Confirm installation and educate customer'),

-- Energy_Usage_Feed__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'ENERGY_USAGE_FEED'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'View hourly energy usage'),

((SELECT feature_id FROM Features WHERE feature_code = 'ENERGY_USAGE_FEED'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Monitor grid load and peak demand'),

((SELECT feature_id FROM Features WHERE feature_code = 'ENERGY_USAGE_FEED'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Analyze usage patterns'),

-- Energy_Report__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'ENERGY_REPORT'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'Receive monthly energy report'),

((SELECT feature_id FROM Features WHERE feature_code = 'ENERGY_REPORT'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Review audit outcomes'),

((SELECT feature_id FROM Features WHERE feature_code = 'ENERGY_REPORT'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Summarize reports for customer'),

-- Product_Recommendation__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'PRODUCT_RECOMMENDATION'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'Receive product recommendations'),

((SELECT feature_id FROM Features WHERE feature_code = 'PRODUCT_RECOMMENDATION'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Trigger TOU plan campaigns'),

((SELECT feature_id FROM Features WHERE feature_code = 'PRODUCT_RECOMMENDATION'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Suggest products based on usage'),

-- Interaction_Log__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'INTERACTION_LOG'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'Log interactions with support'),

((SELECT feature_id FROM Features WHERE feature_code = 'INTERACTION_LOG'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Review agent performance'),

((SELECT feature_id FROM Features WHERE feature_code = 'INTERACTION_LOG'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Log chat history'),

-- Order__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'ORDER'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'Purchase smart thermostat'),

((SELECT feature_id FROM Features WHERE feature_code = 'ORDER'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Monitor bulk orders'),

((SELECT feature_id FROM Features WHERE feature_code = 'ORDER'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Track product purchases'),

-- Email_Campaign__c capabilities
((SELECT feature_id FROM Features WHERE feature_code = 'EMAIL_CAMPAIGN'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'RC_DEMO_USER'), 
 'Receive personalized energy tips'),

((SELECT feature_id FROM Features WHERE feature_code = 'EMAIL_CAMPAIGN'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'UOM_DEMO_USER'), 
 'Trigger email campaigns'),

((SELECT feature_id FROM Features WHERE feature_code = 'EMAIL_CAMPAIGN'), 
 (SELECT persona_id FROM Personas WHERE persona_code = 'AGENTFORCE'), 
 'Send follow-up emails');

-- Create view for easy querying
CREATE VIEW FeaturePersonaMatrix AS
SELECT 
    f.feature_name,
    f.feature_code,
    p.persona_name,
    p.persona_code,
    fpc.capability_description,
    fpc.is_active
FROM Features f
CROSS JOIN Personas p
LEFT JOIN FeaturePersonaCapabilities fpc ON f.feature_id = fpc.feature_id AND p.persona_id = fpc.persona_id
WHERE fpc.is_active = 1;

-- Sample queries
-- Get all capabilities for a specific persona
-- SELECT * FROM FeaturePersonaMatrix WHERE persona_code = 'RC_DEMO_USER';

-- Get all personas for a specific feature
-- SELECT * FROM FeaturePersonaMatrix WHERE feature_code = 'SMART_METER_REQUEST';

-- Get feature-persona matrix
-- SELECT feature_name, persona_name, capability_description FROM FeaturePersonaMatrix ORDER BY feature_name, persona_name; 