# ZDI-25-211: (Pwn2Own) Synology BeeStation BST150-4T CRLF Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-211
- **ZDI-CAN:** ZDI-CAN-25613
- **Date:** 2025-04-09
- **CVE:** CVE-2024-50629
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Synology
- **Affected Products:** BeeStation BST150-4T
- **Credit:** Pumpkin Chang (@u1f383) and Orange Tsai (@orange_8361) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-211/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Synology BeeStation BST150-4T devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of HTTP requests. The issue results from the lack of proper validation of a user-supplied data before using it to prepare an HTTP response. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_24_20

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
