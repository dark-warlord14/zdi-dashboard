# ZDI-14-406: Microsoft Internet Explorer LineBoxBuilder::FindWord Out-Of-Bounds Memory Access Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-406
- **ZDI-CAN:** ZDI-CAN-2520
- **Date:** 2014-12-09
- **CVE:** CVE-2014-6376
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Garage4Hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-406/
## Vulnerability Details

This vulnerability consists of potentially hazardous use of memory on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer performs hyphenation of text on web pages. By presenting a specially formed web page to the browser, an attacker can cause Internet Explorer to access memory past the end of a buffer. This may give an attacker the ability to improperly influence the behavior of the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-080.aspx

## Disclosure Timeline

- 2014-09-04 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
