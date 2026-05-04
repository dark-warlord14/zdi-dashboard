# ZDI-11-145: HP Data Protector Backup Client Service GET_FILE Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-145
- **ZDI-CAN:** ZDI-CAN-1172
- **Date:** 2011-04-29
- **CVE:** CVE-2011-1729
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-145/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP OpenView Data Protector. Authentication is not required to exploit this vulnerability. This specific flaw exists in the Backup Client Service (OmniInet.exe). The Backup Client Service listens on TCP port 5555 for communications between systems in the cell. The process has insufficient bounds checking on user-supplied data in a fixed-length buffer on the stack. Remote, unauthenticated attackers can exploit this vulnerability by sending malformed GET_FILE message packets to the target, which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02810240

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-04-29 - Coordinated public release of advisory
