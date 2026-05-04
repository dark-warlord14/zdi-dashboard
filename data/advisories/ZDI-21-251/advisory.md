# ZDI-21-251: Apple iOS FairplayIOKit Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-251
- **ZDI-CAN:** ZDI-CAN-12053
- **Date:** 2021-02-03
- **CVE:** CVE-2021-1791
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** Junzhi Lu(@pwn0rz), Qi Sun and Mickey Jin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-251/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple iOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the FairplayIOKit kext. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT212146

## Disclosure Timeline

- 2020-10-02 - Vulnerability reported to vendor
- 2021-02-03 - Coordinated public release of advisory
- 2021-02-24 - Advisory Updated
