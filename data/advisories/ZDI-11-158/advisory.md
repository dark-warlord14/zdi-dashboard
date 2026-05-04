# ZDI-11-158: Mozilla Firefox OBJECT mChannel Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-158
- **ZDI-CAN:** ZDI-CAN-1032
- **Date:** 2011-05-10
- **CVE:** CVE-2011-0065
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the OnChannelRedirect method. When an OBJECT element has no mChannel assigned, it is possible to call the |OnChannelRedirect| method, setting a nearly arbitrary object as the channel in use. |mChannel| will become a dangling pointer, allowing an attacker to execute arbitrary code under the context of the user running the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-13.html

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-05-10 - Coordinated public release of advisory
