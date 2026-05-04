# ZDI-17-190: Apple macOS M4A Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-190
- **ZDI-CAN:** ZDI-CAN-4414
- **Date:** 2017-03-28
- **CVE:** CVE-2017-2430
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** 734388278a34721ed1869ab23235b2c976a145e2
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-190/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of M4A files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to achieve remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2017-01-20 - Vulnerability reported to vendor
- 2017-03-28 - Coordinated public release of advisory
