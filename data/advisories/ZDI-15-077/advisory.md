# ZDI-15-077: Microsoft Internet Explorer CImgElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-077
- **ZDI-CAN:** ZDI-CAN-2631
- **Date:** 2015-03-10
- **CVE:** CVE-2015-0056
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes HTML img elements. By adding an img element to a document fragment and then performing certain manipulations, an attacker can force a CImgElement object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-018

## Disclosure Timeline

- 2014-11-26 - Vulnerability reported to vendor
- 2015-03-10 - Coordinated public release of advisory
