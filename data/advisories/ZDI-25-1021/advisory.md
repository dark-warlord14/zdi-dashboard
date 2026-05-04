# ZDI-25-1021: Siemens SINEC NMS getTotalAndFilterCounts SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1021
- **ZDI-CAN:** ZDI-CAN-26570
- **Date:** 2025-11-25
- **CVE:** CVE-2025-40755
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** SINEC NMS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1021/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Siemens SINEC NMS. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the getTotalAndFilterCounts method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-318832.html

## Disclosure Timeline

- 2025-06-27 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
