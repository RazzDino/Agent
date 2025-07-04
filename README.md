# Einstein Discovery Objects and Fields Documentation

## Overview
This document outlines the complete object and field structure needed for Einstein Discovery training focused on energy usage analytics. The structure includes enhanced versions of existing Energy Report and Energy Feed objects, plus new supporting objects for comprehensive energy consumption analysis and prediction based on real-world training data.

## Objects and Fields Structure

### 1. Energy Report Object (Enhanced)
**Object API Name:** `Energy_Report__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Customer__c` | Lookup | Reference | Link to Account | Account |
| `Record_ID__c` | Text | Text | Unique record identifier | - |
| `Report_Date__c` | Date | Date | Date of energy report | - |
| `Report_Time__c` | Time | Time | Time of energy reading | - |
| `Timestamp__c` | DateTime | DateTime | Full timestamp of reading | - |
| `Hour__c` | Number | Number | Hour of day (0-23) | - |
| `Day_of_Week__c` | Picklist | Text | Day of the week | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday |
| `Month__c` | Number | Number | Month (1-12) | - |
| `Season__c` | Picklist | Text | Season | Winter, Spring, Summer, Fall |
| `Is_Weekend__c` | Checkbox | Boolean | Whether reading is on weekend | - |
| `Is_Holiday__c` | Checkbox | Boolean | Whether reading is on holiday | - |
| `Energy_Usage_kWh__c` | Currency | Currency | Total energy usage in kWh | - |
| `Peak_Hours_Usage__c` | Currency | Currency | Energy usage during peak hours | - |
| `Off_Peak_Hours_Usage__c` | Currency | Currency | Energy usage during off-peak hours | - |
| `Usage_per_Person__c` | Currency | Currency | Energy usage per person | - |
| `Usage_per_SqFt__c` | Currency | Currency | Energy usage per square foot | - |
| `Smart_Meter_Installed__c` | Checkbox | Boolean | Whether smart meter is installed | - |
| `Home_Size_SqFt__c` | Number | Number | Home size in square feet | - |
| `Occupants__c` | Number | Number | Number of occupants | - |
| `Income_Level__c` | Picklist | Text | Income level | Low, Medium, High, Very_High |
| `Age_Group__c` | Picklist | Text | Age group | 18-25, 26-35, 36-45, 46-55, 56-65, 65+ |
| `Family_Size__c` | Number | Number | Family size | - |
| `Climate_Zone__c` | Picklist | Text | Climate zone | Polar, Tropical, Temperate, Subtropical, Continental |
| `Urban_Setting__c` | Picklist | Text | Urban setting | Urban, Suburban, Rural |
| `Energy_Source__c` | Picklist | Text | Primary energy source | Grid, Solar, Wind, Hybrid, Battery_Backup |
| `Meter_Type__c` | Picklist | Text | Meter type | Smart_Meter, Digital_Meter, Analog_Meter |
| `Grid_Reliability__c` | Picklist | Text | Grid reliability | Poor, Fair, Good, Excellent |
| `Building_Type__c` | Picklist | Text | Building type | Single_Family, Apartment, Condo, Townhouse, Office, Warehouse |
| `Construction_Year__c` | Number | Number | Year building was constructed | - |
| `Energy_Certification__c` | Picklist | Text | Energy certification | None, Energy_Star, LEED_Gold, LEED_Silver, LEED_Platinum |
| `Appliance_Count__c` | Number | Number | Number of appliances | - |
| `Appliances__c` | Long Text Area | Text | List of appliances | - |
| `Heating_Type__c` | Picklist | Text | Type of heating system | Natural_Gas, Electric, Propane, Oil, Heat_Pump |
| `Cooling_Type__c` | Picklist | Text | Type of cooling system | Central_AC, Heat_Pump, Window_AC, Mini_Split, None |
| `Roof_Insulation__c` | Picklist | Text | Roof insulation quality | Poor, Fair, Good, Excellent |
| `Window_Efficiency__c` | Picklist | Text | Window efficiency rating | Single_Pane, Double_Pane, Triple_Pane, Low_E |
| `Lifestyle_Type__c` | Picklist | Text | Lifestyle classification | Minimalist, Average, High_Consumption, Tech_Heavy, Eco_Conscious |
| `Work_Pattern__c` | Picklist | Text | Work pattern | Office, Remote, Hybrid, Shift_Work, Unemployed |
| `Activity_Pattern__c` | Picklist | Text | Activity pattern | Early_Bird, Regular, Night_Owl, Irregular |
| `Usage_Pattern__c` | Picklist | Text | Usage pattern classification | Low_Usage, Moderate_Usage, High_Usage, Extreme_High |
| `Anomaly_Score__c` | Number | Number | Anomaly detection score (0-1) | - |
| `Energy_Efficiency_Rating__c` | Number | Number | Energy efficiency rating (0-100) | - |
| `Carbon_Footprint_kg__c` | Number | Number | Carbon footprint in kg | - |
| `Cost_Estimate_USD__c` | Currency | Currency | Estimated cost in USD | - |
| `Savings_Potential_Percent__c` | Number | Number | Potential savings percentage | - |
| `Usage_Description__c` | Long Text Area | Text | Description of usage pattern | - |
| `Efficiency_Insights__c` | Long Text Area | Text | Efficiency insights and analysis | - |
| `Recommendations__c` | Long Text Area | Text | Energy saving recommendations | - |
| `Weather_Temperature__c` | Number | Number | Temperature in Fahrenheit | - |
| `Weather_Humidity__c` | Number | Number | Humidity percentage | - |
| `Weather_Condition__c` | Picklist | Text | Weather condition | Sunny, Cloudy, Rainy, Snowy, Stormy |

