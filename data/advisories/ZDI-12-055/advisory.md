# ZDI-12-055: Webkit.org Webkit copyNonAttributeProperties Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-055
- **ZDI-CAN:** ZDI-CAN-1415
- **Date:** 2012-04-09
- **CVE:** CVE-2011-3928
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the WebCore component as used by WebKit. Specifically within the handling of element properties. When importing a node having a nonattribute property such as an attached event, an object is improperly freed and accessed. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://prod.lists.apple.com/archives/security-announce/2012/Mar/msg00003.html

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-04-09 - Coordinated public release of advisory
