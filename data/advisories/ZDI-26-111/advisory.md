# ZDI-26-111: MLflow Use of Default Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-111
- **ZDI-CAN:** ZDI-CAN-28256
- **Date:** 2026-02-19
- **CVE:** CVE-2026-2635
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MLflow
- **Affected Products:** MLflow
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-111/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of MLflow. Authentication is not required to exploit this vulnerability. The specific flaw exists within the basic_auth.ini file. The file contains hard-coded default credentials. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of the administrator.

## Additional Details

MLflow has issued an update to correct this vulnerability. More details can be found at: https://github.com/mlflow/mlflow/pull/19260

## Disclosure Timeline

- 2025-10-14 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
