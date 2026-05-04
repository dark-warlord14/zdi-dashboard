# ZDI-24-1112: Apple macOS AMDRadeonX6000MTLDriver KTX Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1112
- **ZDI-CAN:** ZDI-CAN-24065
- **Date:** 2024-08-08
- **CVE:** CVE-2024-27857
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1112/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the Metal framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the AMDRadeonX6000MTLDriver. Crafted data in a KTX file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT214108

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-08-08 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
