# Community Resources Directory
# A program to track local community resources

# 1. Create your list of community resources (each as a dictionary)
resources = [
    {"name": "ULEM", "service": "Job Training", "address": "88 Warren St, Boston", "contact": "617-442-4519"},
    {"name": "Greater Boston Food Bank", "service": "Food Bank", "address": "70 South Bay Ave, Boston", "contact": "617-427-5200"},
    {"name": "Roxbury Community Health Center", "service": "Healthcare", "address": "435 Warren St, Roxbury", "contact": "617-442-7400"}
]

# 2. Print all resources
print("ALL COMMUNITY RESOURCES:")
for stuff in resources:
    print("Organization:", stuff["name"])
    print("Service:", stuff["service"])
    print("Address:", stuff["address"])
    print("Contact:", stuff["contact"])
    print()

# 3. Print resources of a specific type
service_type = "Food Bank"  # Try different types
print("\nRESOURCES OFFERING " + service_type + ":")
for stuff in resources:
    if stuff["service"] == service_type:
        print("Organization:", stuff["name"])
        print("Service:", stuff["service"])
        print("Address:", stuff["address"])
        print("Contact:", stuff["contact"])
        print()

# 4. Find and print contact info for a specific organization
org_name = "ULEM"  # Try different organization names
print("\nCONTACT INFO FOR " + org_name + ":")
for stuff in resources:
    if stuff["name"] == org_name:
        print("Organization:", stuff["name"])
        print("Contact:", stuff["contact"])