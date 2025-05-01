# Distributor Onboarding & Payment Backend

A Django REST API service for managing distributor onboarding and payment confirmation. Built for Fenice Energy's backend system design assessment.

---

##  Features

- Create, update, and retrieve distributor profiles
- Record and confirm payments with status tracking
- Secure API access using JWT authentication
- Integration with:
  - SAP (to sync distributor data)
  - Cashfree (webhook to confirm payments)

---

##  Tech Stack

- Django
- Django REST Framework
- JWT Authentication (`djangorestframework-simplejwt`)

---

## Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/distributor-backend.git
cd distributor-backend
