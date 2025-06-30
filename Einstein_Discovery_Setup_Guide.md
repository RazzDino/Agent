# Einstein Discovery Setup and Training Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Data Preparation](#data-preparation)
3. [Einstein Discovery Setup](#einstein-discovery-setup)
4. [Data Upload and Configuration](#data-upload-and-configuration)
5. [Model Training Process](#model-training-process)
6. [Analysis and Insights](#analysis-and-insights)
7. [Deployment and Integration](#deployment-and-integration)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Salesforce Requirements
- **Salesforce Edition:** Enterprise, Performance, or Unlimited Edition
- **Einstein Discovery Add-on:** Must be purchased and activated
- **User Permissions:** 
  - Einstein Discovery User permission set
  - Data Export permission
  - API access enabled

### Data Requirements
- **Minimum Records:** 500+ records
- **Data Quality:** Clean, consistent data with minimal missing values
- **Target Variable:** One field to predict or analyze
- **Features:** Multiple fields that influence the target

### System Requirements
- **Browser:** Chrome, Firefox, Safari, or Edge (latest versions)
- **Internet:** Stable connection for data upload and processing
- **Storage:** Sufficient space for data files and model artifacts

---

## Data Preparation

### Step 1: Review Your Generated Data
Your `llm_training_data.csv` file contains 1,000 records with the following structure:

```csv
record_id,customer_id,timestamp,date,time,hour,day_of_week,month,season,
is_weekend,is_holiday,customer_type,income_level,age_group,family_size,
region,climate_zone,urban_setting,energy_source,meter_type,grid_reliability,
building_type,building_size_sqft,construction_year,energy_certification,
energy_usage_kwh,peak_hours_usage,off_peak_hours_usage,usage_per_person,
usage_per_sqft,lifestyle_type,work_pattern,activity_pattern,efficiency_score,
usage_pattern,anomaly_score,appliance_count,appliances,carbon_footprint_kg,
cost_estimate_usd,savings_potential_percent,usage_description,
efficiency_insights,recommendations
```

### Step 2: Identify Target Variables
Choose one of these as your primary target for prediction:

1. **`energy_usage_kwh`** - Predict energy consumption
2. **`efficiency_score`** - Predict energy efficiency
3. **`usage_pattern`** - Classify usage patterns
4. **`anomaly_score`** - Detect anomalies
5. **`savings_potential_percent`** - Predict savings potential

### Step 3: Select Feature Variables
Choose relevant features that influence your target:

**Demographic Features:**
- `customer_type`, `income_level`, `age_group`, `family_size`

**Geographic Features:**
- `region`, `climate_zone`, `urban_setting`

**Building Features:**
- `building_type`, `building_size_sqft`, `construction_year`, `energy_certification`

**Behavioral Features:**
- `lifestyle_type`, `work_pattern`, `activity_pattern`

**Infrastructure Features:**
- `energy_source`, `meter_type`, `grid_reliability`

**Temporal Features:**
- `hour`, `day_of_week`, `month`, `season`, `is_weekend`, `is_holiday`

### Step 4: Data Cleaning (if needed)
```python
# Example data cleaning steps
import pandas as pd

# Load your data
df = pd.read_csv('llm_training_data.csv')

# Check for missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert categorical variables to numeric (if needed)
df['customer_type_encoded'] = pd.Categorical(df['customer_type']).codes

# Save cleaned data
df.to_csv('einstein_discovery_ready.csv', index=False)
```

---

## Einstein Discovery Setup

### Step 1: Access Einstein Discovery
1. **Login to Salesforce**
2. **Navigate to:** Setup → Einstein Discovery
3. **Click:** "Einstein Discovery" in the left sidebar
4. **Verify:** You see the Einstein Discovery dashboard

### Step 2: Configure User Permissions
1. **Go to:** Setup → Users → Permission Sets
2. **Find:** "Einstein Discovery User" permission set
3. **Assign:** To your user account
4. **Verify:** You can access Einstein Discovery features

### Step 3: Enable Data Sources
1. **Navigate to:** Einstein Discovery → Settings
2. **Enable:** External data sources (if using CSV upload)
3. **Configure:** Data refresh schedules
4. **Set up:** API connections (if needed)

---

## Data Upload and Configuration

### Step 1: Create a New Story
1. **Open:** Einstein Discovery
2. **Click:** "Create Story"
3. **Select:** "Upload Data" option
4. **Choose:** Your `llm_training_data.csv` file

### Step 2: Configure Data Schema
1. **Review:** Auto-detected field types
2. **Adjust:** Field types as needed:
   - **Text:** `customer_id`, `customer_type`, `region`
   - **Number:** `energy_usage_kwh`, `efficiency_score`, `building_size_sqft`
   - **Date:** `date`, `timestamp`
   - **Boolean:** `is_weekend`, `is_holiday`

3. **Set:** Target variable (e.g., `energy_usage_kwh`)
4. **Configure:** Feature variables
5. **Click:** "Next"

### Step 3: Data Validation
1. **Review:** Data quality report
2. **Check:** Missing values and outliers
3. **Verify:** Data distribution looks correct
4. **Confirm:** Data is ready for analysis

---

## Model Training Process

### Step 1: Select Analysis Type
Choose one of these analysis types:

1. **Predictive Analysis**
   - **Target:** `energy_usage_kwh`
   - **Goal:** Predict future energy consumption
   - **Use Case:** Load forecasting, billing estimates

2. **Classification Analysis**
   - **Target:** `usage_pattern`
   - **Goal:** Classify customers into usage categories
   - **Use Case:** Customer segmentation, targeted marketing

3. **Anomaly Detection**
   - **Target:** `anomaly_score`
   - **Goal:** Identify unusual usage patterns
   - **Use Case:** Fraud detection, equipment failure

### Step 2: Configure Model Parameters
1. **Set:** Training/Test split (80/20 recommended)
2. **Choose:** Algorithm preferences:
   - **Auto:** Let Einstein choose the best algorithm
   - **Specific:** Choose based on your use case
3. **Configure:** Feature engineering options
4. **Set:** Model validation criteria

### Step 3: Start Training
1. **Click:** "Train Model"
2. **Monitor:** Training progress
3. **Wait:** For completion (typically 5-15 minutes)
4. **Review:** Training results and model performance

### Step 4: Model Evaluation
1. **Check:** Model accuracy metrics
2. **Review:** Feature importance rankings
3. **Analyze:** Prediction vs. actual comparisons
4. **Validate:** Model performance on test data

---

## Analysis and Insights

### Step 1: Explore Model Insights
1. **View:** Feature importance chart
2. **Analyze:** Key drivers of your target variable
3. **Review:** Prediction explanations
4. **Explore:** What-if scenarios

### Step 2: Generate Recommendations
1. **Click:** "Recommendations" tab
2. **Review:** AI-generated insights
3. **Customize:** Recommendation thresholds
4. **Export:** Insights for stakeholders

### Step 3: Create Visualizations
1. **Build:** Custom dashboards
2. **Create:** Charts and graphs
3. **Add:** Filters and drill-downs
4. **Share:** With team members

### Step 4: Export Results
1. **Download:** Model performance reports
2. **Export:** Prediction results
3. **Save:** Visualization configurations
4. **Archive:** Model artifacts

---

## Deployment and Integration

### Step 1: Deploy Model
1. **Click:** "Deploy" button
2. **Choose:** Deployment options:
   - **Real-time:** For immediate predictions
   - **Batch:** For scheduled processing
3. **Configure:** API endpoints
4. **Test:** Model deployment

### Step 2: Integrate with Salesforce
1. **Create:** Custom fields for predictions
2. **Set up:** Automated workflows
3. **Configure:** Dashboards and reports
4. **Train:** Users on new features

### Step 3: Monitor Performance
1. **Track:** Model accuracy over time
2. **Monitor:** Prediction drift
3. **Update:** Model as needed
4. **Retrain:** With new data

---

## Best Practices

### Data Quality
- ✅ **Clean Data:** Remove duplicates and outliers
- ✅ **Consistent Format:** Use standardized field values
- ✅ **Sufficient Records:** Minimum 500 records
- ✅ **Balanced Classes:** For classification problems

### Model Selection
- ✅ **Start Simple:** Use auto-selection first
- ✅ **Validate Results:** Always test on unseen data
- ✅ **Monitor Performance:** Track accuracy over time
- ✅ **Regular Updates:** Retrain with new data

### Feature Engineering
- ✅ **Relevant Features:** Choose features that logically influence the target
- ✅ **Avoid Leakage:** Don't include future information
- ✅ **Handle Missing Values:** Use appropriate imputation strategies
- ✅ **Scale Features:** Normalize numerical variables

### Deployment
- ✅ **Test Thoroughly:** Validate before production
- ✅ **Monitor Closely:** Watch for performance degradation
- ✅ **Document Everything:** Keep records of model versions
- ✅ **Plan for Updates:** Schedule regular retraining

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Insufficient Data"
**Solution:**
- Ensure you have at least 500 records
- Check for missing values in target variable
- Verify data quality and consistency

#### Issue: "Poor Model Performance"
**Solution:**
- Review feature selection
- Check for data leakage
- Try different algorithms
- Increase training data

#### Issue: "Upload Errors"
**Solution:**
- Verify CSV format
- Check file size limits
- Ensure proper encoding (UTF-8)
- Validate field names

#### Issue: "Permission Errors"
**Solution:**
- Verify Einstein Discovery permissions
- Check user license
- Contact Salesforce admin

#### Issue: "Slow Training"
**Solution:**
- Reduce feature count
- Use data sampling
- Check system resources
- Consider batch processing

### Getting Help
1. **Salesforce Help:** Search Einstein Discovery documentation
2. **Community:** Post questions in Salesforce Community
3. **Support:** Contact Salesforce Support
4. **Training:** Take Einstein Discovery Trailhead modules

---

## Example Use Cases

### Use Case 1: Energy Consumption Prediction
**Target:** `energy_usage_kwh`
**Features:** `building_size_sqft`, `family_size`, `climate_zone`, `season`
**Application:** Load forecasting, billing estimates

### Use Case 2: Customer Segmentation
**Target:** `usage_pattern`
**Features:** `lifestyle_type`, `income_level`, `building_type`
**Application:** Targeted marketing, personalized recommendations

### Use Case 3: Anomaly Detection
**Target:** `anomaly_score`
**Features:** `energy_usage_kwh`, `hour`, `day_of_week`
**Application:** Fraud detection, equipment monitoring

### Use Case 4: Efficiency Optimization
**Target:** `efficiency_score`
**Features:** `building_type`, `energy_certification`, `appliance_count`
**Application:** Energy efficiency recommendations

---

## Next Steps

1. **Prepare Your Data:** Clean and format your CSV file
2. **Set Up Einstein Discovery:** Configure permissions and access
3. **Upload Data:** Import your energy usage dataset
4. **Train Model:** Choose target and features, start training
5. **Analyze Results:** Review insights and recommendations
6. **Deploy Model:** Integrate with your Salesforce org
7. **Monitor Performance:** Track accuracy and update as needed

---

## Resources

- [Einstein Discovery Documentation](https://help.salesforce.com/s/articleView?id=sf.einstein_discovery_overview.htm)
- [Einstein Discovery Trailhead](https://trailhead.salesforce.com/content/learn/trails/einstein-discovery)
- [Salesforce Community](https://success.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000LQoGSAW)
- [Einstein Discovery API](https://developer.salesforce.com/docs/atlas.en-us.einstein_discovery_api.meta/einstein_discovery_api/)

---

*This guide is based on your generated energy usage dataset with 1,000 records. Adjust the steps based on your specific use case and data requirements.* 
