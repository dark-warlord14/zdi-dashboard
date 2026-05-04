# ZDI-12-168: InduSoft Thin Client ISSymbol InternationalSeparator Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-168
- **ZDI-CAN:** ZDI-CAN-1342
- **Date:** 2012-08-29
- **CVE:** CVE-2011-0340
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Indusoft
- **Affected Products:** WebStudio
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-168/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Indusoft Thin Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ISSymbol.ocx ActiveX component. The process performs insufficient bounds checking on user-supplied data passed in as the 'InternationalSeparator' parameter which results in a heap overflow. This vulnerability can be leveraged to execute code under the context of the user running the browser.

## Additional Details

Indusoft has issued an update to correct this vulnerability. More details can be found at: http://www.indusoft.com/hotfixes/hotfixes.php

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
