# ZDI-16-020: Apple OS X IOAcceleratorFamily2 Out-Of-Bounds Indexing Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-020
- **ZDI-CAN:** ZDI-CAN-3316
- **Date:** 2016-01-22
- **CVE:** CVE-2016-1718
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin - Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-020/
## Vulnerability Details

This vulnerability allows local attackers to elevate privileges on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the IOAcceleratorFamily2 interface. The issue lies in the failure to properly test a user-supplied index to ensure it is within the bounds of an array. An attacker can leverage this to escalate their privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT205731

## Disclosure Timeline

- 2015-11-02 - Vulnerability reported to vendor
- 2016-01-22 - Coordinated public release of advisory
