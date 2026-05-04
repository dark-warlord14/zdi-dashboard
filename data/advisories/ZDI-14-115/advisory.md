# ZDI-14-115: SolarWinds Server and Application Monitor PEstrarg1 ActiveX Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-115
- **ZDI-CAN:** ZDI-CAN-1874
- **Date:** 2014-04-23
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Server and Application Monitor
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Server and Application Monitor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the PEstrarg1 property. The issue lies in a failure to validate the size of the input buffer before copying it into a fixed-size buffer on the heap. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/Orion/docs/ReleaseNotes/releaseNotes.htm

## Disclosure Timeline

- 2013-08-28 - Vulnerability reported to vendor
- 2014-04-23 - Coordinated public release of advisory
