# ZDI-14-391: Cisco OpenH264 Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-391
- **ZDI-CAN:** ZDI-CAN-2414
- **Date:** 2014-12-03
- **CVE:** CVE-2014-8001
- **CVSS:** 9.5
- **CVSS Vector:** AV:U/AC:L/Au:U/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** OpenH264
- **Credit:** Оксана
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-391/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on applications using vulnerable versions of Cisco OpenH264. The specific flaw exists within the decoder logic. By providing malformed H.264 data to the decoder, an attacker can overwrite a heap buffer. This could result in the execution of arbitrary code in the context of the application.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/viewAlert.x?alertId=36500

## Disclosure Timeline

- 2014-07-25 - Vulnerability reported to vendor
- 2014-12-03 - Coordinated public release of advisory
