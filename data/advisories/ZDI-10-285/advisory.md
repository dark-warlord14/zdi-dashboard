# ZDI-10-285: Novell ZENworks Desktop Management Linux TFTPD Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-285
- **ZDI-CAN:** ZDI-CAN-847
- **Date:** 2010-12-13
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Francis Provencher for Protek Researchh Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks Desktop Management. Authentication is not required to exploit this vulnerability. The flaw exists within the tftpd server component which listens by default on UDP port 69. When handling the filename in a Read Request (0x01) packet type the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the tftpd server process.

## Additional Details

Fixed in ZENworks 7 Desktop Management Support Pack 1 Interim Release 4 Hot Patch 5: http://download.novell.com/Download?buildid=r9kcCymJ7Os Documented in TID 7007321 http://www.novell.com/support/dynamickc.do?cmd=show&forward=nonthreadedKC&docType=kc&externalId=7007321&sliceId=1

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-12-13 - Coordinated public release of advisory
