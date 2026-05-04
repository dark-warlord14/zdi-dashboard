# ZDI-12-102: Novell iPrint Client nipplib.dll GetDriverSettings realm Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-102
- **ZDI-CAN:** ZDI-CAN-1345
- **Date:** 2012-06-27
- **CVE:** CVE-2011-4187
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required in that a target must visit a malicious page or open a malicious file. The flaw exists within the exposed GetDriverSettings method in the nipplib component imported by ienipp and npnipp. When encountering a realm parameter this user supplied value's length is not properly verified before copying into a fixed length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7010143

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-27 - Coordinated public release of advisory
