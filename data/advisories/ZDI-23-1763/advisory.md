# ZDI-23-1763: Apple macOS Hydra Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1763
- **ZDI-CAN:** ZDI-CAN-21505
- **Date:** 2023-12-07
- **CVE:** CVE-2023-42826
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1763/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the Hydra library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the Hydra framework. Crafted data in an image can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213940

## Disclosure Timeline

- 2023-06-27 - Vulnerability reported to vendor
- 2023-12-07 - Coordinated public release of advisory
