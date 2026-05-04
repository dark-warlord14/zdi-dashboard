# ZDI-22-811: Apple macOS PackageKit PKInstallSandbox SIP Bypass vulnerability

## Metadata

- **ZDI ID:** ZDI-22-811
- **ZDI-CAN:** ZDI-CAN-16024
- **Date:** 2022-06-02
- **CVE:** CVE-2022-22583
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-811/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within PackageKit. The issue results from improper access control. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213055

## Disclosure Timeline

- 2021-11-18 - Vulnerability reported to vendor
- 2022-06-02 - Coordinated public release of advisory
- 2022-06-02 - Advisory Updated
