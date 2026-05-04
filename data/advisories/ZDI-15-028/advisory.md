# ZDI-15-028: Microsoft Internet Explorer Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-028
- **ZDI-CAN:** ZDI-CAN-2607
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0046
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-028/
## Vulnerability Details

This vulnerability allows remote attackers to disclose information on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DOM manipulations. By manipulating the DOM, an attacker can cause the browser to confuse an ActiveX control with a string. This could allow an attacker to disclose memory from the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-11-04 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
