import json
import csv
from datetime import datetime

def filter_kickstarter_data(input_file, json_output_file, csv_output_file):
    projects = []
    successful_count = 0
    total_processed = 0
    current_date = datetime.now()

    print("Applying filters: Technology (parent_id=16), Successful (state='successful' or percent_funded>=100)")

    # Read JSONL file line by line
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    # Skip empty or whitespace lines
                    if not line.strip():
                        continue

                    # Parse JSON
                    project_data = json.loads(line.strip())
                    
                    # Handle nested 'data' field
                    if not project_data or 'data' not in project_data:
                        print(f"Skipping invalid entry: no 'data' field")
                        continue
                    project = project_data.get('data')
                    if not project:
                        print(f"Skipping invalid entry: 'data' is None")
                        continue

                    # Filter: Technology (parent_id=16) and successful (state="successful" or percent_funded>=100)
                    category = project.get('category', {})
                    parent_id = category.get('parent_id')
                    state = project.get('state')
                    percent_funded = project.get('percent_funded', 0)

                    total_processed += 1
                    if parent_id != 16 or (state != 'successful' and percent_funded < 100):
                        continue

                    # Successful Technology project found
                    successful_count += 1

                    # Extract fields
                    name = project.get('name', 'Unknown')
                    img_url = project.get('photo', {}).get('ed', '')
                    video_url = project.get('video', {}).get('base', 'Expired') if project.get('video') else 'Expired'
                    funding = project.get('converted_pledged_amount', 'Unknown')
                    funding_percent = project.get('percent_funded', 'Unknown')
                    deadline = project.get('deadline', None)

                    # Calculate days left
                    days_left = 'Expired'
                    end_date_str = 'Unknown'
                    if deadline:
                        end_date = datetime.fromtimestamp(deadline)
                        end_date_str = end_date.strftime('%Y-%m-%d')
                        if state == 'live':
                            days_left = (end_date - current_date).days
                            if days_left < 0:
                                days_left = 'Expired'

                    projects.append({
                        'name': name,
                        'image_url': img_url,
                        'video_url': video_url,
                        'funding_amount': f"${funding:,}" if isinstance(funding, (int, float)) else funding,
                        'funding_percent': f"{funding_percent:.2f}%" if isinstance(funding_percent, (int, float)) else funding_percent,
                        'days_left': days_left,
                        'end_date': end_date_str
                    })

                    # Print progress every 1000 projects
                    if total_processed % 1000 == 0:
                        print(f"Processed {total_processed} projects, {successful_count} successful Technology projects found")

                except json.JSONDecodeError as e:
                    print(f"Skipping invalid JSON line: {e}")
                    continue
                except Exception as e:
                    print(f"Error processing project: {e}")
                    continue

    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Print final count
    print(f"Total projects processed: {total_processed}")
    print(f"Total successful Technology projects: {successful_count}")
    if successful_count < 14000:
        print(f"Warning: Found only {successful_count} successful Technology projects, expected ~14000. Check dataset for 'parent_id': 16.")

    # Save filtered projects to JSON
    try:
        with open(json_output_file, 'w', encoding='utf-8') as f:
            json.dump(projects, f, indent=2)
        print(f"Saved {len(projects)} projects to {json_output_file}")
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return

    # Convert to CSV
    try:
        with open(csv_output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'image_url', 'video_url', 'funding_amount', 'funding_percent', 'days_left', 'end_date'])
            writer.writeheader()
            
            processed_count = 0
            for project in projects:
                writer.writerow(project)
                processed_count += 1
                if processed_count % 1000 == 0:
                    print(f"Converted {processed_count} projects to CSV")
            
        print(f"Total projects converted to CSV: {processed_count}")
        print(f"Saved to {csv_output_file}")
    except Exception as e:
        print(f"Error writing CSV: {e}")

if __name__ == '__main__':
    input_file = 'kickstarter_dataset.json'  # Replace with your dataset file path
    json_output_file = 'filtered_kickstarter_projects.json'
    csv_output_file = 'kickstarter_projects_FINAL.csv'
    filter_kickstarter_data(input_file, json_output_file, csv_output_file)
