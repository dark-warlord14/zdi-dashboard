# ZDI-20-683: Apple macOS SkyLight Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-683
- **ZDI-CAN:** ZDI-CAN-10077
- **Date:** 2020-05-28
- **CVE:** CVE-2020-9841
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** ABC Research s.r.o.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-683/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SkyLight module. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of WindowServer.

## Additional Details

https://support.apple.com/en-gb/HT211170

## Disclosure Timeline

- 2020-03-18 - Vulnerability reported to vendor
- 2020-05-28 - Coordinated public release of advisory
