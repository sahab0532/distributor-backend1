import requests

def sync_distributor_to_sap(distributor):
    url = "https://sap.example.com/api/distributors/"
    payload = {
        "name": distributor.name,
        "gst_number": distributor.gst_number,
        "pan_number": distributor.pan_number,
        "bank_account": distributor.bank_account,
        "ifsc_code": distributor.ifsc_code,
        "address": distributor.address,
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"SAP sync failed: {e}")
        return False