### 2. Energy Feed Object (Enhanced)
**Object API Name:** `Energy_Feed__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Energy_Report__c` | Master-Detail | Reference | Parent Energy Report | Energy_Report__c |
| `Feed_Type__c` | Picklist | Text | Type of energy feed | Real_Time, Historical, Predictive, Anomaly |
| `Feed_Date__c` | Date | Date | Date of feed data | - |
| `Feed_Time__c` | Time | Time | Time of feed data | - |
| `Raw_Energy_Data__c` | Long Text Area | Text | Raw energy consumption data | - |
| `Processed_Energy_Data__c` | Long Text Area | Text | Processed energy data | - |
| `Data_Quality_Score__c` | Number | Number | Data quality score (0-100) | - |
| `Processing_Status__c` | Picklist | Text | Data processing status | Pending, Processing, Completed, Failed |
| `Error_Message__c` | Text Area | Text | Error message if processing failed | - |
| `Data_Source__c` | Picklist | Text | Source of energy data | Smart_Meter, Manual_Entry, API, IoT_Device |
| `Confidence_Score__c` | Number | Number | Confidence score for predictions | - |
| `Device_ID__c` | Text | Text | Smart meter or device identifier | - |
| `Data_Frequency__c` | Picklist | Text | Data collection frequency | Hourly, Daily, Weekly, Monthly |

### 3. Customer Profile Object (Enhanced)
**Object API Name:** `Customer_Profile__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Account__c` | Lookup | Reference | Related Account | Account |
| `Customer_ID__c` | Text | Text | Unique customer identifier | - |
| `Customer_Type__c` | Picklist | Text | Type of customer | Residential, Small_Business, Large_Business, Industrial |
| `Account_Status__c` | Picklist | Text | Account status | Active, Inactive, Suspended, Pending |
| `Primary_Contact__c` | Lookup | Reference | Primary contact | Contact |
| `Account_Manager__c` | Lookup | Reference | Account manager | User |
| `Contract_Start_Date__c` | Date | Date | Contract start date | - |
| `Contract_End_Date__c` | Date | Date | Contract end date | - |
| `Service_Plan__c` | Picklist | Text | Service plan type | Basic, Standard, Premium, Enterprise |
| `Payment_Terms__c` | Picklist | Text | Payment terms | Net_30, Net_60, Net_90, Immediate |
| `Credit_Limit__c` | Currency | Currency | Credit limit | - |
| `Risk_Score__c` | Number | Number | Risk assessment score | - |
| `Energy_Consumption_Tier__c` | Picklist | Text | Energy consumption tier | Low, Medium, High, Very_High |
| `Billing_Cycle__c` | Picklist | Text | Billing cycle | Monthly, Bi_Monthly, Quarterly |
| `Service_Address__c` | Lookup | Reference | Service address | Address__c |
| `Income_Level__c` | Picklist | Text | Income level | Low, Medium, High, Very_High |
| `Age_Group__c` | Picklist | Text | Age group | 18-25, 26-35, 36-45, 46-55, 56-65, 65+ |
| `Family_Size__c` | Number | Number | Family size | - |
| `Lifestyle_Type__c` | Picklist | Text | Lifestyle classification | Minimalist, Average, High_Consumption, Tech_Heavy, Eco_Conscious |
| `Work_Pattern__c` | Picklist | Text | Work pattern | Office, Remote, Hybrid, Shift_Work, Unemployed |
| `Activity_Pattern__c` | Picklist | Text | Activity pattern | Early_Bird, Regular, Night_Owl, Irregular |

