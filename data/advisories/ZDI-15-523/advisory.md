# ZDI-15-523: Microsoft Internet Explorer empty-cells Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-523
- **ZDI-CAN:** ZDI-CAN-3119
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6045
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zheng Huang of Baidu Scloud XTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-523/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer performs layout of table cells when the CSS empty-cells property is specified. By manipulating a document's elements an attacker can force a CElement-derived object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-106

## Disclosure Timeline

- 2015-08-21 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
