# ZDI-14-322: Microsoft Internet Explorer UpdateColumnAndColGroupStyles Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-322
- **ZDI-CAN:** ZDI-CAN-2487
- **Date:** 2014-09-16
- **CVE:** CVE-2014-4101
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Jose A. Vazquez of Yenteasy - Security Research -
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-322/
## Vulnerability Details

This vulnerability may allow remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer maintains an array of objects of type Tree::SComputedStyle tracking the styles applied to the columns or column groups of an HTML table. By manipulating a document's elements an attacker can cause Internet Explorer to use memory beyond the end of this array. An attacker may be able to leverage this vulnerability to execute code under the context of the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://go.microsoft.com/fwlink/?LinkId=509961

## Disclosure Timeline

- 2014-08-27 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
