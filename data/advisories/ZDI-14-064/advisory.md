# ZDI-14-064: SolarWinds Server and Application Monitor wpdlx Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-064
- **ZDI-CAN:** ZDI-CAN-1899
- **Date:** 2014-04-08
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Server and Application Monitor
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-064/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Server and Application Monitor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the wpdlx ActiveX control. The issue lies in the failure to validate file types when loading and saving images. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/Orion/docs/ReleaseNotes/releaseNotes.htm

## Disclosure Timeline

- 2013-10-27 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
