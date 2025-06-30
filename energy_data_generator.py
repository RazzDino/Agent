import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_energy_data():
    """Generate 500 energy usage test records"""
    
    data = []
    customers = [f"CUST{i:03d}" for i in range(1, 101)]
    
    for i in range(500):
        # Basic customer info
        customer_id = random.choice(customers)
        date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 90), hours=random.randint(0, 23))
        
        # Home characteristics
        home_size = random.choice([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
        occupants = random.choice([1, 2, 3, 4, 5, 6])
        income_level = random.choice(['Low', 'Medium', 'High'])
        climate_zone = random.choice(['Zone_1', 'Zone_2', 'Zone_3', 'Zone_4', 'Zone_5'])
        
        # Energy system characteristics
        smart_meter_installed = random.choices([0, 1], weights=[0.3, 0.7])[0]
        heating_type = random.choice(['Natural_Gas', 'Electric', 'Propane', 'Oil'])
        cooling_type = random.choice(['Central_AC', 'Heat_Pump', 'Window_AC', 'Mini_Split'])
        roof_insulation = random.choice(['Poor', 'Fair', 'Good', 'Excellent'])
        window_efficiency = random.choice(['Single_Pane', 'Double_Pane', 'Triple_Pane'])
        
        # Calculate energy usage based on characteristics
        base_usage = home_size * 0.005 * occupants
        
        # Apply multipliers
        climate_mult = {'Zone_1': 1.2, 'Zone_2': 1.1, 'Zone_3': 1.0, 'Zone_4': 1.3, 'Zone_5': 1.4}[climate_zone]
        hour_mult = 1.3 if 6 <= date.hour <= 9 or 17 <= date.hour <= 21 else 0.7 if 22 <= date.hour <= 5 else 1.0
        weekend_mult = 1.1 if date.weekday() >= 5 else 1.0
        smart_mult = 0.95 if smart_meter_installed else 1.0
        
        energy_usage = base_usage * climate_mult * hour_mult * weekend_mult * smart_mult * random.uniform(0.8, 1.2)
        
        # Calculate peak vs off-peak
        if 6 <= date.hour <= 9 or 17 <= date.hour <= 21:
            peak_ratio = random.uniform(0.7, 0.9)
        else:
            peak_ratio = random.uniform(0.3, 0.5)
        
        peak_hours = energy_usage * peak_ratio
        off_peak_hours = energy_usage - peak_hours
        
        # Determine usage pattern
        usage_per_person = energy_usage / occupants
        if usage_per_person > 8:
            usage_pattern = 'Peak_Usage'
        elif usage_per_person > 5:
            usage_pattern = 'High_Usage'
        elif usage_per_person > 3:
            usage_pattern = 'Regular'
        else:
            usage_pattern = 'Low_Usage'
        
        # Calculate efficiency rating
        insulation_bonus = {'Poor': 0, 'Fair': 5, 'Good': 10, 'Excellent': 15}[roof_insulation]
        window_bonus = {'Single_Pane': 0, 'Double_Pane': 5, 'Triple_Pane': 10}[window_efficiency]
        smart_bonus = 5 if smart_meter_installed else 0
        
        efficiency_rating = max(0, min(100, 50 + (20 - usage_per_person) + insulation_bonus + window_bonus + smart_bonus))
        
        data.append({
            'customer_id': customer_id,
            'date': date.strftime('%Y-%m-%d'),
            'time': date.strftime('%H:%M:%S'),
            'hour': date.hour,
            'day_of_week': date.strftime('%A'),
            'month': date.month,
            'season': ['Winter', 'Spring', 'Summer', 'Fall'][(date.month % 12 + 3) // 3 - 1],
            'energy_usage_kwh': round(energy_usage, 1),
            'peak_hours': round(peak_hours, 1),
            'off_peak_hours': round(off_peak_hours, 1),
            'weekend_usage': 1 if date.weekday() >= 5 else 0,
            'holiday_usage': 0,  # Simplified
            'smart_meter_installed': smart_meter_installed,
            'home_size_sqft': home_size,
            'occupants': occupants,
            'income_level': income_level,
            'climate_zone': climate_zone,
            'appliance_count': int(home_size / 100) + random.randint(-2, 3),
            'heating_type': heating_type,
            'cooling_type': cooling_type,
            'roof_insulation': roof_insulation,
            'window_efficiency': window_efficiency,
            'usage_pattern': usage_pattern,
            'anomaly_score': round(random.uniform(0, 0.5), 2),
            'energy_efficiency_rating': round(efficiency_rating, 0)
        })
    
    return pd.DataFrame(data)

# Generate and save data
print("Generating 500 energy usage test records...")
df = generate_energy_data()
df.to_csv('energy_usage_test_data_500.csv', index=False)

print(f"Generated {len(df)} records")
print("Data saved to: energy_usage_test_data_500.csv")

print("\nData Summary:")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print(f"Unique customers: {df['customer_id'].nunique()}")
print(f"Average energy usage: {df['energy_usage_kwh'].mean():.1f} kWh")
print(f"Usage range: {df['energy_usage_kwh'].min():.1f} - {df['energy_usage_kwh'].max():.1f} kWh")
print(f"Smart meter adoption: {df['smart_meter_installed'].mean()*100:.1f}%")
print(f"Average efficiency rating: {df['energy_efficiency_rating'].mean():.1f}")

print("\nUsage Pattern Distribution:")
pattern_counts = df['usage_pattern'].value_counts()
for pattern, count in pattern_counts.items():
    print(f"  {pattern}: {count} ({count/len(df)*100:.1f}%)") 