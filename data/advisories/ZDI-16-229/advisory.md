# ZDI-16-229: Microsoft Internet Explorer CAttrValue Double-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-229
- **ZDI-CAN:** ZDI-CAN-3366
- **Date:** 2016-04-12
- **CVE:** CVE-2015-6065
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** B6BEB4D5E828CF0CCB47BB24AAC22515
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of CAttrValue objects. By manipulating a document's elements, an attacker can force a double free condition to occur. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-112

## Disclosure Timeline

- 2015-11-02 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
