def menu_items(request):
    return {
        "menu_items": [
            {"label": "Customers", "url": "customer", "icon": "bi-people","namespace":"Customer"},
            {"label": "Employees", "url": "employee", "icon": "bi-person-badge","namespace":"Employee"},
            {"label": "Project", "url": "project", "icon": "bi-folder","namespace":"Project"},
            {"label": "Versions", "url": "version", "icon": "bi-code-slash","namespace":"Version"},{"label": "Locations", "url": "location", "icon": "bi-geo-alt","namespace":"Location"},
            {"label": "Roles", "url": "role", "icon": "bi-briefcase","namespace":"Role"},
            {"label": "ContactUs", "url": "contact-us", "icon": "bi-envelope","namespace":"ContactUs"},
            {"label": "Coordination & Execution Escalation", "url": "coordination-and-execution-escalation", "icon": "bi-gear","namespace":"Coordination_and_Execution_Escalation"},
            {"label": "Changedetails", "url": "Changedetails", "icon": "bi-tools","namespace":"changedetails"},
            #{"label": "Remedy2Hippo", "url": "Remedy2Hippo", "icon": "bi-tools","namespace":"Remedy2Hippo"},
            {"label": "Task information", "url": "task-information", "icon": "bi-tools","namespace":"task_information"},
            {"label": "Access Control", "icon": "bi-person-lock", "namespace":["AccessControl_Role","AccessControl_Employee"],"children":[
                {"label": "Role", "url": "access-control-role", "icon": "bi-shield-lock","namespace":"AccessControl_Role"},
                {"label": "Employee", "url": "access-control-employee", "icon": "bi-person-lock","namespace":"AccessControl_Employee"},]
            },
            {"label": "Uploader", "icon": "bi-person-lock", "namespace":["clients","crq_client_approval","crq_additional_tasks","crq_coordination","crq_properties","server_details","aip_data","dc_region","timezone_table","uploader_projects","uploader_variants"],"children":[
                {"label": "Clients", "url": "clients", "icon": "bi-shield-lock","namespace":"clients"},
                {"label": "CRQ Client Approval", "url": "crq-client-approval", "icon": "bi-shield-lock","namespace":"crq_client_approval"},
                {"label": "CRQ Additional tasks", "url": "crq-additional-tasks", "icon": "bi-shield-lock","namespace":"crq_additional_tasks"},
                {"label": "CRQ Coordination", "url": "crq-coordination", "icon": "bi-shield-lock","namespace":"crq_coordination"},
                {"label": "CRQ Properties", "url": "crq-properties", "icon": "bi-shield-lock","namespace":"crq_properties"},
                {"label": "Server Details", "url": "server-details", "icon": "bi-shield-lock","namespace":"server_details"},
                {"label": "AIP Data", "url": "aip-data", "icon": "bi-shield-lock","namespace":"aip_data"},
                {"label": "DC Region", "url": "dc-region", "icon": "bi-shield-lock","namespace":"dc_region"},
                {"label": "Timezone Table", "url": "timezone-table", "icon": "bi-shield-lock","namespace":"timezone_table"},
                {"label": "Projects", "url": "uploader-projects", "icon": "bi-shield-lock","namespace":"uploader_projects"},
                {"label": "Variants", "url": "uploader-variants", "icon": "bi-shield-lock","namespace":"uploader_variants"},
                ]
            }
            
        ]
    }