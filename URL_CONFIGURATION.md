# Django URL Configuration Summary

## URL Patterns in Main.urls

This document provides a complete overview of all URL patterns configured in the Django application.

### Main URL Patterns

| URL Pattern | View Function | Name | Description |
|------------|---------------|------|-------------|
| `/` | home | home | Home page |
| `/home/` | home | home | Home page (alternative) |
| `/about/` | about | about | About page |
| `/organisation/` | employee | employee | Organization/Employee listing |
| `/projects/` | project | project | Project listing |
| `/project-version/<int:i>/` | project_version | project_version | Project version details (55, 76, 108, PS) |
| `/escalation/` | escalation | escalation | Coordination and Execution Escalation |
| `/customers/` | customer | customer | Customer listing |
| `/Geo/` | location | location | Geographic locations |
| `/roles/` | role | role | Role listing |
| `/contact/` | contact_us | contact_us | Contact page |
| `/login/` | login | login | User login |
| `/forgot-password/` | forgot_password | forgot_password | Password recovery |
| `/reset-password/<str:token>/` | reset_password | reset_password | Password reset with token |
| `/logout/` | logout | logout | User logout |
| `/admin/` | admin.site.urls | - | Django admin interface |

### Included URL Patterns (Sub-applications)

| Base URL | Included Module | Description |
|----------|----------------|-------------|
| `/employee/` | Employee.urls | Employee management |
| `/role/` | Role.urls | Role management |
| `/location/` | Location.urls | Location management |
| `/customer/` | Customer.urls | Customer management |
| `/project/` | Project.urls | Project management |
| `/version/` | Version.urls | Version management |
| `/coordination-and-execution-escalation/` | Coordination_and_Execution_Escalation.urls | Escalation management |
| `/contact-us/` | ContactUs.urls | Contact form handling |
| `/access-control-role/` | AccessControl_Role.urls | Role access control |
| `/access-control-employee/` | AccessControl_Employee.urls | Employee access control |

### Error Handlers

- **404 Not Found**: Custom handler at `FrontEnd.views.Error404View`
  - Template: `templates/FrontEnd/404.html`

### Valid Project Version IDs

The `project-version/<int:i>/` endpoint accepts the following version IDs:
- 55
- 76
- 108
- PS (as string)

Any other version ID will redirect to `project_not_found.html`.

## Testing URLs

To test the URL configuration, you can use Django's `show_urls` command or access the following URLs in your browser:

```bash
# Home pages
http://localhost:8000/
http://localhost:8000/home/

# Info pages
http://localhost:8000/about/
http://localhost:8000/contact/

# Management pages
http://localhost:8000/organisation/
http://localhost:8000/projects/
http://localhost:8000/customers/
http://localhost:8000/Geo/
http://localhost:8000/roles/
http://localhost:8000/escalation/

# Authentication
http://localhost:8000/login/
http://localhost:8000/logout/
http://localhost:8000/forgot-password/

# Admin
http://localhost:8000/admin/

# Test 404 error
http://localhost:8000/nonexistent-page/
```

## Troubleshooting

### Common Issues

1. **"Page not found" errors**: 
   - Check that the URL exactly matches one of the patterns above
   - Ensure trailing slashes match the pattern definition
   - Verify that all required URL parameters are provided

2. **Template not found errors**:
   - All FrontEnd templates should be in `templates/FrontEnd/` directory
   - Check that template names match exactly in the view functions

3. **URL pattern order**:
   - Django tries URL patterns in the order they're defined
   - More specific patterns should come before more general ones
   - The current order is optimized for the application structure

## Running the Development Server

```powershell
python manage.py runserver
```

Then access the application at `http://localhost:8000/`
