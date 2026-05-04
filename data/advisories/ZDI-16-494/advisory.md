# ZDI-16-494: Apple OS X IOHIDFamily Heap Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-494
- **ZDI-CAN:** ZDI-CAN-3554
- **Date:** 2016-08-29
- **CVE:** CVE-2016-4650
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Peter Pi of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-494/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the IOHIDFamily kernel extension. The issue lies in the failure to validate a supplied length value causing a heap buffer overflow. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-02-12 - Vulnerability reported to vendor
- 2016-08-29 - Coordinated public release of advisory
