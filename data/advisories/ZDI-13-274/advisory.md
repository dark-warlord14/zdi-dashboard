# ZDI-13-274: IBM Forms Viewer 'fontname' Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-274
- **ZDI-CAN:** ZDI-CAN-1976
- **Date:** 2013-12-15
- **CVE:** CVE-2013-5447
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Forms Viewer
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-274/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Forms Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within a document handler of an XFDL document. The parsing of the 'fontname' tag with a large value can lead to a stack buffer overflow. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21657500

## Disclosure Timeline

- 2013-09-27 - Vulnerability reported to vendor
- 2013-12-15 - Coordinated public release of advisory
