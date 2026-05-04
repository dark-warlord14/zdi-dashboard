# ZDI-12-134: IBM Lotus Quickr QP2 ActiveX _Times Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-134
- **ZDI-CAN:** ZDI-CAN-1455
- **Date:** 2012-08-03
- **CVE:** CVE-2012-2176
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Quickr
- **Credit:** Gaurav Baruah of eSecForte Technologies Pvt. Ltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-134/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Quickr. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the QP2.cab ActiveX control. When passing a long string argument to the Attachment_Times or Import_Times parameters during the control's instantiation it is possible to overflow a stack buffer causing memory corruption. This can be leveraged by an attacker to execute code under the context of the user running the browser.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21596191

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
