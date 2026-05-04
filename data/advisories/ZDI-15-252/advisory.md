# ZDI-15-252: (Pwn2Own) Microsoft Internet Explorer mergeAttributes Uninitialized Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-252
- **ZDI-CAN:** ZDI-CAN-2828
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1745
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Yuki Chen of Qihoo 360
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-252/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer merges attributes of HTML elements. By manipulating a document's elements an attacker can cause a CAttrValue object to be created with uninitialized data. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
