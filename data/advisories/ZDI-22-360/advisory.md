# ZDI-22-360: Apple macOS fclonefileat Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-360
- **ZDI-CAN:** ZDI-CAN-15320
- **Date:** 2022-02-16
- **CVE:** CVE-2021-30995
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-360/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of directory paths. The code is subject to a time-of-check/time-of-use race condition when performing path validation. An attacker can leverage this vulnerability to escalate privileges from low integrity and execute code in the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212979

## Disclosure Timeline

- 2021-09-24 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
