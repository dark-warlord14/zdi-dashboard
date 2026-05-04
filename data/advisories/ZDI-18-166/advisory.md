# ZDI-18-166: Microsoft Windows SMB Client Improper Initialization Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-166
- **ZDI-CAN:** ZDI-CAN-5441
- **Date:** 2018-02-21
- **CVE:** CVE-2018-0833
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nabeel Ahmed and Eric Schayes from Dimension Data
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-166/
## Vulnerability Details

This vulnerability allows remote attackers to deny service to vulnerable installations of Microsoft Windows. In some cases, user interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file, but attack vectors may vary depending on the implementation. The specific flaw exists within the mrxsmb.sys driver. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to deny access to the target system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0833

## Disclosure Timeline

- 2017-12-01 - Vulnerability reported to vendor
- 2018-02-21 - Coordinated public release of advisory
- 2018-02-21 - Advisory Updated
