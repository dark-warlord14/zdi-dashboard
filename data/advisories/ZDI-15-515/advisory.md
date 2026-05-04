# ZDI-15-515: Microsoft Windows JavaScript Regular Expression Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-515
- **ZDI-CAN:** ZDI-CAN-2899
- **Date:** 2015-10-13
- **CVE:** CVE-2015-2482
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-515/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to search and replace operations performed using JavaScript regular expressions. An attacker can cause the in-memory representation of a regular expression to be freed while it is being used in a replace operation. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-108

## Disclosure Timeline

- 2015-04-23 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
