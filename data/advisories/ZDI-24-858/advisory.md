# ZDI-24-858: (Pwn2Own) Phoenix Contact CHARX SEC-3100 OCPP Protocol Missing Encryption Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-858
- **ZDI-CAN:** ZDI-CAN-23225
- **Date:** 2024-06-21
- **CVE:** CVE-2024-26288
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-858/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the OCPP protocol. The issue results from a lack of encryption. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
