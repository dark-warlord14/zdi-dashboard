# ZDI-11-152: HP Data Protector Backup Client Service GET_FILE Directory Traversal Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-152
- **ZDI-CAN:** ZDI-CAN-1179
- **Date:** 2011-04-29
- **CVE:** CVE-2011-1736
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-152/
## Vulnerability Details

This vulnerability allows remote attackers directory traversal on vulnerable installations of HP OpenView Data Protector. Authentication is not required to exploit this vulnerability. This specific flaw exists in the Backup Client Service (OmniInet.exe). The Backup Client Service listens on TCP port 5555 for communications between systems in the cell. The process has insufficient sanitization on user-supplied data when handling certain messages. Remote, unauthenticated attackers can exploit this vulnerability by sending crafted filename strings to the target, which would allow attackers to view or download arbitrary files on the target system.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02810240

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-04-29 - Coordinated public release of advisory
