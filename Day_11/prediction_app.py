#!/usr/bin/env python3
"""
Student Score Predictor App - Day 11 Task
AI & ML Internship - Codomax Digital Solutions

This application predicts an examination score based on the daily study hours entered by the user.
It uses a Linear Regression model trained on student study performance data.
"""

import sys

# Default coefficients trained on the complete dataset
DEFAULT_SLOPE = 9.775803
DEFAULT_INTERCEPT = 2.483673

def get_trained_parameters():
    """
    Attempts to train the model dynamically from the dataset using standard python.
    Falls back to pre-calculated OLS coefficients if the dataset is not found.
    """
    try:
        import csv
        hours = []
        scores = []
        # Try relative path or relative parent path
        try:
            filepath = "student_scores.csv"
            with open(filepath, mode='r') as f:
                pass
        except FileNotFoundError:
            filepath = "../student_scores.csv"
            
        with open(filepath, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                hours.append(float(row['Hours_Studied']))
                scores.append(float(row['Scores']))
        
        n = len(hours)
        if n == 0:
            return DEFAULT_SLOPE, DEFAULT_INTERCEPT
            
        mean_x = sum(hours) / n
        mean_y = sum(scores) / n
        
        num = sum((x - mean_x) * (y - mean_y) for x, y in zip(hours, scores))
        den = sum((x - mean_x) ** 2 for x in hours)
        
        if den == 0:
            return DEFAULT_SLOPE, DEFAULT_INTERCEPT
            
        slope = num / den
        intercept = mean_y - slope * mean_x
        return slope, intercept
    except Exception:
        # Fallback to pre-calculated parameters
        return DEFAULT_SLOPE, DEFAULT_INTERCEPT

def predict_score(hours, slope, intercept):
    """
    Applies the linear equation y = mx + c and caps the output between 0 and 100.
    """
    raw_prediction = (slope * hours) + intercept
    capped_score = max(0.0, min(100.0, raw_prediction))
    return raw_prediction, capped_score

def main():
    print("==================================================")
    print("      STUDENT SCORE PREDICTOR APP - Day 11        ")
    print("          AI & ML Internship - Codomax            ")
    print("==================================================")
    print("Loading predictive model parameters...")
    
    slope, intercept = get_trained_parameters()
    print("✅ Model is loaded and ready.")
    print(f"Formula: Score = {slope:.4f} * Hours_Studied + {intercept:.4f}\n")
    
    while True:
        try:
            user_input = input("Enter study hours per day (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print("Thank you for using the Student Score Predictor! Goodbye.")
                break
                
            if not user_input:
                continue
                
            hours = float(user_input)
            if hours < 0:
                print("❌ Error: Study hours cannot be negative. Try again.")
                print("--------------------------------------------------")
                continue
            elif hours > 24:
                print("⚠️ Warning: A day only has 24 hours! Setting hours to 24.")
                hours = 24.0
                
            raw_pred, final_score = predict_score(hours, slope, intercept)
            
            print("\n--- Prediction Output ---")
            print(f"Daily Study Hours : {hours:.2f} hrs")
            print(f"Predicted Score   : {final_score:.2f}%")
            print("-------------------------")
            
            # Grade feedback
            if final_score >= 90:
                print("Grade: A+ (Excellent performance expected!)")
            elif final_score >= 75:
                print("Grade: A (Very good, keep up the focus.)")
            elif final_score >= 50:
                print("Grade: B (Pass, good job.)")
            else:
                print("Grade: F/D (Focus on increasing daily study hours!)")
            print("==================================================\n")
            
        except ValueError:
            print("❌ Error: Please enter a valid decimal number.")
            print("--------------------------------------------------")

if __name__ == "__main__":
    main()
