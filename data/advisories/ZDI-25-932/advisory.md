# ZDI-25-932: MLflow Weak Password Requirements Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-932
- **ZDI-CAN:** ZDI-CAN-26916
- **Date:** 2025-10-03
- **CVE:** CVE-2025-11200
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MLflow
- **Affected Products:** MLflow
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-932/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of MLflow. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of passwords. The issue results from weak password requirements. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

MLflow has issued an update to correct this vulnerability. More details can be found at: https://github.com/mlflow/mlflow/commit/1f74f3f24d8273927b8db392c23e108576936c54

## Disclosure Timeline

- 2025-04-09 - Vulnerability reported to vendor
- 2025-10-03 - Coordinated public release of advisory
- 2025-10-03 - Advisory Updated
