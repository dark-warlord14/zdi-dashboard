# ZDI-24-859: (Pwn2Own) Phoenix Contact CHARX SEC-3100 MTQQ Protocol JSON Parsing Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-859
- **ZDI-CAN:** ZDI-CAN-23239
- **Date:** 2024-06-21
- **CVE:** CVE-2024-26000
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Midnight Blue / PHP Hooligans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-859/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of JSON-encoded arrays. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
