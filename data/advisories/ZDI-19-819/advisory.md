# ZDI-19-819: Apple macOS AMDRadeonX4000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-819
- **ZDI-CAN:** ZDI-CAN-9066
- **Date:** 2019-09-10
- **CVE:** CVE-2019-8692
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-819/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple MacOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the fillUBMSurfaceInfoInternal function in AMDRadeonX4000.kext. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210348

## Disclosure Timeline

- 2019-07-25 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
