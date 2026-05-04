# ZDI-18-1326: Apple macOS NECP Control Socket Type Confusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1326
- **ZDI-CAN:** ZDI-CAN-6378
- **Date:** 2018-10-30
- **CVE:** CVE-2018-4425
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** cc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1326/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of NECP control sockets. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-07-12 - Vulnerability reported to vendor
- 2018-10-30 - Coordinated public release of advisory
- 2018-10-30 - Advisory Updated
