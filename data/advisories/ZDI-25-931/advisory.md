# ZDI-25-931: MLflow Tracking Server Model Creation Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-931
- **ZDI-CAN:** ZDI-CAN-26921
- **Date:** 2025-10-03
- **CVE:** CVE-2025-11201
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MLflow
- **Affected Products:** MLflow
- **Credit:** Mas Fadilullah dzaki
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-931/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MLflow Tracking Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of model file paths. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

MLflow has issued an update to correct this vulnerability. More details can be found at: https://github.com/B-Step62/mlflow/commit/2e02bc7bb70df243e6eb792689d9b8eba0013161

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-10-03 - Coordinated public release of advisory
- 2025-10-03 - Advisory Updated
