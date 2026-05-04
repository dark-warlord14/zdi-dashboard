# ZDI-16-590: Apple Safari JavaScriptCore Array Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-590
- **ZDI-CAN:** ZDI-CAN-3875
- **Date:** 2016-11-04
- **CVE:** CVE-2016-4677
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-590/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Array objects. A crafted Array object can trigger a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207271

## Disclosure Timeline

- 2016-08-23 - Vulnerability reported to vendor
- 2016-11-04 - Coordinated public release of advisory
