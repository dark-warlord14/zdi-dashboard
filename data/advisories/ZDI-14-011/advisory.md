# ZDI-14-011: WellinTech KingScada KingGraphic kxClientDownload ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-011
- **ZDI-CAN:** ZDI-CAN-1552
- **Date:** 2014-02-05
- **CVE:** CVE-2013-2827
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WellinTech
- **Affected Products:** KingScada KingGraphic
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WellinTech KingScada KingGraphics. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the kxClientDownload.ocx ActiveX control. By properly setting the ProjectURL property, it is possible for an attacker to download and load an arbitrary DLL file from a remote location. An attacker can leverage this vulnerability to execute code under the context of the administrator.

## Additional Details

WellinTech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-13-344-01

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2014-02-05 - Coordinated public release of advisory
