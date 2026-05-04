# ZDI-18-880: (Pwn2Own) Google Android UserCallActivity Null Pointer Dereference Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-880
- **ZDI-CAN:** ZDI-CAN-5360
- **Date:** 2018-08-02
- **CVE:** N/A
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-880/
## Vulnerability Details

This vulnerability allows local attackers to force a reboot on vulnerable installations of Google Android. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of UserCallActivity. The issue lies in the failure to properly handle a NULL pointer dereference. An attacker can leverage this vulnerability to force the device to reboot.

## Additional Details

Patched with 2018 JAN SMR

## Disclosure Timeline

- 2017-11-01 - Vulnerability reported to vendor
- 2018-08-02 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
