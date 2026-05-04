# ZDI-24-404: Apple macOS Metal Framework PVR File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-404
- **ZDI-CAN:** ZDI-CAN-22327
- **Date:** 2024-04-25
- **CVE:** CVE-2024-23264
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Meysam Firouzi @R00tkitsmm
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-404/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the Metal Framework library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of PVR files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT214084

## Disclosure Timeline

- 2023-11-16 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
