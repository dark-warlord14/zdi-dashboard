# ZDI-12-155: InduSoft Thin Client ISSymbol InternationalOrder Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-155
- **ZDI-CAN:** ZDI-CAN-1341
- **Date:** 2012-08-22
- **CVE:** CVE-2011-0340
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Indusoft
- **Affected Products:** WebStudio
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-155/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Indusoft Thin Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ISSymbol.ocx ActiveX component. When an overly large string is passed as the 'InternationalOrder' parameter, a heap overflow occurs. This vulnerability can be leveraged to execute code under the context of the user running the browser.

## Additional Details

Indusoft has issued an update to correct this vulnerability. More details can be found at: http://www.indusoft.com/hotfixes/hotfixes.php

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
