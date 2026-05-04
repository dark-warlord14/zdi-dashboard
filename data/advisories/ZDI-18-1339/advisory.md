# ZDI-18-1339: (Pwn2Own) Apple macOS task_set_special_port Port Overwrite Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1339
- **ZDI-CAN:** ZDI-CAN-5821
- **Date:** 2018-11-05
- **CVE:** CVE-2018-4237
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Samuel Gross (saelo)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1339/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Mach ports. The issue results from ability to modify ports that are inherited by child processes. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208848

## Disclosure Timeline

- 2018-04-07 - Vulnerability reported to vendor
- 2018-11-05 - Coordinated public release of advisory
- 2018-11-05 - Advisory Updated
