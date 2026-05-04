# ZDI-20-1260: Apple macOS process_token_SetFence Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1260
- **ZDI-CAN:** ZDI-CAN-10924
- **Date:** 2020-10-19
- **CVE:** CVE-2020-9990
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ABC Research s.r.l.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1260/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppleIntelKBLGraphics kernel extension. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211289

## Disclosure Timeline

- 2020-05-19 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
