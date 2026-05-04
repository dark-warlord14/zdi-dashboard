# ZDI-26-231: Apple macOS Exposure of Sensitive Information to Unauthorized Sphere Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-231
- **ZDI-CAN:** ZDI-CAN-28499
- **Date:** 2026-03-30
- **CVE:** CVE-2026-20695
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** 이동하 (Lee Dong Ha of 0xb6)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-231/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within NVRAM variable logging. The issue results from the exposure of sensitive information to an unauthorized control sphere. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/126795

## Disclosure Timeline

- 2026-03-05 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
