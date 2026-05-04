# ZDI-24-617: Logsign Unified SecOps Platform Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-617
- **ZDI-CAN:** ZDI-CAN-24165
- **Date:** 2024-06-12
- **CVE:** CVE-2024-5717
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-617/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Logsign Unified SecOps Platform. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the HTTP API. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/19316621924754-03-06-2024-Version-6-4-8-Release-Notes

## Disclosure Timeline

- 2024-05-31 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
