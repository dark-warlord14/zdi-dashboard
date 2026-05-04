# ZDI-14-392: Cisco OpenH264 Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-392
- **ZDI-CAN:** ZDI-CAN-2415
- **Date:** 2014-12-03
- **CVE:** CVE-2014-8002
- **CVSS:** 9.5
- **CVSS Vector:** AV:U/AC:L/Au:U/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** OpenH264
- **Credit:** Оксана
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-392/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on applications using vulnerable versions of Cisco OpenH264. The specific flaw exists within the decoder logic. By providing malformed H.264 data to the decoder, an attacker can force a dangling pointer to be referenced after it has been freed. This could result in the execution of arbitrary code in the context of the application.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/viewAlert.x?alertId=36501

## Disclosure Timeline

- 2014-07-25 - Vulnerability reported to vendor
- 2014-12-03 - Coordinated public release of advisory
