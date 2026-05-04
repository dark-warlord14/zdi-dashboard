# ZDI-13-268: ABB MicroSCADA Wserver wserver.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-268
- **ZDI-CAN:** ZDI-CAN-1772
- **Date:** 2013-11-24
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** ABB
- **Affected Products:** MicroSCADA
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-268/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB MicroSCADA Wserver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the wserver.exe component which listens on TCP port 12221. This component performs insufficient bounds checking on user-supplied data which results in stack corruption. An attacker can leverage this situation to execute code under the context of the user running the application.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: http://www05.abb.com/global/scot/scot229.nsf/veritydisplay/41ccfa8ccd0431e6c1257c1200395574/$file/ABB_SoftwareVulnerabilityHandlingAdvisory_ABB-VU-PSAC-1MRS235805.pdf

## Disclosure Timeline

- 2013-02-13 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
