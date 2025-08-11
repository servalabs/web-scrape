import json
import csv

def json_to_csv(input_file, output_file):
    # Read JSON file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            projects = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    # Define CSV headers
    headers = ['name', 'image_url', 'video_url', 'funding_amount', 'funding_percent', 'days_left', 'end_date']
    
    # Write to CSV
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            
            processed_count = 0
            for project in projects:
                writer.writerow(project)
                processed_count += 1
                if processed_count % 1000 == 0:
                    print(f"Processed {processed_count} projects")
            
        print(f"Total projects converted: {processed_count}")
        print(f"Saved to {output_file}")
    except Exception as e:
        print(f"Error writing CSV: {e}")

if __name__ == '__main__':
    input_file = 'C:\\Users\\Admin\\Desktop\\New folder\\filtered_kickstarter_projects.json'  # Replace with your JSON file path
    output_file = 'kickstarter_projects.csv'
    json_to_csv(input_file, output_file)
