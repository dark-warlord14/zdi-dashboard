# ZDI-16-231: Microsoft Internet Explorer CTableLayout AddRow Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-231
- **ZDI-CAN:** ZDI-CAN-3422
- **Date:** 2016-04-12
- **CVE:** CVE-2016-0159
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** B6BEB4D5E828CF0CCB47BB24AAC22515
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-231/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer keeps track of table rows when performing layout of HTML tables. By manipulating a document's elements an attacker can cause Internet Explorer to write beyond the end of an array of pointers to CTableRow objects. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-037

## Disclosure Timeline

- 2015-11-24 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
