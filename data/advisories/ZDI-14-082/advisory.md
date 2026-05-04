# ZDI-14-082: (Pwn2Own) Mozilla Firefox Pop-Up Blocker Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-082
- **ZDI-CAN:** ZDI-CAN-2215
- **Date:** 2014-04-11
- **CVE:** CVE-2014-1511
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Mariusz Mlynski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-082/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the pop-up blocker. The issue lies in the ability to forward calls to an unloaded window. An attacker can leverage this vulnerability in combination with another vulnerability to silently execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2014/mfsa2014-29.html

## Disclosure Timeline

- 2014-03-12 - Vulnerability reported to vendor
- 2014-04-11 - Coordinated public release of advisory
