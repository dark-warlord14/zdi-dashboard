# ZDI-19-641: Microsoft Windows Event Viewer XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-641
- **ZDI-CAN:** ZDI-CAN-6191
- **Date:** 2019-07-10
- **CVE:** CVE-2019-0948
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Sooraj K S
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-641/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Event Viewer. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose the contents of files in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0948

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
- 2019-07-10 - Advisory Updated
