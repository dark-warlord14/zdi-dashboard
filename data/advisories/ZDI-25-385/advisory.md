# ZDI-25-385: Siemens TeleControl Server Basic RestoreFromBackup SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-385
- **ZDI-CAN:** ZDI-CAN-25923
- **Date:** 2025-06-16
- **CVE:** CVE-2025-29905
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** TeleControl Server Basic
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-385/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens TeleControl Server Basic. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the RestoreFromBackup method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-443402.html

## Disclosure Timeline

- 2025-03-04 - Vulnerability reported to vendor
- 2025-06-16 - Coordinated public release of advisory
- 2025-06-16 - Advisory Updated
