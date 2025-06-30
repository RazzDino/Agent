#!/usr/bin/env python3
"""
Energy Usage Test Data Generator
Creates 500 realistic test records for energy usage analysis and Einstein Discovery training
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_energy_usage_data(num_records=500):
    """Generate comprehensive energy usage test data"""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Base parameters
    customers = [f"CUST{i:03d}" for i in range(1, 101)]  # 100 unique customers
    dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='H')
    
    # Climate zones and their characteristics
    climate_zones = {
        'Zone_1': {'temp_range': (-10, 35), 'humidity': 'Low'},
        'Zone_2': {'temp_range': (-5, 40), 'humidity': 'Low'},
        'Zone_3': {'temp_range': (0, 45), 'humidity': 'Medium'},
        'Zone_4': {'temp_range': (5, 50), 'humidity': 'Medium'},
        'Zone_5': {'temp_range': (10, 55), 'humidity': 'High'}
    }
    
    # Home characteristics
    home_sizes = [1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000]
    occupant_counts = [1, 2, 3, 4, 5, 6]
    income_levels = ['Low', 'Medium', 'High']
    heating_types = ['Natural_Gas', 'Electric', 'Propane', 'Oil']
    cooling_types = ['Central_AC', 'Heat_Pump', 'Window_AC', 'Mini_Split']
    insulation_levels = ['Poor', 'Fair', 'Good', 'Excellent']
    window_types = ['Single_Pane', 'Double_Pane', 'Triple_Pane']
    
    data = []
    
    for i in range(num_records):
        # Random customer and date
        customer_id = random.choice(customers)
        date_time = random.choice(dates)
        
        # Extract time components
        hour = date_time.hour
        day_of_week = date_time.strftime('%A')
        month = date_time.month
        season = get_season(month)
        
        # Determine if weekend or holiday
        weekend_usage = 1 if day_of_week in ['Saturday', 'Sunday'] else 0
        holiday_usage = 1 if is_holiday(date_time) else 0
        
        # Smart meter installation (70% have smart meters)
        smart_meter_installed = random.choices([0, 1], weights=[0.3, 0.7])[0]
        
        # Home characteristics
        home_size = random.choice(home_sizes)
        occupants = random.choice(occupant_counts)
        income_level = random.choice(income_levels)
        climate_zone = random.choice(list(climate_zones.keys()))
        appliance_count = int(home_size / 100) + random.randint(-2, 3)
        appliance_count = max(8, min(30, appliance_count))  # Keep within reasonable range
        
        heating_type = random.choice(heating_types)
        cooling_type = random.choice(cooling_types)
        roof_insulation = random.choice(insulation_levels)
        window_efficiency = random.choice(window_types)
        
        # Calculate base energy usage based on characteristics
        base_usage = calculate_base_usage(home_size, occupants, climate_zone, 
                                        heating_type, cooling_type, roof_insulation, 
                                        window_efficiency, hour, season, weekend_usage)
        
        # Add randomness and patterns
        energy_usage = add_usage_patterns(base_usage, hour, day_of_week, season, 
                                        weekend_usage, holiday_usage, smart_meter_installed)
        
        # Calculate peak vs off-peak usage
        peak_hours, off_peak_hours = calculate_peak_usage(energy_usage, hour)
        
        # Determine usage pattern
        usage_pattern = determine_usage_pattern(energy_usage, hour, home_size, occupants)
        
        # Calculate anomaly score
        anomaly_score = calculate_anomaly_score(energy_usage, home_size, occupants, 
                                              climate_zone, hour, season)
        
        # Calculate energy efficiency rating
        efficiency_rating = calculate_efficiency_rating(home_size, energy_usage, 
                                                      roof_insulation, window_efficiency, 
                                                      smart_meter_installed, occupants)
        
        data.append({
            'customer_id': customer_id,
            'date': date_time.strftime('%Y-%m-%d'),
            'time': date_time.strftime('%H:%M:%S'),
            'hour': hour,
            'day_of_week': day_of_week,
            'month': month,
            'season': season,
            'energy_usage_kwh': round(energy_usage, 1),
            'peak_hours': round(peak_hours, 1),
            'off_peak_hours': round(off_peak_hours, 1),
            'weekend_usage': weekend_usage,
            'holiday_usage': holiday_usage,
            'smart_meter_installed': smart_meter_installed,
            'home_size_sqft': home_size,
            'occupants': occupants,
            'income_level': income_level,
            'climate_zone': climate_zone,
            'appliance_count': appliance_count,
            'heating_type': heating_type,
            'cooling_type': cooling_type,
            'roof_insulation': roof_insulation,
            'window_efficiency': window_efficiency,
            'usage_pattern': usage_pattern,
            'anomaly_score': round(anomaly_score, 2),
            'energy_efficiency_rating': round(efficiency_rating, 0)
        })
    
    return pd.DataFrame(data)

def get_season(month):
    """Determine season based on month"""
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

def is_holiday(date):
    """Check if date is a holiday (simplified)"""
    holidays = ['2024-01-01', '2024-01-15', '2024-02-19', '2024-05-27', '2024-07-04']
    return date.strftime('%Y-%m-%d') in holidays

def calculate_base_usage(home_size, occupants, climate_zone, heating_type, 
                        cooling_type, roof_insulation, window_efficiency, 
                        hour, season, weekend_usage):
    """Calculate base energy usage based on home characteristics"""
    
    # Base usage per square foot
    base_per_sqft = 0.005
    
    # Occupant multiplier
    occupant_multiplier = 1 + (occupants - 2) * 0.2
    
    # Climate zone multiplier
    climate_multipliers = {'Zone_1': 1.2, 'Zone_2': 1.1, 'Zone_3': 1.0, 
                          'Zone_4': 1.3, 'Zone_5': 1.4}
    climate_mult = climate_multipliers.get(climate_zone, 1.0)
    
    # Heating/cooling efficiency
    heating_efficiency = {'Natural_Gas': 0.8, 'Electric': 1.0, 'Propane': 0.9, 'Oil': 0.85}
    cooling_efficiency = {'Central_AC': 1.0, 'Heat_Pump': 0.7, 'Window_AC': 1.2, 'Mini_Split': 0.8}
    
    heating_mult = heating_efficiency.get(heating_type, 1.0)
    cooling_mult = cooling_efficiency.get(cooling_type, 1.0)
    
    # Insulation efficiency
    insulation_multipliers = {'Poor': 1.4, 'Fair': 1.2, 'Good': 1.0, 'Excellent': 0.8}
    insulation_mult = insulation_multipliers.get(roof_insulation, 1.0)
    
    # Window efficiency
    window_multipliers = {'Single_Pane': 1.3, 'Double_Pane': 1.0, 'Triple_Pane': 0.8}
    window_mult = window_multipliers.get(window_efficiency, 1.0)
    
    # Hour of day multiplier
    if 6 <= hour <= 9 or 17 <= hour <= 21:
        hour_mult = 1.3  # Peak hours
    elif 22 <= hour <= 5:
        hour_mult = 0.7  # Off-peak hours
    else:
        hour_mult = 1.0  # Regular hours
    
    # Season multiplier
    season_multipliers = {'Winter': 1.4, 'Spring': 0.9, 'Summer': 1.3, 'Fall': 0.8}
    season_mult = season_multipliers.get(season, 1.0)
    
    # Weekend multiplier
    weekend_mult = 1.1 if weekend_usage else 1.0
    
    # Calculate base usage
    base_usage = (home_size * base_per_sqft * occupant_multiplier * climate_mult * 
                  heating_mult * cooling_mult * insulation_mult * window_mult * 
                  hour_mult * season_mult * weekend_mult)
    
    return base_usage

def add_usage_patterns(base_usage, hour, day_of_week, season, weekend_usage, 
                      holiday_usage, smart_meter_installed):
    """Add realistic usage patterns and variations"""
    
    # Random variation (±20%)
    variation = random.uniform(0.8, 1.2)
    
    # Smart meter efficiency (5% reduction)
    smart_meter_mult = 0.95 if smart_meter_installed else 1.0
    
    # Holiday usage increase
    holiday_mult = 1.2 if holiday_usage else 1.0
    
    # Day of week patterns
    day_multipliers = {
        'Monday': 1.1, 'Tuesday': 1.0, 'Wednesday': 1.0, 'Thursday': 1.0,
        'Friday': 1.1, 'Saturday': 1.2, 'Sunday': 1.1
    }
    day_mult = day_multipliers.get(day_of_week, 1.0)
    
    final_usage = base_usage * variation * smart_meter_mult * holiday_mult * day_mult
    
    return max(0.1, final_usage)  # Ensure minimum usage

def calculate_peak_usage(total_usage, hour):
    """Calculate peak vs off-peak usage distribution"""
    if 6 <= hour <= 9 or 17 <= hour <= 21:
        peak_ratio = random.uniform(0.7, 0.9)
    else:
        peak_ratio = random.uniform(0.3, 0.5)
    
    peak_hours = total_usage * peak_ratio
    off_peak_hours = total_usage - peak_hours
    
    return peak_hours, off_peak_hours

def determine_usage_pattern(energy_usage, hour, home_size, occupants):
    """Determine usage pattern category"""
    # Calculate usage per occupant per hour
    usage_per_person = energy_usage / occupants
    
    if usage_per_person > 8:
        return 'Peak_Usage'
    elif usage_per_person > 5:
        return 'High_Usage'
    elif usage_per_person > 3:
        return 'Regular'
    else:
        return 'Low_Usage'

def calculate_anomaly_score(energy_usage, home_size, occupants, climate_zone, hour, season):
    """Calculate anomaly score based on expected vs actual usage"""
    
    # Expected usage based on home characteristics
    expected_usage = home_size * 0.005 * occupants
    
    # Adjust for climate and season
    climate_adjustments = {'Zone_1': 1.2, 'Zone_2': 1.1, 'Zone_3': 1.0, 'Zone_4': 1.3, 'Zone_5': 1.4}
    season_adjustments = {'Winter': 1.4, 'Spring': 0.9, 'Summer': 1.3, 'Fall': 0.8}
    
    expected_usage *= climate_adjustments.get(climate_zone, 1.0)
    expected_usage *= season_adjustments.get(season, 1.0)
    
    # Calculate deviation
    deviation = abs(energy_usage - expected_usage) / expected_usage
    
    # Normalize to 0-1 scale
    anomaly_score = min(1.0, deviation)
    
    return anomaly_score

def calculate_efficiency_rating(home_size, energy_usage, roof_insulation, 
                              window_efficiency, smart_meter_installed, occupants):
    """Calculate energy efficiency rating (0-100)"""
    
    # Base efficiency score
    base_score = 50
    
    # Size efficiency (smaller homes are more efficient per person)
    size_efficiency = max(0, 20 - (home_size / 100 - 15))
    
    # Usage efficiency (lower usage per person is better)
    usage_per_person = energy_usage / occupants
    usage_efficiency = max(0, 20 - usage_per_person)
    
    # Insulation bonus
    insulation_bonus = {'Poor': 0, 'Fair': 5, 'Good': 10, 'Excellent': 15}
    insulation_score = insulation_bonus.get(roof_insulation, 0)
    
    # Window bonus
    window_bonus = {'Single_Pane': 0, 'Double_Pane': 5, 'Triple_Pane': 10}
    window_score = window_bonus.get(window_efficiency, 0)
    
    # Smart meter bonus
    smart_meter_bonus = 5 if smart_meter_installed else 0
    
    total_score = base_score + size_efficiency + usage_efficiency + insulation_score + window_score + smart_meter_bonus
    
    return min(100, max(0, total_score))

def main():
    """Generate and save the test data"""
    print("Generating 500 energy usage test records...")
    
    # Generate data
    df = generate_energy_usage_data(500)
    
    # Save to CSV
    df.to_csv('energy_usage_test_data_500.csv', index=False)
    
    print(f"Generated {len(df)} records")
    print("Data saved to: energy_usage_test_data_500.csv")
    
    # Print summary statistics
    print("\nData Summary:")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Unique customers: {df['customer_id'].nunique()}")
    print(f"Average energy usage: {df['energy_usage_kwh'].mean():.1f} kWh")
    print(f"Usage range: {df['energy_usage_kwh'].min():.1f} - {df['energy_usage_kwh'].max():.1f} kWh")
    print(f"Smart meter adoption: {df['smart_meter_installed'].mean()*100:.1f}%")
    print(f"Average efficiency rating: {df['energy_efficiency_rating'].mean():.1f}")
    
    # Usage pattern distribution
    print("\nUsage Pattern Distribution:")
    pattern_counts = df['usage_pattern'].value_counts()
    for pattern, count in pattern_counts.items():
        print(f"  {pattern}: {count} ({count/len(df)*100:.1f}%)")

if __name__ == "__main__":
    main() 