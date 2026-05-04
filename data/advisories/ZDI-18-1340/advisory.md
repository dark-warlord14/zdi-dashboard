# ZDI-18-1340: (Pwn2Own) Apple macOS Dock Service DSSetDesktopForDisplayAndSpace Uninitialized Pointer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1340
- **ZDI-CAN:** ZDI-CAN-5827
- **Date:** 2018-11-05
- **CVE:** CVE-2018-4196
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** MWR Labs - Alex Plaskett Georgi Geshev Fabian Beterke
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1340/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Mach messages to the Dock. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker could leverage this vulnerability to execute code within the context of the Dock process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208854

## Disclosure Timeline

- 2018-04-07 - Vulnerability reported to vendor
- 2018-11-05 - Coordinated public release of advisory
- 2018-12-20 - Advisory Updated
