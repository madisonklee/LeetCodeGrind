import json

# Sample JSON data
json_data = '''
[
    {"Response": "Yes", "Additional Context": "The risk governance program includes risk management policies, procedures, and internal controls."},
    {"Response": "Yes", "Additional Context": "The risk governance program includes a range of assets to include: people, processes, data, and technology."},
    {"Response": "Yes", "Additional Context": "Fourth parties have access to scoped systems and data or processing facilities through a third party risk management program."},
    {"Response": "Yes", "Additional Context": "There is a third party risk management program that is reviewed and approved by management."},
    {"Response": "Yes", "Additional Context": "An information security program has been documented, approved by management, published, and communicated to constituents."},
    {"Response": "Yes", "Additional Context": "The information security program establishes requirements for the protection of information that is accessed, processed, stored, or transmitted on external systems."},
    {"Response": "Yes", "Additional Context": "Chain of custody logs identifying media contents, protection applied, times of transfer and receipt at destination are used when transporting scoped data."},
    {"Response": "Yes", "Additional Context": "Data Loss Prevention (DLP) security solutions are implemented."},
    {"Response": "Yes", "Additional Context": "Human Resource policies and/or procedures are approved by management, communicated to constituents, and have an owner to maintain, and review."},
    {"Response": "Yes", "Additional Context": "Background checks are performed at time of hire."},
    {"Response": "Yes", "Additional Context": "A physical security program is approved by management, communicated to constituents, and has an owner assigned to maintain and review."},
    {"Response": "Yes", "Additional Context": "The physical security program includes a clean desk policy."},
    {"Response": "Yes", "Additional Context": "Executive leadership ensures IT Operations' policies and procedures are established and aligned with organizational strategy, and communicated to the entire organization."},
    {"Response": "Yes", "Additional Context": "The organization has a formalized Information Technology organizational structure that defines IT governance and management responsibilities."},
    {"Response": "Yes", "Additional Context": "Password policy requires initial and temporary passwords to be changed upon next login."},
    {"Response": "Yes", "Additional Context": "Password reset authority is restricted to authorized persons and/or an automated password reset tool."}
]
'''

# Parse the JSON data
data = json.loads(json_data)

# Extract and print the "Additional Context" fields as an unnumbered list
for item in data:
    print(f"- {item['Additional Context']}")
