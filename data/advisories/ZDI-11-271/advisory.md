# ZDI-11-271: Mozilla Firefox appendChild DOM Tree Inconsistency Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-271
- **ZDI-CAN:** ZDI-CAN-1141
- **Date:** 2011-08-17
- **CVE:** CVE-2011-2378
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-271/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw results when .setUserData() handlers are used with an object and .appendChild() is called within a handler. Ultimately the import operation resulting from an .appendChild() is not guarded from mutation, and invalid DOM trees can result. Invalid DOM trees can be navigated resulting in dereferencing invalid pointers which can be leveraged to execute arbitrary code in the context of the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-30.html#cve-2011-2378

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-08-17 - Coordinated public release of advisory
