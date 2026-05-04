# ZDI-09-052: CA Unicenter Software Delivery dtscore.dll Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-052
- **ZDI-CAN:** ZDI-CAN-233
- **Date:** 2009-08-07
- **CVE:** CVE-2009-2026
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** Unicenter Software Delivery
- **Credit:** Orlando Padilla and Peter Silberman
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-052/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates Unicenter Software Delivery. Authentication is not required to exploit this vulnerability. The specific flaw resides in the dtscore.dll library. The vulnerability is exposed through multiple processes listening on multiple ports. The vulnerable function is a token searching routine which will copy user supplied data into a fixed length stack buffer. Exploitation of this vulnerability leads to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID=214090

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2009-08-07 - Coordinated public release of advisory
