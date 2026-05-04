# ZDI-24-665: (Pwn2Own) Mozilla Firefox Exposed Dangerous Function Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-665
- **ZDI-CAN:** ZDI-CAN-23848
- **Date:** 2024-06-12
- **CVE:** CVE-2024-29944
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-665/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Mozilla Firefox. An attacker must first obtain the ability to execute low-privileged code in the renderer process in order to exploit this vulnerability. The specific flaw exists within the SessionStore component. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escape the sandbox and execute arbitrary code in the context of the current user at medium integrity.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2024-15/#CVE-2024-29944

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
