# ZDI-11-232: HP iNode Management Center iNodeMngChecker.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-232
- **ZDI-CAN:** ZDI-CAN-1082
- **Date:** 2011-07-01
- **CVE:** CVE-2011-1867
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** iNode Management Center
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-232/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP H3C/3Com iNode Management Center. Authentication is not required to exploit this vulnerability. The flaw exists within the iNOdeMngChecker.exe component which listens by default on TCP port 9090. When handling the 0x0A0BF007 packet type the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02901775

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-07-01 - Coordinated public release of advisory
