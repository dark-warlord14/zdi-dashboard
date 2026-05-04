# ZDI-24-1445: Apple macOS ICC Profile Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1445
- **ZDI-CAN:** ZDI-CAN-25085
- **Date:** 2024-10-31
- **CVE:** CVE-2024-44236
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Hossein Lotfi (@hosselot) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1445/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ICC profiles. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/121564

## Disclosure Timeline

- 2024-08-09 - Vulnerability reported to vendor
- 2024-10-31 - Coordinated public release of advisory
- 2024-10-31 - Advisory Updated
