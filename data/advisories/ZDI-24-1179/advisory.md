# ZDI-24-1179: Apple macOS AMDRadeonX6000MTLDriver KTX Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1179
- **ZDI-CAN:** ZDI-CAN-24068
- **Date:** 2024-08-23
- **CVE:** CVE-2024-27857
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1179/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the Metal framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AMDRadeonX6000MTLDriver. Crafted data in a KTX image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/120906

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-08-23 - Coordinated public release of advisory
- 2024-08-23 - Advisory Updated
