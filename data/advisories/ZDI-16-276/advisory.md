# ZDI-16-276: Microsoft Internet Explorer AcquireLineBoxBuilderForLayout Null Array Base Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-276
- **ZDI-CAN:** ZDI-CAN-3509
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0192
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zheng Huang of Baidu Scloud XTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer performs layout of web pages. By manipulating a document's elements an attacker can cause Internet Explorer to use a null pointer as the base address of an array read. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-051.aspx

## Disclosure Timeline

- 2016-02-01 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
