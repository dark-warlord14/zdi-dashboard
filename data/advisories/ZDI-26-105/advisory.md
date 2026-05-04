# ZDI-26-105: MLflow Tracking Server Artifact Handler Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-105
- **ZDI-CAN:** ZDI-CAN-26649
- **Date:** 2026-02-13
- **CVE:** CVE-2026-2033
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MLflow
- **Affected Products:** MLflow
- **Credit:** Muhammad Fadilullah Dzaki
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-105/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MLflow Tracking Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of artifact file paths. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

MLflow has issued an update to correct this vulnerability. More details can be found at: https://github.com/mlflow/mlflow/pull/19260

## Disclosure Timeline

- 2025-07-31 - Vulnerability reported to vendor
- 2026-02-13 - Coordinated public release of advisory
- 2026-02-13 - Advisory Updated
