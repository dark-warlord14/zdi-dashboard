# ZDI-16-360: (Pwn2Own) Apple OS X fontd Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-360
- **ZDI-CAN:** ZDI-CAN-3606
- **Date:** 2016-05-27
- **CVE:** CVE-2016-1797
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-360/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. Authentication is not required to exploit this vulnerability. The specific flaw exists within the sandbox policy for the fontd process. The issue lies in the failure to properly ensure the FontValidator binary is either excluded from the policy, or is also sandboxed. An attacker can leverage this in conjunction with other vulnerabilities to execute code outside the context of the Safari sandbox.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-27 - Coordinated public release of advisory
