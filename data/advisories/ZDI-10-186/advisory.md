# ZDI-10-186: IBM TSM FastBack _CalcHashValueWithLength Remote Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-186
- **ZDI-CAN:** ZDI-CAN-659
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-186/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of IBM Tivoli FastBack Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe which listens by default on tcp port 11406. The issue is due to an unchecked user supplied length value. This value is used to iterate over supplied data and calculate a CRC value. Successful exploitation leads to an unhandled access violation and immediate termination of the FastBackServer.exe process.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 3

## Disclosure Timeline

- 2010-01-22 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory
