# ZDI-23-1654: Adobe FrameMaker Publishing Server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1654
- **ZDI-CAN:** ZDI-CAN-21344
- **Date:** 2023-11-15
- **CVE:** CVE-2023-44324
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** FrameMaker Publishing Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1654/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Adobe FrameMaker Publishing Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Login method. The issue results from improper implementation of the authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/framemaker/apsb23-58.html

## Disclosure Timeline

- 2023-07-20 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