### 4. Address Object (Enhanced)
**Object API Name:** `Address__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Address_Type__c` | Picklist | Text | Type of address | Billing, Shipping, Service |
| `Address_Line_1__c` | Text | Text | Address line 1 | - |
| `Address_Line_2__c` | Text | Text | Address line 2 | - |
| `City__c` | Text | Text | City | - |
| `State__c` | Picklist | Text | State/Province | [Standard US States + International] |
| `Country__c` | Picklist | Text | Country | [Standard Countries] |
| `Postal_Code__c` | Text | Text | Postal/ZIP code | - |
| `County__c` | Text | Text | County | - |
| `Is_Active__c` | Checkbox | Boolean | Whether address is active | - |
| `Primary_Address__c` | Checkbox | Boolean | Whether this is the primary address | - |
| `Geolocation__c` | Geolocation | Location | Latitude and longitude | - |
| `Climate_Zone__c` | Picklist | Text | Climate zone | Polar, Tropical, Temperate, Subtropical, Continental |
| `Region__c` | Picklist | Text | Geographic region | Northeast, Southeast, Midwest, Southwest, West_Coast |
| `Urban_Setting__c` | Picklist | Text | Urban setting | Urban, Suburban, Rural |
| `Elevation__c` | Number | Number | Elevation in feet | - |

### 5. Energy Prediction Object (Enhanced)
**Object API Name:** `Energy_Prediction__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Customer_Profile__c` | Lookup | Reference | Customer profile | Customer_Profile__c |
| `Prediction_Date__c` | Date | Date | Date for prediction | - |
| `Prediction_Type__c` | Picklist | Text | Type of prediction | Daily, Weekly, Monthly, Seasonal |
| `Predicted_Energy_Usage__c` | Currency | Currency | Predicted energy usage in kWh | - |
| `Confidence_Level__c` | Number | Number | Confidence level (0-100) | - |
| `Prediction_Model__c` | Picklist | Text | Model used for prediction | Linear_Regression, Random_Forest, Neural_Network, Ensemble |
| `Model_Version__c` | Text | Text | Model version | - |
| `Prediction_Factors__c` | Long Text Area | Text | Key factors influencing prediction | - |
| `Actual_Usage__c` | Currency | Currency | Actual usage (for comparison) | - |
| `Prediction_Accuracy__c` | Number | Number | Prediction accuracy percentage | - |
| `Recommendations__c` | Long Text Area | Text | Energy saving recommendations | - |
| `Cost_Savings_Potential__c` | Currency | Currency | Potential cost savings | - |
| `Peak_Usage_Prediction__c` | Currency | Currency | Predicted peak usage | - |
| `Off_Peak_Usage_Prediction__c` | Currency | Currency | Predicted off-peak usage | - |
| `Carbon_Footprint_Prediction__c` | Number | Number | Predicted carbon footprint | - |
| `Savings_Percentage_Prediction__c` | Number | Number | Predicted savings percentage | - |

### 6. Energy Analytics Object (Enhanced)
**Object API Name:** `Energy_Analytics__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Customer_Profile__c` | Lookup | Reference | Customer profile | Customer_Profile__c |
| `Analysis_Period__c` | Picklist | Text | Analysis period | Daily, Weekly, Monthly, Quarterly, Yearly |
| `Start_Date__c` | Date | Date | Analysis start date | - |
| `End_Date__c` | Date | Date | Analysis end date | - |
| `Total_Energy_Consumed__c` | Currency | Currency | Total energy consumed in period | - |
| `Average_Daily_Usage__c` | Currency | Currency | Average daily usage | - |
| `Peak_Usage_Day__c` | Date | Date | Day with highest usage | - |
| `Lowest_Usage_Day__c` | Date | Date | Day with lowest usage | - |
| `Usage_Trend__c` | Picklist | Text | Usage trend | Increasing, Decreasing, Stable, Fluctuating |
| `Efficiency_Score__c` | Number | Number | Efficiency score (0-100) | - |
| `Cost_Analysis__c` | Currency | Currency | Total cost for period | - |
| `Savings_Opportunities__c` | Long Text Area | Text | Identified savings opportunities | - |
| `Comparison_to_Previous_Period__c` | Percent | Number | Percentage change from previous period | - |
| `Carbon_Footprint_Total__c` | Number | Number | Total carbon footprint for period | - |
| `Usage_per_Person_Average__c` | Currency | Currency | Average usage per person | - |
| `Usage_per_SqFt_Average__c` | Currency | Currency | Average usage per square foot | - |
| `Peak_Hours_Percentage__c` | Percent | Number | Percentage of usage during peak hours | - |
| `Weekend_Usage_Percentage__c` | Percent | Number | Percentage of usage on weekends | - |
| `Holiday_Usage_Percentage__c` | Percent | Number | Percentage of usage on holidays | - |

