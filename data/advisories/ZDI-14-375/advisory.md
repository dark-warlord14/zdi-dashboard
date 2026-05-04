# ZDI-14-375: Microsoft Internet Explorer CSecurityContext Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-375
- **ZDI-CAN:** ZDI-CAN-2404
- **Date:** 2014-11-19
- **CVE:** CVE-2014-4143
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** s3tm3m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-375/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer manages the lifetime of CSecurityContext objects. By manipulating a document's elements an attacker can force a CSecurityContext object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-065.aspx

## Disclosure Timeline

- 2014-07-07 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
