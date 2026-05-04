# ZDI-13-008: Novell GroupWise gwcls1.dll ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-008
- **ZDI-CAN:** ZDI-CAN-1329
- **Date:** 2013-02-01
- **CVE:** CVE-2012-0439
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaws exists within multiple methods exposed by gwcls1.dll. There are 20 methods which accept an XPItem pointer and perform operations on the potentially malicious pointer without validation. Additionally, the SetEngine() method accepts an unvalidated pointer and performs operations and method calls based upon it. An attacker can manipulate these behaviors to execute arbitrary code on the user's system in the context of the browser.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7011688

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
