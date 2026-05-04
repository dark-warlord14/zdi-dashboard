# ZDI-24-1444: Apple SceneKit Improper Validation of Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1444
- **ZDI-CAN:** ZDI-CAN-25204
- **Date:** 2024-10-31
- **CVE:** CVE-2024-44218
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** SceneKit
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1444/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the Scenekit framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the Scenekit framework. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/121564

## Disclosure Timeline

- 2024-08-20 - Vulnerability reported to vendor
- 2024-10-31 - Coordinated public release of advisory
- 2024-10-31 - Advisory Updated