### 7. Building Profile Object (New)
**Object API Name:** `Building_Profile__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Address__c` | Lookup | Reference | Building address | Address__c |
| `Building_Type__c` | Picklist | Text | Building type | Single_Family, Apartment, Condo, Townhouse, Office, Warehouse |
| `Building_Size_SqFt__c` | Number | Number | Building size in square feet | - |
| `Construction_Year__c` | Number | Number | Year building was constructed | - |
| `Energy_Certification__c` | Picklist | Text | Energy certification | None, Energy_Star, LEED_Gold, LEED_Silver, LEED_Platinum |
| `Energy_Source__c` | Picklist | Text | Primary energy source | Grid, Solar, Wind, Hybrid, Battery_Backup |
| `Meter_Type__c` | Picklist | Text | Meter type | Smart_Meter, Digital_Meter, Analog_Meter |
| `Grid_Reliability__c` | Picklist | Text | Grid reliability | Poor, Fair, Good, Excellent |
| `Heating_Type__c` | Picklist | Text | Type of heating system | Natural_Gas, Electric, Propane, Oil, Heat_Pump |
| `Cooling_Type__c` | Picklist | Text | Type of cooling system | Central_AC, Heat_Pump, Window_AC, Mini_Split, None |
| `Roof_Insulation__c` | Picklist | Text | Roof insulation quality | Poor, Fair, Good, Excellent |
| `Window_Efficiency__c` | Picklist | Text | Window efficiency rating | Single_Pane, Double_Pane, Triple_Pane, Low_E |
| `Appliance_Count__c` | Number | Number | Number of appliances | - |
| `Appliances__c` | Long Text Area | Text | List of appliances | - |
| `Building_Age__c` | Formula | Number | Calculated building age | - |
| `Energy_Efficiency_Rating__c` | Number | Number | Energy efficiency rating (0-100) | - |

### 8. Lifestyle Pattern Object (New)
**Object API Name:** `Lifestyle_Pattern__c`

| Field Name | Field Type | Data Type | Description | Picklist Values (if applicable) |
|------------|------------|-----------|-------------|--------------------------------|
| `Name` | Auto Number | Text | Record Name | - |
| `Customer_Profile__c` | Lookup | Reference | Customer profile | Customer_Profile__c |
| `Lifestyle_Type__c` | Picklist | Text | Lifestyle classification | Minimalist, Average, High_Consumption, Tech_Heavy, Eco_Conscious |
| `Work_Pattern__c` | Picklist | Text | Work pattern | Office, Remote, Hybrid, Shift_Work, Unemployed |
| `Activity_Pattern__c` | Picklist | Text | Activity pattern | Early_Bird, Regular, Night_Owl, Irregular |
| `Usage_Pattern__c` | Picklist | Text | Usage pattern classification | Low_Usage, Moderate_Usage, High_Usage, Extreme_High |
| `Peak_Hours_Preference__c` | Picklist | Text | Peak hours usage preference | High, Medium, Low |
| `Weekend_Usage_Pattern__c` | Picklist | Text | Weekend usage pattern | Higher, Lower, Similar |
| `Holiday_Usage_Pattern__c` | Picklist | Text | Holiday usage pattern | Higher, Lower, Similar |
| `Seasonal_Variation__c` | Picklist | Text | Seasonal usage variation | High, Medium, Low |
| `Efficiency_Conscious__c` | Checkbox | Boolean | Whether customer is efficiency conscious | - |
| `Technology_Adoption__c` | Picklist | Text | Technology adoption level | High, Medium, Low |
| `Sustainability_Focus__c` | Checkbox | Boolean | Whether customer focuses on sustainability | - |

## Object Relationships

```
Account
├── Customer_Profile__c (1:1)
│   ├── Address__c (1:Many - Service Address)
│   ├── Energy_Prediction__c (1:Many)
│   ├── Energy_Analytics__c (1:Many)
│   └── Lifestyle_Pattern__c (1:1)
├── Energy_Report__c (1:Many)
│   └── Energy_Feed__c (1:Many - Master-Detail)
├── Building_Profile__c (1:Many)
│   └── Address__c (1:1)
└── Contact (1:Many)
```

## Einstein Discovery Training Configuration

### Primary Prediction Targets

