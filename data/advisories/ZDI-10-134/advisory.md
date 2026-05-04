# ZDI-10-134: Mozilla Firefox DOM Attribute Cloning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-134
- **ZDI-CAN:** ZDI-CAN-832
- **Date:** 2010-07-20
- **CVE:** CVE-2010-1208
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to a workaround that was implemented in order to support recursive cloning of attribute nodes. If an event is added to the first attribute node, the application can be made to free the node, and then later access a reference to it. This can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-35.html

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-07-20 - Coordinated public release of advisory
