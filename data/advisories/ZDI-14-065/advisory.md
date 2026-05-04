# ZDI-14-065: SolarWinds Server and Application Monitor C1Chart3D8 Array Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-065
- **ZDI-CAN:** ZDI-CAN-1978
- **Date:** 2014-04-08
- **CVE:** N/A
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Server and Application Monitor
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Server and Application Monitor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the C1Chart3D8 ActiveX control. The issue lies in the usage of the LoadURL method to load an OC3 file. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/Orion/docs/ReleaseNotes/releaseNotes.htm

## Disclosure Timeline

- 2013-10-27 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
