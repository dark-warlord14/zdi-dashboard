# ZDI-23-1019: Apple macOS Hydra Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1019
- **ZDI-CAN:** ZDI-CAN-21503
- **Date:** 2023-08-04
- **CVE:** CVE-2023-38421
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1019/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the Hydra library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the Hydra framework. Crafted data in an image file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213843

## Disclosure Timeline

- 2023-06-27 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
