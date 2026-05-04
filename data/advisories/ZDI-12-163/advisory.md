# ZDI-12-163: (0Day) HP iNode Management Center iNodeMngChecker.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-163
- **ZDI-CAN:** ZDI-CAN-1358
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** iNode Management Center
- **Credit:** Anonymous Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-163/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP H3C/3Com iNode Management Center. Authentication is not required to exploit this vulnerability. The flaw exists within the iNOdeMngChecker.exe component which listens by default on TCP port 9090. When handling the 0x0A0BF007 packet type the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline.

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
