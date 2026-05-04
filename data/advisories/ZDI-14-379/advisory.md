# ZDI-14-379: Microsoft Internet Explorer GetReplacedUrlImgCtxCookie Out-of-bounds Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-379
- **ZDI-CAN:** ZDI-CAN-2436
- **Date:** 2014-11-19
- **CVE:** CVE-2014-6344
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Jason Kratzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-379/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments passed to the GetReplacedUrlImgCtxCookie function. By manipulating a document's elements an attacker can access data outside the bounds of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-065.aspx

## Disclosure Timeline

- 2014-07-24 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
