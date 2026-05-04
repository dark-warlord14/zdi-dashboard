# ZDI-25-805: (0Day) Vacron Camera ping Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-805
- **ZDI-CAN:** ZDI-CAN-25892
- **Date:** 2025-08-06
- **CVE:** CVE-2025-8613
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Vacron
- **Affected Products:** Camera
- **Credit:** Steven C Yu of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-805/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Vacron Camera devices. Authentication is required to exploit this vulnerability. The specific flaw exists within the webs.cgi endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

12/06/24 – ZDI requested the vendor PSIRT contacts 12/06/24 – ZDI received a confirmation email from the vendor 07/25/25 – ZDI asked for updates and notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
