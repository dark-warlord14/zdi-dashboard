# ZDI-22-798: (Pwn2Own) Mozilla Firefox Improper Input Validation Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-798
- **ZDI-CAN:** ZDI-CAN-17418
- **Date:** 2022-05-27
- **CVE:** CVE-2022-1529
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-798/
## Vulnerability Details

This vulnerability allows local attackers to escape the sandbox on affected installations of Mozilla Firefox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the NotificationsDB module. The issue results from the lack of input validation in messages sent to the parent process. An attacker can leverage this vulnerability to escape the sandbox and execute arbitrary code in the context of the privileged parent process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2022-19/

## Disclosure Timeline

- 2022-05-26 - Vulnerability reported to vendor
- 2022-05-27 - Coordinated public release of advisory
