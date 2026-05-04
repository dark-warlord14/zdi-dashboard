# ZDI-12-148: GE Proficy Real-Time Information Portal Remote Interface Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-148
- **ZDI-CAN:** ZDI-CAN-1419
- **Date:** 2012-08-22
- **CVE:** CVE-2012-0232
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:N
- **Affected Vendors:** GE
- **Affected Products:** Proficy Real-Time Information Portal
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE Proficy Real-Time Information Portal. Authentication is not required to exploit this vulnerability. This specific flaw exists within the Remote Interface Service (rifsrvd.exe). The Remote Interface Service listens on TCP port 5159 by default. The process does not sufficiently validate two input strings that are used to create a configuration file on the server. Remote, unauthenticated attackers can exploit this vulnerability by sending malformed ID_SAVE_SRVC_CFG message packets to the target, which could ultimately lead to remote code execution under the context of the SYSTEM user.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: http://support.ge-ip.com/support/index?page=kbchannel&id=S:KB14768

## Disclosure Timeline

- 2011-10-17 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
