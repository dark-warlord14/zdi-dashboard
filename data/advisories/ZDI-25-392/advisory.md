# ZDI-25-392: Siemens TeleControl Server Basic UpdateSmtpSettings SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-392
- **ZDI-CAN:** ZDI-CAN-25919
- **Date:** 2025-06-16
- **CVE:** CVE-2025-31349
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** TeleControl Server Basic
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-392/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens TeleControl Server Basic. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the UpdateSmtpSettings method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker could leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-443402.html

## Disclosure Timeline

- 2025-03-19 - Vulnerability reported to vendor
- 2025-06-16 - Coordinated public release of advisory
- 2025-06-16 - Advisory Updated
