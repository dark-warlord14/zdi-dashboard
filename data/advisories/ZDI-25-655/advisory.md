# ZDI-25-655: Samsung MagicINFO 9 Server downloadChangedFiles Directory Traversal Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-655
- **ZDI-CAN:** ZDI-CAN-26520
- **Date:** 2025-07-28
- **CVE:** CVE-2025-54438
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** MagicINFO 9 Server
- **Credit:** Paolo `paupu` Cavaglia of Shielder, Abdel Adim `smaury` Oisfi of Shielder and Nicola `fromVeeko` Davico of Shielder
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-655/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Samsung MagicINFO 9 Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloadChangedFiles function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungtv.com/securityUpdates

## Disclosure Timeline

- 2025-04-16 - Vulnerability reported to vendor
- 2025-07-28 - Coordinated public release of advisory
- 2025-07-28 - Advisory Updated
