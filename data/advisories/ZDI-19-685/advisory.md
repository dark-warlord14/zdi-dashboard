# ZDI-19-685: Apple macOS diskmanagementd Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-685
- **ZDI-CAN:** ZDI-CAN-8320
- **Date:** 2019-07-24
- **CVE:** CVE-2019-8697
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ccpwd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-685/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the diskmanagementd daemon. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210348

## Disclosure Timeline

- 2019-05-31 - Vulnerability reported to vendor
- 2019-07-24 - Coordinated public release of advisory
