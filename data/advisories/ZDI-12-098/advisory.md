# ZDI-12-098: AOL Products dnUpdater ActiveX Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-098
- **ZDI-CAN:** ZDI-CAN-1421
- **Date:** 2012-06-21
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** America Online
- **Affected Products:** AOL Deskbar
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of America Online's Toolbar, Desktop, IM, and winamp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dnUpdater ActiveX Control. When initializing the ActiveX control object, dnu.exe assumes the 5th argument being used for the Init() method, to be a legitimate pointer to a function. This vulnerability can be leveraged to execute code under the context of the user.

## Additional Details

America Online has issued an update to correct this vulnerability. More details can be found at: http://client.web.aol.com/toolbarfiles/Prod/downloads/downloadupdater/dnupdatersetup.exe

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-21 - Coordinated public release of advisory
