# ZDI-22-1682: Apple Safari DFG JIT Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1682
- **ZDI-CAN:** ZDI-CAN-18337
- **Date:** 2022-12-21
- **CVE:** CVE-2022-42852
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** hazbinhotel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1682/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DFG JIT. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213530

## Disclosure Timeline

- 2022-10-14 - Vulnerability reported to vendor
- 2022-12-21 - Coordinated public release of advisory
