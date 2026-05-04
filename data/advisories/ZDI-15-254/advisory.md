# ZDI-15-254: Microsoft Internet Explorer COptionElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-254
- **ZDI-CAN:** ZDI-CAN-2842
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1755
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-254/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes HTML option elements that are placed inside datalist elements. By manipulating a document's elements an attacker can force a COptionElement object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-056.aspx

## Disclosure Timeline

- 2015-04-07 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
