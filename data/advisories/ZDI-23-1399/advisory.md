# ZDI-23-1399: Visualware MyConnection Server doRTAAccessCTConfig Cross-Site Scripting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1399
- **ZDI-CAN:** ZDI-CAN-21613
- **Date:** 2023-09-08
- **CVE:** CVE-2023-42034
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Visualware
- **Affected Products:** MyConnection Server
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1399/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Visualware MyConnection Server. Minimal user interaction is required to exploit this vulnerability. The specific flaw exists within the doRTAAccessCTConfig method. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Visualware has issued an update to correct this vulnerability. More details can be found at: https://myconnectionserver.visualware.com/support/security-advisories

## Disclosure Timeline

- 2023-07-31 - Vulnerability reported to vendor
- 2023-09-08 - Coordinated public release of advisory
