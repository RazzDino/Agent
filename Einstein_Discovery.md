# Energy Bill Prediction - Technical Implementation Guide

This guide provides detailed technical information for implementing the Energy Bill Prediction system with Einstein Discovery.

## Table of Contents

1. [Required Fields & Validation Rules](#required-fields--validation-rules)
2. [Data Quality Assessment](#data-quality-assessment)
3. [Model Training & Evaluation](#model-training--evaluation)
4. [Deployment Configuration](#deployment-configuration)
5. [Customer Experience Integration](#customer-experience-integration)
6. [Monitoring & Maintenance](#monitoring--maintenance)
7. [Troubleshooting](#troubleshooting)

## Required Fields & Validation Rules

### Energy_Report__c Field Configuration

| Field Name | Field Type | Description | Required |
|------------|------------|-------------|----------|
| Account__c | Lookup(Account) | Related customer account | Yes |
| Report_Date__c | Date | Date of the energy report | Yes |
| Monthly_Usage__c | Number(10,2) | Total monthly energy usage in kWh | Yes |
| Peak_Usage__c | Number(10,2) | Peak hours usage in kWh | Yes |
| Off_Peak_Usage_kWh__c | Number(10,2) | Off-peak hours usage in kWh | Yes |
| Appliance_Count__c | Number(3,0) | Number of appliances in use | Yes |
| Previous_Bill_Amount__c | Currency(10,2) | Previous month's bill amount | Yes |
| Current_Bill_Amount__c | Currency(10,2) | Current month's bill amount | Yes |
| Weather_Impact__c | Number(3,1) | Weather impact factor (0-100) | No |
| Recommendation_Adopted__c | Checkbox | Whether customer adopted recommendations | No |
| High_Bill_Flag__c | Checkbox | Target field for prediction | Yes |
| Predicted_Bill_Amount__c | Currency(10,2) | Predicted bill amount | No |
| Prediction_Confidence__c | Number(3,1) | Confidence score (0-100) | No |
| Top_Factor_1__c | Text(255) | Primary contributing factor | No |
| Top_Factor_2__c | Text(255) | Secondary contributing factor | No |
| Top_Factor_3__c | Text(255) | Tertiary contributing factor | No |

### Validation Rules

#### High Bill Threshold Rule
```apex
// Validation Rule: High_Bill_Threshold_Validation
// Object: Energy_Report__c
// Error Condition Formula:
AND(
    NOT(ISNULL(Current_Bill_Amount__c)),
    NOT(ISNULL(Previous_Bill_Amount__c)),
    Current_Bill_Amount__c > (Previous_Bill_Amount__c * 1.25)
)
// Error Message: "Bill amount is 25% higher than previous month"
```

**Why This Validation is Needed:**
- **Prevents Data Anomalies**: Catches unusually high bills that might be data entry errors
- **Business Logic**: Ensures bills follow expected patterns
- **Model Training**: Helps identify genuine high bills vs. data errors
- **Customer Experience**: Prevents false alarms to customers

#### Usage Validation Rule
```apex
// Validation Rule: Usage_Validation
// Object: Energy_Report__c
// Error Condition Formula:
AND(
    NOT(ISNULL(Peak_Usage__c)),
    NOT(ISNULL(Off_Peak_Usage_kWh__c)),
    NOT(ISNULL(Monthly_Usage__c)),
    ABS((Peak_Usage__c + Off_Peak_Usage_kWh__c) - Monthly_Usage__c) > 0.01
)
// Error Message: "Peak + Off-peak usage must equal total monthly usage"
```

**Why This Validation is Needed:**
- **Mathematical Consistency**: Ensures peak + off-peak = total usage
- **Data Integrity**: Prevents logical inconsistencies in energy data
- **Model Accuracy**: Inconsistent data leads to poor predictions
- **Audit Trail**: Maintains data quality for compliance

#### Usage Range Validation
```apex
// Validation Rule: Usage_Range_Validation
// Object: Energy_Report__c
// Error Condition Formula:
OR(
    Monthly_Usage__c < 0,
    Monthly_Usage__c > 10000,
    Peak_Usage__c < 0,
    Peak_Usage__c > 8000,
    Off_Peak_Usage_kWh__c < 0,
    Off_Peak_Usage_kWh__c > 5000
)
// Error Message: "Usage values must be within reasonable ranges (0-10,000 kWh total, 0-8,000 kWh peak, 0-5,000 kWh off-peak)"
```

**Why This Validation is Needed:**
- **Prevents Outliers**: Stops unrealistic usage values from entering the system
- **Model Stability**: Extreme values can skew predictions
- **Business Reality**: Ensures data reflects real-world usage patterns
- **Data Quality**: Maintains reasonable bounds for energy consumption

#### Appliance Count Validation
```apex
// Validation Rule: Appliance_Count_Validation
// Object: Energy_Report__c
// Error Condition Formula:
OR(
    Appliance_Count__c < 1,
    Appliance_Count__c > 50
)
// Error Message: "Appliance count must be between 1 and 50"
```

**Why This Validation is Needed:**
- **Realistic Constraints**: Ensures appliance count is within reasonable limits
- **Model Features**: Appliance count is a key predictor variable
- **Data Quality**: Prevents impossible values from affecting predictions
- **Business Logic**: Reflects typical household/business appliance counts

#### Bill Amount Validation
```apex
// Validation Rule: Bill_Amount_Validation
// Object: Energy_Report__c
// Error Condition Formula:
OR(
    Current_Bill_Amount__c < 0,
    Current_Bill_Amount__c > 5000,
    Previous_Bill_Amount__c < 0,
    Previous_Bill_Amount__c > 5000
)
// Error Message: "Bill amounts must be between $0 and $5,000"
```

**Why This Validation is Needed:**
- **Financial Constraints**: Ensures bill amounts are within realistic ranges
- **Target Variable**: Bill amounts are critical for prediction accuracy
- **Data Quality**: Prevents negative or unrealistic bill values
- **Business Rules**: Reflects typical energy bill ranges

#### Weather Impact Validation
```apex
// Validation Rule: Weather_Impact_Validation
// Object: Energy_Report__c
// Error Condition Formula:
AND(
    NOT(ISNULL(Weather_Impact__c)),
    OR(
        Weather_Impact__c < 0,
        Weather_Impact__c > 100
    )
)
// Error Message: "Weather impact must be between 0 and 100"
```

**Why This Validation is Needed:**
- **Scale Consistency**: Weather impact is a percentage (0-100)
- **Model Features**: Weather impact influences energy consumption
- **Data Quality**: Ensures weather data is properly normalized
- **Business Logic**: Weather impact should be a percentage value

#### Date Validation
```apex
// Validation Rule: Report_Date_Validation
// Object: Energy_Report__c
// Error Condition Formula:
OR(
    Report_Date__c > TODAY(),
    Report_Date__c < DATE(2020, 1, 1)
)
// Error Message: "Report date must be between January 1, 2020 and today"
```

**Why This Validation is Needed:**
- **Temporal Logic**: Prevents future dates and very old dates
- **Data Relevance**: Ensures data is current and relevant
- **Model Training**: Recent data is more valuable for predictions
- **Business Continuity**: Maintains data timeline integrity

#### Account Relationship Validation
```apex
// Validation Rule: Account_Relationship_Validation
// Object: Energy_Report__c
// Error Condition Formula:
ISNULL(Account__c)
// Error Message: "Energy report must be associated with a customer account"
```

**Why This Validation is Needed:**
- **Data Relationships**: Ensures proper customer association
- **Business Logic**: Energy reports must belong to customers
- **Reporting**: Enables customer-specific analysis
- **Model Context**: Customer data provides important context for predictions

## Data Quality Assessment

### Required Data Quality Checks

#### Completeness Check
```sql
SELECT COUNT(Id), 
       COUNT(Monthly_Usage__c), 
       COUNT(Peak_Usage__c),
       COUNT(Off_Peak_Usage_kWh__c),
       COUNT(Appliance_Count__c),
       COUNT(Previous_Bill_Amount__c),
       COUNT(Current_Bill_Amount__c)
FROM Energy_Report__c
WHERE Report_Date__c >= LAST_N_MONTHS:6
```

### Data Cleaning Scripts

#### Apex Class for Data Preparation
- **EnergyTrainingDataGenerator**
- **ImprovedEnergyTestDataGenerator**

```apex
// Execute Energy Test Data Generation
// This script will create 1000 Energy Report records

// Option 1: Generate 1000 records (10 accounts × 100 records each)
System.debug('Starting Energy Test Data Generation...');
ImprovedEnergyTestDataGenerator.generateTestData();

// Option 2: Generate smaller test dataset (100 records)
// ImprovedEnergyTestDataGenerator.generateSmallTestData();

// Option 3: Clean up test data (uncomment if needed)
// ImprovedEnergyTestDataGenerator.cleanupTestData();

System.debug('Energy Test Data Generation completed!');
```

## Model Training & Evaluation

### Key Metrics to Monitor

1. **Accuracy**: Should be > 80%
2. **Precision**: Should be > 75%
3. **Recall**: Should be > 70%
4. **F1-Score**: Should be > 0.75
5. **AUC-ROC**: Should be > 0.80

### Model Scorecard Analysis

1. **Feature Importance**
   - Top factors influencing high bills
   - Relative importance scores
   - Direction of impact

2. **Insights Discovery**
   - Usage patterns correlation
   - Seasonal effects
   - Behavioral factors

## Deployment Configuration

### Deploy Model to Production

1. **Navigate to Model Details**
   - Go to your trained model
   - Click **Deploy**

2. **Configure Deployment Settings**
   - **Deployment Name**: "Energy Bill Prediction Production"
   - **Target Object**: `Energy_Report__c`
   - **Prediction Field**: `High_Bill_Flag__c`
   - **Confidence Field**: `Prediction_Confidence__c`
   - **Score Field**: `Prediction_Score__c`

3. **Set Refresh Schedule**
   - **Frequency**: Daily
   - **Time**: 2:00 AM
   - **Timezone**: Your org's timezone

### Create Prediction Flow

#### Flow Configuration

1. **Navigate to Flow Builder**
   - Go to **Setup** > **Process Automation** > **Flow**
   - Click **New Flow**

2. **Configure Flow Trigger**
   - **Trigger**: When a record is created or updated
   - **Object**: Energy_Report__c
   - **Entry Conditions**: 
     - `Monthly_Usage__c` is not null
     - `Peak_Usage__c` is not null
     - `Off_Peak_Usage_kWh__c` is not null

3. **Add Einstein Prediction Element**
   - **Element Type**: Einstein Prediction
   - **Model**: Energy Bill Prediction Model
   - **Input Fields**: Map all predictor fields
   - **Output Fields**: Map prediction results

4. **Add Decision Element**
   - **Condition**: `High_Bill_Flag__c` equals true
   - **True Path**: Send notification/alert
   - **False Path**: Continue normal process

### Create Apex Trigger for Real-time Predictions

```apex
trigger EnergyReportTrigger on Energy_Report__c (after insert, after update) {
    
    if(Trigger.isAfter) {
        if(Trigger.isInsert || Trigger.isUpdate) {
            List<Energy_Report__c> reportsForPrediction = new List<Energy_Report__c>();
            
            for(Energy_Report__c report : Trigger.new) {
                // Check if required fields are populated
                if(report.Monthly_Usage__c != null && 
                   report.Peak_Usage__c != null && 
                   report.Off_Peak_Usage_kWh__c != null &&
                   report.Appliance_Count__c != null &&
                   report.Previous_Bill_Amount__c != null) {
                    reportsForPrediction.add(report);
                }
            }
            
            if(!reportsForPrediction.isEmpty()) {
                // Call Einstein Discovery API
                EnergyPredictionService.predictBills(reportsForPrediction);
            }
        }
    }
}
```

#### Einstein Prediction Service Class

```apex
public class EnergyPredictionService {
    
    @future(callout=true)
    public static void predictBills(List<Id> reportIds) {
        List<Energy_Report__c> reports = [
            SELECT Id, Monthly_Usage__c, Peak_Usage__c, Off_Peak_Usage_kWh__c,
                   Appliance_Count__c, Previous_Bill_Amount__c, Weather_Impact__c,
                   Recommendation_Adopted__c
            FROM Energy_Report__c
            WHERE Id IN :reportIds
        ];
        
        // Call Einstein Discovery API
        for(Energy_Report__c report : reports) {
            try {
                // Make API call to Einstein Discovery
                Map<String, Object> prediction = callEinsteinAPI(report);
                
                // Update record with prediction results
                report.High_Bill_Flag__c = (Boolean) prediction.get('prediction');
                report.Prediction_Confidence__c = (Decimal) prediction.get('confidence');
                report.Top_Factor_1__c = (String) prediction.get('factor1');
                report.Top_Factor_2__c = (String) prediction.get('factor2');
                report.Top_Factor_3__c = (String) prediction.get('factor3');
                
            } catch(Exception e) {
                System.debug('Error predicting bill for report ' + report.Id + ': ' + e.getMessage());
            }
        }
        
        update reports;
    }
    
    private static Map<String, Object> callEinsteinAPI(Energy_Report__c report) {
        // Implementation of Einstein Discovery API call
        // This would use the Einstein Discovery REST API
        // Return prediction results as Map<String, Object>
        
        // Placeholder implementation
        Map<String, Object> result = new Map<String, Object>();
        result.put('prediction', false);
        result.put('confidence', 0.75);
        result.put('factor1', 'High peak usage');
        result.put('factor2', 'Multiple appliances');
        result.put('factor3', 'Weather impact');
        
        return result;
    }
}
```

## Customer Experience Integration

### Create Lightning Component for Bill Insights

#### HTML Template
```html
<!-- energyBillInsights.html -->
<template>
    <lightning-card title="Energy Bill Insights" icon-name="utility:lightning">
        <div class="slds-p-around_medium">
            <!-- Prediction Status -->
            <div class="slds-grid slds-gutters">
                <div class="slds-col">
                    <div class="prediction-status">
                        <template if:true={isHighBill}>
                            <lightning-icon icon-name="utility:warning" 
                                          variant="warning" 
                                          size="small">
                            </lightning-icon>
                            <span class="slds-text-heading_small slds-text-color_error">
                                High Bill Predicted
                            </span>
                        </template>
                        <template if:false={isHighBill}>
                            <lightning-icon icon-name="utility:success" 
                                          variant="success" 
                                          size="small">
                            </lightning-icon>
                            <span class="slds-text-heading_small slds-text-color_success">
                                Normal Bill Expected
                            </span>
                        </template>
                    </div>
                </div>
                <div class="slds-col">
                    <div class="confidence-score">
                        <span class="slds-text-body_small">Confidence: {confidenceScore}%</span>
                    </div>
                </div>
            </div>
            
            <!-- Contributing Factors -->
            <template if:true={hasFactors}>
                <div class="slds-m-top_medium">
                    <h3 class="slds-text-heading_small">Why your bill is {billStatus}:</h3>
                    <ul class="slds-list_dotted">
                        <template for:each={contributingFactors} for:item="factor">
                            <li key={factor.id} class="slds-list__item">
                                {factor.description}
                            </li>
                        </template>
                    </ul>
                </div>
            </template>
            
            <!-- Recommendations -->
            <template if:true={hasRecommendations}>
                <div class="slds-m-top_medium">
                    <h3 class="slds-text-heading_small">Recommendations:</h3>
                    <ul class="slds-list_dotted">
                        <template for:each={recommendations} for:item="rec">
                            <li key={rec.id} class="slds-list__item">
                                {rec.description}
                            </li>
                        </template>
                    </ul>
                </div>
            </template>
        </div>
    </lightning-card>
</template>
```

#### JavaScript Controller
```javascript
// energyBillInsights.js
import { LightningElement, api, wire } from 'lwc';
import getEnergyReport from '@salesforce/apex/EnergyReportController.getEnergyReport';

export default class EnergyBillInsights extends LightningElement {
    @api recordId;
    
    energyReport;
    isHighBill = false;
    confidenceScore = 0;
    contributingFactors = [];
    recommendations = [];
    
    @wire(getEnergyReport, { recordId: '$recordId' })
    wiredEnergyReport({ error, data }) {
        if (data) {
            this.energyReport = data;
            this.processPredictionData();
        } else if (error) {
            console.error('Error loading energy report:', error);
        }
    }
    
    processPredictionData() {
        if (this.energyReport) {
            this.isHighBill = this.energyReport.High_Bill_Flag__c;
            this.confidenceScore = this.energyReport.Prediction_Confidence__c || 0;
            
            // Process contributing factors
            this.contributingFactors = this.getContributingFactors();
            this.recommendations = this.getRecommendations();
        }
    }
    
    get hasFactors() {
        return this.contributingFactors.length > 0;
    }
    
    get hasRecommendations() {
        return this.recommendations.length > 0;
    }
    
    get billStatus() {
        return this.isHighBill ? 'high' : 'normal';
    }
    
    getContributingFactors() {
        const factors = [];
        
        if (this.energyReport.Top_Factor_1__c) {
            factors.push({
                id: 'factor1',
                description: this.energyReport.Top_Factor_1__c
            });
        }
        
        if (this.energyReport.Top_Factor_2__c) {
            factors.push({
                id: 'factor2',
                description: this.energyReport.Top_Factor_2__c
            });
        }
        
        if (this.energyReport.Top_Factor_3__c) {
            factors.push({
                id: 'factor3',
                description: this.energyReport.Top_Factor_3__c
            });
        }
        
        return factors;
    }
    
    getRecommendations() {
        const recommendations = [];
        
        if (this.isHighBill) {
            if (this.energyReport.Peak_Usage__c > (this.energyReport.Monthly_Usage__c * 0.6)) {
                recommendations.push({
                    id: 'peak_usage',
                    description: 'Consider shifting energy usage to off-peak hours to reduce costs.'
                });
            }
            
            if (this.energyReport.Appliance_Count__c > 10) {
                recommendations.push({
                    id: 'appliance_count',
                    description: 'Review and optimize appliance usage to reduce energy consumption.'
                });
            }
            
            if (!this.energyReport.Recommendation_Adopted__c) {
                recommendations.push({
                    id: 'adopt_recommendations',
                    description: 'Implement previously suggested energy-saving measures.'
                });
            }
        }
        
        return recommendations;
    }
}
```

#### CSS Styling
```css
/* energyBillInsights.css */
.prediction-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.confidence-score {
    text-align: right;
    color: var(--lwc-colorTextLabel);
}

.slds-list_dotted {
    list-style-type: disc;
    padding-left: 1rem;
}

.slds-list__item {
    margin-bottom: 0.25rem;
}
```

### Create Apex Controller

```apex
public class EnergyReportController {
    
    @AuraEnabled(cacheable=true)
    public static Energy_Report__c getEnergyReport(Id recordId) {
        return [
            SELECT Id, Name, Account__c, Report_Date__c,
                   Monthly_Usage__c, Peak_Usage__c, Off_Peak_Usage_kWh__c,
                   Appliance_Count__c, Previous_Bill_Amount__c, Current_Bill_Amount__c,
                   Weather_Impact__c, Recommendation_Adopted__c,
                   High_Bill_Flag__c, Prediction_Confidence__c,
                   Top_Factor_1__c, Top_Factor_2__c, Top_Factor_3__c
            FROM Energy_Report__c
            WHERE Id = :recordId
        ];
    }
    
    @AuraEnabled
    public static void updateRecommendationAdoption(Id recordId, Boolean adopted) {
        Energy_Report__c report = new Energy_Report__c(
            Id = recordId,
            Recommendation_Adopted__c = adopted
        );
        update report;
    }
}
```

## Monitoring & Maintenance

### Model Performance Monitoring

#### Create Dashboard for Model Metrics

1. **Navigate to Reports & Dashboards**
   - Go to **Reports** > **New Report**
   - Select **Custom Report Type** > **Energy Reports**

2. **Create Model Performance Report**
   ```sql
   -- SOQL for model performance
   SELECT 
       COUNT(Id) as Total_Records,
       SUM(CASE WHEN High_Bill_Flag__c = true THEN 1 ELSE 0 END) as High_Bills,
       AVG(Prediction_Confidence__c) as Avg_Confidence,
       AVG(CASE WHEN High_Bill_Flag__c = true THEN Prediction_Confidence__c ELSE null END) as High_Bill_Confidence
   FROM Energy_Report__c
   WHERE Report_Date__c >= LAST_N_MONTHS:1
   ```

3. **Create Dashboard Components**
   - **Chart**: Prediction accuracy over time
   - **Metric**: Average confidence score
   - **Table**: Top contributing factors
   - **Gauge**: Model performance score

### Automated Model Retraining

#### Create Scheduled Job for Model Updates

```apex
public class EinsteinModelRetrainScheduler implements Schedulable {
    
    public void execute(SchedulableContext sc) {
        // Check if model needs retraining
        if(shouldRetrainModel()) {
            // Trigger model retraining
            retrainModel();
        }
    }
    
    private Boolean shouldRetrainModel() {
        // Check model performance metrics
        // Retrain if accuracy drops below threshold
        AggregateResult result = [
            SELECT AVG(Prediction_Confidence__c) avgConfidence
            FROM Energy_Report__c
            WHERE Report_Date__c >= LAST_N_DAYS:30
        ];
        
        Decimal avgConfidence = (Decimal) result.get('avgConfidence');
        return avgConfidence < 0.75; // Retrain if confidence drops below 75%
    }
    
    private void retrainModel() {
        // Call Einstein Discovery API to retrain model
        // This would involve API calls to trigger retraining
        System.debug('Triggering model retraining...');
    }
}
```

### Data Quality Monitoring

#### Create Data Quality Validation

```apex
public class EnergyDataQualityMonitor {
    
    public static void validateDataQuality() {
        // Check for missing data
        List<Energy_Report__c> incompleteRecords = [
            SELECT Id, Name, Account__c, Report_Date__c
            FROM Energy_Report__c
            WHERE Monthly_Usage__c = null
            OR Peak_Usage__c = null
            OR Off_Peak_Usage_kWh__c = null
            OR Appliance_Count__c = null
            OR Previous_Bill_Amount__c = null
        ];
        
        if(!incompleteRecords.isEmpty()) {
            // Send notification to admin
            sendDataQualityAlert(incompleteRecords);
        }
        
        // Check for outliers
        validateOutliers();
    }
    
    private static void validateOutliers() {
        // Calculate statistical outliers
        AggregateResult stats = [
            SELECT 
                AVG(Monthly_Usage__c) avgUsage,
                STDDEV(Monthly_Usage__c) stdDevUsage
            FROM Energy_Report__c
            WHERE Report_Date__c >= LAST_N_MONTHS:3
        ];
        
        Decimal avgUsage = (Decimal) stats.get('avgUsage');
        Decimal stdDevUsage = (Decimal) stats.get('stdDevUsage');
        Decimal upperBound = avgUsage + (2 * stdDevUsage);
        
        List<Energy_Report__c> outliers = [
            SELECT Id, Name, Monthly_Usage__c
            FROM Energy_Report__c
            WHERE Monthly_Usage__c > :upperBound
            AND Report_Date__c >= LAST_N_MONTHS:1
        ];
        
        if(!outliers.isEmpty()) {
            // Flag outliers for review
            flagOutliersForReview(outliers);
        }
    }
    
    private static void sendDataQualityAlert(List<Energy_Report__c> records) {
        // Send email notification to admin
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
        mail.setToAddresses(new String[] {'admin@yourcompany.com'});
        mail.setSubject('Energy Data Quality Alert');
        mail.setPlainTextBody('Found ' + records.size() + ' incomplete energy reports that need attention.');
        Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });
    }
    
    private static void flagOutliersForReview(List<Energy_Report__c> outliers) {
        // Mark outliers for manual review
        for(Energy_Report__c outlier : outliers) {
            // Add a custom field to flag for review
            // outlier.Needs_Review__c = true;
        }
        // update outliers;
    }
}
```

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Model Training Fails
**Symptoms**: Model creation fails with insufficient data error
**Solution**:
- Ensure minimum 1,000 records in training dataset
- Check data quality and completeness
- Verify all required fields are populated

#### Issue 2: Low Prediction Accuracy
**Symptoms**: Model accuracy below 80%
**Solutions**:
- Review feature selection
- Check for data leakage
- Increase training data volume
- Add more relevant features

#### Issue 3: Predictions Not Updating
**Symptoms**: Real-time predictions not working
**Solutions**:
- Verify Flow configuration
- Check Apex trigger deployment
- Review Einstein Discovery API permissions
- Test API connectivity

#### Issue 4: High False Positives
**Symptoms**: Too many false high bill predictions
**Solutions**:
- Adjust prediction threshold
- Review feature importance
- Add more negative examples to training data
- Implement business rules for validation

### Debugging Tools

#### Create Debug Logging

```apex
public class EinsteinDebugLogger {
    
    public static void logPrediction(String recordId, Map<String, Object> prediction, String error) {
        // Create custom debug log record
        Einstein_Debug_Log__c log = new Einstein_Debug_Log__c(
            Record_Id__c = recordId,
            Prediction_Result__c = JSON.serialize(prediction),
            Error_Message__c = error,
            Timestamp__c = Datetime.now()
        );
        insert log;
    }
    
    public static void logModelPerformance(String modelId, Decimal accuracy, Decimal precision, Decimal recall) {
        // Log model performance metrics
        Model_Performance_Log__c log = new Model_Performance_Log__c(
            Model_Id__c = modelId,
            Accuracy__c = accuracy,
            Precision__c = precision,
            Recall__c = recall,
            Log_Date__c = Date.today()
        );
        insert log;
    }
}
```
