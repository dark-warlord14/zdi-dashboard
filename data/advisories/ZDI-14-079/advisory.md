# ZDI-14-079: Microsoft Internet Explorer CAttrArray Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-079
- **ZDI-CAN:** ZDI-CAN-2111
- **Date:** 2014-04-10
- **CVE:** CVE-2014-1753
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Yuki Chen of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CAttrArray objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms14-018

## Disclosure Timeline

- 2014-03-31 - Vulnerability reported to vendor
- 2014-04-10 - Coordinated public release of advisory