1. **Energy Usage Prediction**
   - Target Field: `Energy_Usage_kWh__c`
   - Prediction Type: Regression
   - Use Cases: Daily, weekly, monthly energy consumption forecasting

2. **Anomaly Detection**
   - Target Field: `Anomaly_Score__c`
   - Prediction Type: Classification
   - Use Cases: Identify unusual energy consumption patterns

3. **Customer Risk Assessment**
   - Target Field: `Risk_Score__c`
   - Prediction Type: Regression
   - Use Cases: Assess customer credit and payment risk

4. **Energy Efficiency Optimization**
   - Target Field: `Energy_Efficiency_Rating__c`
   - Prediction Type: Regression
   - Use Cases: Predict efficiency improvements and recommendations

5. **Usage Pattern Classification**
   - Target Field: `Usage_Pattern__c`
   - Prediction Type: Classification
   - Use Cases: Classify customer usage patterns for targeted recommendations

6. **Lifestyle Type Classification**
   - Target Field: `Lifestyle_Type__c`
   - Prediction Type: Classification
   - Use Cases: Classify customer lifestyle for personalized recommendations

7. **Carbon Footprint Prediction**
   - Target Field: `Carbon_Footprint_kg__c`
   - Prediction Type: Regression
   - Use Cases: Predict environmental impact and sustainability metrics

### Key Features for Training

#### Temporal Features
- `Report_Date__c` - Date of energy reading
- `Report_Time__c` - Time of energy reading
- `Timestamp__c` - Full timestamp
- `Hour__c` - Hour of day (0-23)
- `Day_of_Week__c` - Day of the week
- `Month__c` - Month (1-12)
- `Season__c` - Season (Winter, Spring, Summer, Fall)
- `Is_Weekend__c` - Weekend indicator
- `Is_Holiday__c` - Holiday indicator

#### Customer Demographics
- `Age_Group__c` - Age group classification
- `Income_Level__c` - Income level (Low, Medium, High, Very_High)
- `Family_Size__c` - Number of family members
- `Customer_Type__c` - Customer type (Residential, Small_Business, Large_Business, Industrial)

#### Building Characteristics
- `Building_Type__c` - Type of building
- `Building_Size_SqFt__c` - Building size
- `Construction_Year__c` - Year built
- `Energy_Certification__c` - Energy certification
- `Climate_Zone__c` - Climate zone
- `Urban_Setting__c` - Urban setting
- `Heating_Type__c` - Heating system type
- `Cooling_Type__c` - Cooling system type
- `Roof_Insulation__c` - Roof insulation quality
- `Window_Efficiency__c` - Window efficiency

#### Technical Features
- `Energy_Source__c` - Primary energy source
- `Meter_Type__c` - Meter type
- `Grid_Reliability__c` - Grid reliability
- `Appliance_Count__c` - Number of appliances
- `Appliances__c` - List of appliances
- `Smart_Meter_Installed__c` - Smart meter presence

#### Behavioral Features
- `Lifestyle_Type__c` - Lifestyle classification
- `Work_Pattern__c` - Work pattern
- `Activity_Pattern__c` - Activity pattern
- `Usage_Pattern__c` - Usage pattern classification
- `Peak_Hours_Usage__c` - Peak hours usage
- `Off_Peak_Hours_Usage__c` - Off-peak hours usage
- `Usage_per_Person__c` - Usage per person
- `Usage_per_SqFt__c` - Usage per square foot

#### Environmental Features
- `Climate_Zone__c` - Climate zone
- `Season__c` - Season
- `Weather_Temperature__c` - Temperature
- `Weather_Humidity__c` - Humidity
- `Weather_Condition__c` - Weather condition
- `Region__c` - Geographic region

#### Financial Features
- `Income_Level__c` - Income level
- `Cost_Estimate_USD__c` - Cost estimate
- `Savings_Potential_Percent__c` - Savings potential
- `Credit_Limit__c` - Credit limit
- `Service_Plan__c` - Service plan type

#### Sustainability Features
- `Carbon_Footprint_kg__c` - Carbon footprint
- `Energy_Certification__c` - Energy certification
- `Lifestyle_Type__c` - Lifestyle type (Eco_Conscious)
- `Energy_Efficiency_Rating__c` - Efficiency rating

### Support Resources
- Einstein Discovery documentation
- Salesforce Trailhead modules
- Weather API documentation
- Energy efficiency certification guidelines
- Internal knowledge base and training materials

---

**Last Updated:** [06/07/2025]
**Version:** 2.0
**Author:** [Riyaz Shaik]
**Review Cycle:** Frequently 
