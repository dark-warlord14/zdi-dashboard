# ZDI-14-309: Microsoft Internet Explorer Empty CAttrValue Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-309
- **ZDI-CAN:** ZDI-CAN-2353
- **Date:** 2014-09-16
- **CVE:** CVE-2014-4096
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** cloudfuzzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-309/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles style attributes which have been set to a value and then emptied. By emptying a style attribute and then performing specific manipulations on the document, an attacker can cause Internet Explorer to read from a memory location which has not been initialized. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-052

## Disclosure Timeline

- 2014-05-28 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
