# ZDI-12-128: Mozilla Firefox nsHTMLSelectElement Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-128
- **ZDI-CAN:** ZDI-CAN-1301
- **Date:** 2012-08-03
- **CVE:** CVE-2011-3671
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-128/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within nsINode::ReplaceOrInsertBefore() in content/base/src/nsGenericElement.cpp. A use-after-free condition can be triggered by adding an already parented option element to an option collection and then removing its associated select element during an event handler execution. Successful exploitation of this vulnerability will lead to code execution in the context of the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.mozilla.org/show_bug.cgi?id=335998

## Disclosure Timeline

- 2011-12-07 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
