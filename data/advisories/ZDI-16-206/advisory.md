# ZDI-16-206: Apple OS X IOUSBInterfaceUserClient Out-Of-Bounds Indexing Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-206
- **ZDI-CAN:** ZDI-CAN-3530
- **Date:** 2016-03-22
- **CVE:** CVE-2016-1749
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-206/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the IOUSBInterfaceUserClient interface. The issue lies in the failure to ensure that a user-supplied index is within the bounds of the allocated buffer. An attacker can leverage this to escalate their privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206167

## Disclosure Timeline

- 2016-02-04 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
