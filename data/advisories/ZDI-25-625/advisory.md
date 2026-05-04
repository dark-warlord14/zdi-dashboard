# ZDI-25-625: Veeam Backup Enterprise Manager JobManagmentService Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-625
- **ZDI-CAN:** ZDI-CAN-26062
- **Date:** 2025-07-21
- **CVE:** CVE-2025-24286
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Veeam
- **Affected Products:** Backup Enterprise Manager
- **Credit:** Nikolai Skliarenko of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-625/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Veeam Backup Enterprise Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the JobManagmentService component. The issue results from improper access control. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Veeam has issued an update to correct this vulnerability. More details can be found at: https://www.veeam.com/kb4743

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-07-21 - Coordinated public release of advisory
- 2025-07-21 - Advisory Updated
