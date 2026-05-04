# ZDI-12-132: IBM Lotus iNotes dwa85W ActiveX Attachment_Times Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-132
- **ZDI-CAN:** ZDI-CAN-1439
- **Date:** 2012-08-03
- **CVE:** CVE-2012-2175
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Lotues iNotes
- **Credit:** Gaurav Baruah of eSecForte Technologies Pvt. Ltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus iNotes. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dwa85W.cab ActiveX control. When passing a long string argument to the Attachment_Times parameter during the control instantiation it is possible to overflow a stack buffer causing memory corruption. This can be leveraged by an attacker to execute code under the context of the user running the browser.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-304.ibm.com/support/docview.wss?uid=swg21596862

## Disclosure Timeline

- 2011-12-07 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
