# ZDI-19-657: Mozilla Firefox Language Pack XUL Injection Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-657
- **ZDI-CAN:** ZDI-CAN-8374
- **Date:** 2019-07-10
- **CVE:** CVE-2019-9811
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:N/S:C/C:L/I:L/A:L
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Niklas Baumstark (@_niklasb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-657/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Mozilla Firefox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists due to possibility of XUL injection via language pack. An attacker can leverage this vulnerability to escape the sandbox and execute code at medium integrity.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2019-21/

## Disclosure Timeline

- 2019-07-10 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
