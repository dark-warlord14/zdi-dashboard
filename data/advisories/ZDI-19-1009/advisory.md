# ZDI-19-1009: Apple macOS fseventsd Uninitialized Buffer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1009
- **ZDI-CAN:** ZDI-CAN-8613
- **Date:** 2019-12-11
- **CVE:** CVE-2019-8798
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ABC Research s.r.o.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1009/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the fseventsd daemon. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210722

## Disclosure Timeline

- 2019-08-07 - Vulnerability reported to vendor
- 2019-12-11 - Coordinated public release of advisory
