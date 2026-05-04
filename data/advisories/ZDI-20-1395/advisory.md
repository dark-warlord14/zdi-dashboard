# ZDI-20-1395: Apple macOS powerd Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1395
- **ZDI-CAN:** ZDI-CAN-11183
- **Date:** 2020-12-04
- **CVE:** CVE-2020-10007
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1395/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the powerd daemon. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211931

## Disclosure Timeline

- 2020-07-29 - Vulnerability reported to vendor
- 2020-12-04 - Coordinated public release of advisory
- 2024-07-08 - Advisory Updated
