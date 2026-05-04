# ZDI-13-091: Oracle Document Capture BlackIceDevMode.ocx ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-091
- **ZDI-CAN:** ZDI-CAN-1551
- **Date:** 2013-05-29
- **CVE:** CVE-2013-1516
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Document Capture
- **Credit:** Francis Provencher From Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Document Capture. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the BlackIceDevMode.ocx ActiveX control. This component performs insufficient bounds checking on user-supplied data passed in the SetAnnotationFont() method which results in stack corruption. This corruption can be leveraged to achieve code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2013-1899555.html

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
