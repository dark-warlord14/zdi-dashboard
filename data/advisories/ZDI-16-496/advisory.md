# ZDI-16-496: Apple OS X DspFuncLib Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-496
- **ZDI-CAN:** ZDI-CAN-3598
- **Date:** 2016-08-29
- **CVE:** CVE-2016-4648
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Jack Tang and Moony Li of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-496/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the DspFuncLib extension. The issue lies in the failure to properly handle error conditions leading to a dangling pointer being reused after it has been freed. An attacker can leverage this vulnerability to raise privileges and execute code under the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT206903

## Disclosure Timeline

- 2016-04-01 - Vulnerability reported to vendor
- 2016-08-29 - Coordinated public release of advisory
