# ZDI-16-207: Apple OS X IOGeneralMemoryDescriptor Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-207
- **ZDI-CAN:** ZDI-CAN-3315
- **Date:** 2016-03-22
- **CVE:** CVE-2016-1753
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-207/
## Vulnerability Details

This vulnerability allows local attackers to elevate privileges on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the IOGeneralMemoryDescriptor interface. The issue lies in the failure to test user-supplied input for integer overflow. An attacker can leverage this to escalate their privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206167

## Disclosure Timeline

- 2015-11-02 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
