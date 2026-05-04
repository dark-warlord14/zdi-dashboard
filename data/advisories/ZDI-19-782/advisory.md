# ZDI-19-782: (Pwn2Own) Mozilla Firefox sync Universal Cross-Site Scripting Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-782
- **ZDI-CAN:** ZDI-CAN-8375
- **Date:** 2019-09-05
- **CVE:** CVE-2019-9812
- **CVSS:** 5.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:L
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Niklas Baumstark (@_niklasb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-782/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to a universal cross-site scripting issue when syncing accounts. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current user at medium integrity.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2019-25/#CVE-2019-9812

## Disclosure Timeline

- 2019-09-05 - Vulnerability reported to vendor
- 2019-09-05 - Coordinated public release of advisory
