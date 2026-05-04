# ZDI-19-290: Apple macOS SCSITaskUserClient Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-290
- **ZDI-CAN:** ZDI-CAN-7889
- **Date:** 2019-03-26
- **CVE:** CVE-2019-8529
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Juwei Lin(@panicaII) of TrendMicro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-290/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SCSITaskUserClient module. The issue triggers a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209599

## Disclosure Timeline

- 2019-01-21 - Vulnerability reported to vendor
- 2019-03-26 - Coordinated public release of advisory
