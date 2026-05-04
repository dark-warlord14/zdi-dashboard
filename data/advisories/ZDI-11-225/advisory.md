# ZDI-11-225: Mozilla Firefox nsXULCommandDispatcher Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-225
- **ZDI-CAN:** ZDI-CAN-1203
- **Date:** 2011-06-21
- **CVE:** CVE-2011-0085
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-225/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the nsXULCommandDispatcher.cpp source code. During a NS_XUL_COMMAND_UPDATE event dispatch, the user is able to force command dispatcher to remove all the updaters in the mUpdaters chain including the one that is currently in use. As a result, the local variable updater becomes a stale pointer and updater->mNext refers to memory previously freed. Successful exploitation can lead to code execution in the context of the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-23.html

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-06-21 - Coordinated public release of advisory
