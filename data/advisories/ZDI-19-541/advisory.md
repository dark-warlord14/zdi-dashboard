# ZDI-19-541: Apple macOS kextutil Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-541
- **ZDI-CAN:** ZDI-CAN-8367
- **Date:** 2019-05-30
- **CVE:** CVE-2019-8606
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** phoenhex & qwerty team (@_niklasb @qwertyoruiopz and @bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-541/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of kernel extensions in kextutil. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code as the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-05-30 - Vulnerability reported to vendor
- 2019-05-30 - Coordinated public release of advisory
