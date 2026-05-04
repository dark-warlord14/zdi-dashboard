# ZDI-19-857: Apple macOS diskmanagementd Uninitialized Buffer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-857
- **ZDI-CAN:** ZDI-CAN-8719
- **Date:** 2019-10-04
- **CVE:** CVE-2019-8539
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ccpwd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-857/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the diskmanagementd daemon. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210348

## Disclosure Timeline

- 2019-05-31 - Vulnerability reported to vendor
- 2019-10-04 - Coordinated public release of advisory
