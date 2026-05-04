# ZDI-17-169: Microsoft Internet Explorer CHtmTag Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-169
- **ZDI-CAN:** ZDI-CAN-4058
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0018
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Kai Song(exp-sky) of Tencent's Xuanwu Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-169/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of HTML tags. By manipulating a document's elements an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to disclose sensitive information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms17-006.aspx

## Disclosure Timeline

- 2016-10-06 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
