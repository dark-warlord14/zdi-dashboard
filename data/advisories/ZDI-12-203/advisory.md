# ZDI-12-203: Honeywell HMIWeb Browser ActiveX Control RequestDSPLoad Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-203
- **ZDI-CAN:** ZDI-CAN-1437
- **Date:** 2012-12-21
- **CVE:** CVE-2012-2054
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Honeywell
- **Affected Products:** HMIWeb
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-203/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Honeywell HMIWeb. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ActiveX control defined within the HSCDSPRenderDll.dll file. The RequestDSPLoad method does not properly verify the length of a supplied argument before copying it into a fixed-length heap buffer. A remote attacker can abuse this to execute arbitrary code under the context of the user running the browser.

## Additional Details

http://www.us-cert.gov/control_systems/pdf/ICSA-12-150-01.pdf

## Disclosure Timeline

- 2011-11-23 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
