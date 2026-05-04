# ZDI-11-021: Icon Labs Iconfidant SSL Server Key Length Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-021
- **ZDI-CAN:** ZDI-CAN-403
- **Date:** 2011-01-20
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Icon Labs
- **Affected Products:** Iconfidant SSL
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Icon Labs Iconfidant SSL Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the functionality responsible for key exchange. If the sum of specific length fields within a client master key packet exceeds 0x4000, a static buffer can be overflowed leading to arbitrary code execution on the affected system.

## Additional Details

Icon Labs states that this issue was first fixed in Iconfidant SSL 1.3.0 and recommends upgrading to Iconfidant 1.3.1. Please contact Icon Labs at support@icon-labs.com to update the latest Iconfidant SSL software. "Icon Labs would like to thank an Anonymous researcher and TippingPoint's Zero Day Initiative for responsibly reporting this vulnerability, ZDI-CAN-403."

## Disclosure Timeline

- 2008-10-28 - Vulnerability reported to vendor
- 2011-01-20 - Coordinated public release of advisory
