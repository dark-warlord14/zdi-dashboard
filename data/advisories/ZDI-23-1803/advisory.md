# ZDI-23-1803: Parallels Desktop Updater Improper Verification of Cryptographic Signature Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1803
- **ZDI-CAN:** ZDI-CAN-21817
- **Date:** 2023-12-19
- **CVE:** CVE-2023-50228
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1803/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Updater service. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2023-08-28 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
