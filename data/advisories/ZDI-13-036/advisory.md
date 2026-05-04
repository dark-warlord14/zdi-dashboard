# ZDI-13-036: Novell GroupWise Messenger import Command Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-036
- **ZDI-CAN:** ZDI-CAN-1339
- **Date:** 2013-03-22
- **CVE:** CVE-2013-1085
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise Messenger. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of specific commands passed to the messenger via the nim:// protocol handler. By crafting a page with a large filename parameter within an import command, a stack-based buffer overflow can be made to occur. This can be exploited by an attacker to execute remote code under the context of the Administrator account.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7011935

## Disclosure Timeline

- 2012-01-24 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
