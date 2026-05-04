# ZDI-11-155: Sybase M-Business Anywhere Server agd.exe encodeUsername Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-155
- **ZDI-CAN:** ZDI-CAN-942
- **Date:** 2011-05-09
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sybase
- **Affected Products:** MBusiness Anywhere
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-155/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sybase MBusiness Anywhere. Authentication is not required to exploit this vulnerability. The flaw exists within the agd.exe component which listens by default on TCP port 80 and 443. When calling agd!encodeUsername the process creates a 100 byte buffer on the heap. The process then blindly copies user supplied data into that fixed-length buffer without verifying that the size of the destination buffer is adequately sized. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Sybase has issued an update to correct this vulnerability. More details can be found at: http://www.sybase.com/detail?id=1093029

## Disclosure Timeline

- 2011-01-20 - Vulnerability reported to vendor
- 2011-05-09 - Coordinated public release of advisory
