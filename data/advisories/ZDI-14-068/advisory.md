# ZDI-14-068: SolarWinds Firewall Security Manager FSMWebService Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-068
- **ZDI-CAN:** ZDI-CAN-1898
- **Date:** 2014-04-08
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** SolarWinds
- **Affected Products:** Firewall Security Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Firewall Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FSMWebService service. The issue lies within the DownloadFileServlet servlet which fails to prevent directory traversal within all parameters. An attacker can leverage this vulnerability to retrieve arbitrary files as the SYSTEM user.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/Orion/docs/ReleaseNotes/releaseNotes.htm

## Disclosure Timeline

- 2013-10-27 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
